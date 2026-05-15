# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for MODEL2427021978_url.xml."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Model2427021978urlxmlmodel2427021978model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2427021978'
    _TITLE = 'MODEL2427021978_url.xml'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLCi', 'ATP', 'G6P', 'ADP', 'F6P', 'F16bP', 'AMP', 'DHAP', 'GAP', 'NAD', 'BPG', 'NADH', 'P3G', 'P2G', 'PEP', 'PYR', 'AcAld', 'GLCo', 'CO2', 'EtOH', 'Glycerol', 'Glycogen', 'Trehalose', 'Succinate']
    _SPECIES_LABELS = {'GLCi': 'GLCi', 'ATP': 'ATP', 'G6P': 'G6P', 'ADP': 'ADP', 'F6P': 'F6P', 'F16bP': 'F16bP', 'AMP': 'AMP', 'DHAP': 'DHAP', 'GAP': 'GAP', 'NAD': 'NAD', 'BPG': 'BPG', 'NADH': 'NADH', 'P3G': 'P3G', 'P2G': 'P2G', 'PEP': 'PEP', 'PYR': 'PYR', 'AcAld': 'AcAld', 'GLCo': 'GLCo', 'CO2': 'CO2', 'EtOH': 'EtOH', 'Glycerol': 'Glycerol', 'Glycogen': 'Glycogen', 'Trehalose': 'Trehalose', 'Succinate': 'Succinate'}
    _PARAMETER_INPUTS = {'external_glucose': ('GLCo', 50.0, 'native SBML value', 'External glucose boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'intracellular_glucose': ('GLCi', 'native SBML value', 'GLCi. Maps to SBML symbol `GLCi`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'G6P. Maps to SBML symbol `G6P`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2427021978.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Model2427021978UrlXmlModel2427021978Model = Model2427021978urlxmlmodel2427021978model
