# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Desktop visualisation module for curated microbiology SBML labs."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from biosim import BioModule
from biosim.signals import AcceptedSignalProfile, BioSignal, SignalSpec, scalar_or_record_input

VisualSpec = dict[str, Any]

SUMMARY_SCHEMA = {
    "duration_simulated": "float",
    "observable_count": "int",
    "largest_change_observable": "str",
    "largest_change_magnitude": "float",
    "peak_observable": "str",
    "peak_value": "float",
}


def _unwrap(value: Any) -> Any:
    if hasattr(value, "value"):
        value = value.value
    if isinstance(value, Mapping) and set(value) == {"payload"}:
        return value["payload"]
    return value


class MicrobiologyVisualisationModel(BioModule):
    def __init__(self, sources: list[dict[str, Any]], question: str, scope: str, caveat: str = "") -> None:
        self.sources = sources
        self.question = question
        self.scope = scope
        self.caveat = caveat or "The bundled source model is executed directly; labels are conservative where source symbols are ambiguous."
        self._latest: dict[str, Any] = {}
        self._history: dict[str, list[tuple[float, dict[str, float]]]] = {}
        self._time = 0.0

    def setup(self, config: Optional[dict[str, Any]] = None) -> None:
        self._latest = {}
        self._history = {source["alias"]: [] for source in self.sources}
        self._time = 0.0

    def inputs(self) -> dict[str, SignalSpec]:
        specs: dict[str, SignalSpec] = {}
        for source in self.sources:
            alias = source["alias"]
            observables = source.get("observables") or []
            labels = source.get("labels") or {}
            state_schema = {item["id"]: "float" for item in observables} or {"payload": "json"}
            label_schema = {str(key): "str" for key in labels} or {"payload": "json"}
            specs[f"{alias}_state"] = SignalSpec.record(
                schema=state_schema,
                accepted_profiles=(
                    AcceptedSignalProfile(signal_type="record", schema=state_schema),
                    AcceptedSignalProfile(signal_type="record", schema={"payload": "json"}),
                ),
                description="Current model state for visualisation.",
            )
            specs[f"{alias}_summary"] = SignalSpec.record(
                schema=SUMMARY_SCHEMA,
                accepted_profiles=(
                    AcceptedSignalProfile(signal_type="record", schema=SUMMARY_SCHEMA),
                    AcceptedSignalProfile(signal_type="record", schema={"payload": "json"}),
                ),
                description="Summary statistics from the core model.",
            )
            specs[f"{alias}_species_labels"] = SignalSpec.record(
                schema=label_schema,
                accepted_profiles=(
                    AcceptedSignalProfile(signal_type="record", schema=label_schema),
                    AcceptedSignalProfile(signal_type="record", schema={"payload": "json"}),
                ),
                description="Source observable labels.",
            )
            for output in source.get("headline_outputs") or []:
                description = output.get("label") or output["port"]
                specs[f"{alias}_{output['port']}"] = SignalSpec.scalar(
                    dtype="float64",
                    accepted_profiles=(
                        AcceptedSignalProfile(signal_type="scalar", dtype="float64"),
                        AcceptedSignalProfile(signal_type="record", schema={"payload": "json"}),
                    ),
                    description=description,
                )
        return specs

    def outputs(self) -> dict[str, SignalSpec]:
        return {}

    def set_inputs(self, inputs: dict[str, BioSignal]) -> None:
        for name, signal in (inputs or {}).items():
            value = _unwrap(signal)
            self._latest[name] = value
            emitted_at = float(getattr(signal, "emitted_at", self._time) or self._time)
            self._time = max(self._time, emitted_at)
            if name.endswith("_state") and isinstance(value, Mapping):
                alias = name[: -len("_state")]
                numeric = {}
                for key, raw in value.items():
                    try:
                        numeric[str(key)] = float(raw)
                    except (TypeError, ValueError):
                        continue
                if numeric:
                    self._history.setdefault(alias, []).append((emitted_at, numeric))

    def advance_window(self, start: float, end: float, inputs: Optional[dict[str, BioSignal]] = None) -> None:
        if inputs:
            self.set_inputs(inputs)
        self._time = max(self._time, float(end))

    def get_outputs(self) -> dict[str, BioSignal]:
        return {}

    def visualize(self) -> Optional[list[VisualSpec]]:
        visuals: list[VisualSpec] = []
        for source in self.sources:
            alias = source["alias"]
            labels = self._labels_for(source)
            latest_state = self._latest.get(f"{alias}_state")
            summary = self._latest.get(f"{alias}_summary") or {}
            if not isinstance(latest_state, Mapping):
                continue
            numeric_state = self._numeric_state(latest_state)
            if not numeric_state:
                continue
            answer = self._observed_answer(summary, numeric_state, labels)
            visuals.append({
                "render": "table",
                "title": "Scientific readout",
                "data": {"columns": ["Prompt", "Answer"], "rows": [
                    ["Scientific question", self.question],
                    ["Observed answer", answer],
                    ["Evidence", self._evidence(summary, numeric_state, labels)],
                    ["Dominant module", self.scope],
                    ["Caveat", self.caveat],
                ]},
            })
            series = self._timeseries(alias, source, labels)
            if series:
                visuals.append({
                    "render": "timeseries",
                    "title": "Observable trajectories",
                    "data": {"series": series},
                })
            items = self._headline_items(alias, source, numeric_state, labels)
            if items:
                visuals.append({
                    "render": "bar",
                    "title": "Current headline observables",
                    "data": {"items": items},
                })
        return visuals or None

    def _labels_for(self, source: Mapping[str, Any]) -> dict[str, str]:
        alias = source["alias"]
        labels = dict(source.get("labels") or {})
        signal_labels = self._latest.get(f"{alias}_species_labels")
        if isinstance(signal_labels, Mapping):
            labels.update({str(key): str(value) for key, value in signal_labels.items()})
        return labels

    @staticmethod
    def _numeric_state(state: Mapping[str, Any]) -> dict[str, float]:
        values = {}
        for key, raw in state.items():
            try:
                values[str(key)] = float(raw)
            except (TypeError, ValueError):
                continue
        return values

    def _observed_answer(self, summary: Any, state: Mapping[str, float], labels: Mapping[str, str]) -> str:
        if isinstance(summary, Mapping) and summary.get("largest_change_observable"):
            obs = str(summary["largest_change_observable"])
            return f"{labels.get(obs, obs)} changed most over the simulated window."
        obs = max(state, key=lambda item: abs(state[item]))
        return f"{labels.get(obs, obs)} has the largest current magnitude among displayed observables."

    def _evidence(self, summary: Any, state: Mapping[str, float], labels: Mapping[str, str]) -> str:
        if isinstance(summary, Mapping) and summary.get("peak_observable"):
            peak = str(summary["peak_observable"])
            return f"Peak observable: {labels.get(peak, peak)} = {float(summary.get('peak_value', 0.0)):.6g}."
        obs = max(state, key=lambda item: abs(state[item]))
        return f"Current value: {labels.get(obs, obs)} = {state[obs]:.6g}."

    def _timeseries(self, alias: str, source: Mapping[str, Any], labels: Mapping[str, str]) -> list[dict[str, Any]]:
        history = self._history.get(alias) or []
        if not history:
            return []
        selected = [item["id"] for item in (source.get("observables") or [])[:8]]
        if not selected:
            selected = list(history[-1][1])[:8]
        series = []
        for obs in selected:
            points = [[t, values[obs]] for t, values in history if obs in values]
            if points:
                series.append({"name": labels.get(obs, obs), "points": points})
        return series

    def _headline_items(self, alias: str, source: Mapping[str, Any], state: Mapping[str, float], labels: Mapping[str, str]) -> list[dict[str, Any]]:
        items = []
        for output in source.get("headline_outputs") or []:
            port = output["port"]
            raw = self._latest.get(f"{alias}_{port}")
            try:
                value = float(raw)
            except (TypeError, ValueError):
                source_id = output.get("source")
                if source_id not in state:
                    continue
                value = float(state[source_id])
            items.append({"label": output.get("label") or labels.get(output.get("source", ""), port), "value": value})
        return items
