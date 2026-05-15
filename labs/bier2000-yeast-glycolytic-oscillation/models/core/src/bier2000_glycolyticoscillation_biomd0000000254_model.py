# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Bier2000_GlycolyticOscillation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bier2000glycolyticoscillationbiomd0000000254model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000254'
    _TITLE = 'Bier2000_GlycolyticOscillation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G1', 'T1', 'G2', 'T2']
    _SPECIES_LABELS = {'G1': 'Glucose 1', 'T1': 'ATP 1', 'G2': 'Glucose 2', 'T2': 'ATP 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_glucose_pool_1': ('G1', 6.6, 'native SBML value', 'Initial value for the SBML Glucose_1 pool.'), 'initial_glucose_pool_2': ('G2', 10.3, 'native SBML value', 'Initial value for the SBML Glucose_2 pool.')}
    _HEADLINE_OUTPUTS = {'glucose_pool_1': ('G1', 'native SBML value', 'Glucose 1. Maps to SBML symbol `G1`.'), 'atp_pool_1': ('T1', 'native SBML value', 'ATP 1. Maps to SBML symbol `T1`.'), 'glucose_pool_2': ('G2', 'native SBML value', 'Glucose 2. Maps to SBML symbol `G2`.'), 'atp_pool_2': ('T2', 'native SBML value', 'ATP 2. Maps to SBML symbol `T2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000254.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bier2000GlycolyticoscillationBiomd0000000254Model = Bier2000glycolyticoscillationbiomd0000000254model
