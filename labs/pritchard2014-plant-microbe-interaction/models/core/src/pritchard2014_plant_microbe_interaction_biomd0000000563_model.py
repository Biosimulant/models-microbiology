# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Pritchard2014 - plant-microbe interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Pritchard2014plantmicrobeinteractionbiomd0000000563model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000563'
    _TITLE = 'Pritchard2014 - plant-microbe interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PAMP', 'R', 'R_0', 'E_int', 'Callose', 'Path', 'Path_bulk', 'PRR', 'PRR_0', 'E']
    _SPECIES_LABELS = {'PAMP': 'PAMP', 'R': 'R', 'R_0': 'R*', 'E_int': 'E int', 'Callose': 'Callose', 'Path': 'Path', 'Path_bulk': 'Path bulk', 'PRR': 'PRR*', 'PRR_0': 'PRR', 'E': 'E'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_pamp_signal': ('PAMP', 0.0, 'native SBML value', 'Initial PAMP signal from the bundled SBML source.'), 'initial_pathogen_load': ('Path', 0.0, 'native SBML value', 'Initial pathogen load from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'pamp_signal': ('PAMP', 'native SBML value', 'PAMP. Maps to SBML symbol `PAMP`.'), 'receptor_state': ('R', 'native SBML value', 'R. Maps to SBML symbol `R`.'), 'callose': ('Callose', 'native SBML value', 'Callose. Maps to SBML symbol `Callose`.'), 'pathogen_load': ('Path', 'native SBML value', 'Path. Maps to SBML symbol `Path`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000563.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Pritchard2014PlantMicrobeInteractionBiomd0000000563Model = Pritchard2014plantmicrobeinteractionbiomd0000000563model
