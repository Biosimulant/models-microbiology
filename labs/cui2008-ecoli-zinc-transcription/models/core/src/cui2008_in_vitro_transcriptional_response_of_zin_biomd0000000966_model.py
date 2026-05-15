# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Cui2008 - in vitro transcriptional response of zinc homeostasis system in Escherichia coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cui2008invitrotranscriptionalresponseofzinbiomd0000000966model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000966'
    _TITLE = 'Cui2008 - in vitro transcriptional response of zinc homeostasis system in Escherichia coli'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Py', 'Py1', 'Dw', 'Rw', 'Qw1', 'Qw2', 'Zn_2']
    _SPECIES_LABELS = {'Py': 'Py', 'Py1': 'Py1', 'Dw': 'Dw', 'Rw': 'Rw', 'Qw1': 'Qw1', 'Qw2': 'Qw2', 'Zn_2': 'Zn^2'}
    _PARAMETER_INPUTS = {'zinc_concentration': ('Zn', 1e-05, 'native SBML value', 'Zinc concentration parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'zinc_complex': ('Zn_2', 'native SBML value', 'Zn^2. Maps to SBML symbol `Zn_2`.'), 'zinc_promoter_state': ('Dw', 'native SBML value', 'Dw. Maps to SBML symbol `Dw`.'), 'zinc_transcript_state': ('Rw', 'native SBML value', 'Rw. Maps to SBML symbol `Rw`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000966.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Cui2008InVitroTranscriptionalResponseOfZinBiomd0000000966Model = Cui2008invitrotranscriptionalresponseofzinbiomd0000000966model
