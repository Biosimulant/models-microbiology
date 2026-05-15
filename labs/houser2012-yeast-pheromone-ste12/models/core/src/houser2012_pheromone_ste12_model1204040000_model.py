# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Houser2012_pheromone_Ste12."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Houser2012pheromoneste12model1204040000model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1204040000'
    _TITLE = 'Houser2012_pheromone_Ste12'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T1', 'TS', 'TSD1', 'Ste12B', 'T1B', 'S_2', 'SD1', 'SD2', 'SD1D2', 'Dig2', 'Fus3', 'FUS1', 'Ste12', 'Dig1', 'Fus1']
    _SPECIES_LABELS = {'T1': 'T1', 'TS': 'TS', 'TSD1': 'TSD1', 'Ste12B': 'Ste12B', 'T1B': 'T1B', 'S_2': 'S 2', 'SD1': 'SD1', 'SD2': 'SD2', 'SD1D2': 'SD1D2', 'Dig2': 'Dig2', 'Fus3': 'Fus3', 'FUS1': 'FUS1', 'Ste12': 'Ste12', 'Dig1': 'Dig1', 'Fus1': 'Fus1'}
    _PARAMETER_INPUTS = {'pheromone_input_signal': ('I', 0.0, 'native SBML value', 'Pheromone input parameter I from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {'initial_dig1_level': ('Dig1', 150.5, 'native SBML value', 'Initial Dig1 level from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'bound_ste12_transcription_factor': ('Ste12B', 'native SBML value', 'Ste12B. Maps to SBML symbol `Ste12B`.'), 'pheromone_state_one': ('T1', 'native SBML value', 'T1. Maps to SBML symbol `T1`.'), 'pheromone_ste12_complex': ('TS', 'native SBML value', 'TS. Maps to SBML symbol `TS`.'), 'pheromone_ste12_dig1_complex': ('TSD1', 'native SBML value', 'TSD1. Maps to SBML symbol `TSD1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1204040000.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Houser2012PheromoneSte12Model1204040000Model = Houser2012pheromoneste12model1204040000model
