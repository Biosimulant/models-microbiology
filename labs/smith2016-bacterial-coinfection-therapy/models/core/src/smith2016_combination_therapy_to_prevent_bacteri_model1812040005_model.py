# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Smith2016-Combination therapy to prevent bacterial coinfection during influenza.."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smith2016combinationtherapytopreventbacterimodel1812040005model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1812040005'
    _TITLE = 'Smith2016-Combination therapy to prevent bacterial coinfection during influenza.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I1', 'I2', 'V', 'P']
    _SPECIES_LABELS = {'T': 'T', 'I1': 'I1', 'I2': 'I2', 'V': 'V', 'P': 'P'}
    _PARAMETER_INPUTS = {'transmission_rate': ('beta', 2.8e-06, 'native SBML value', 'Transmission-rate parameter beta from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {'initial_viral_load': ('V', 2.0, 'native SBML value', 'Initial viral load from the bundled SBML source.'), 'initial_target_cells': ('T', 10000000.0, 'native SBML value', 'Initial target-cell count from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'target_cells': ('T', 'native SBML value', 'T. Maps to SBML symbol `T`.'), 'infected_cells_type_1': ('I1', 'native SBML value', 'I1. Maps to SBML symbol `I1`.'), 'infected_cells_type_2': ('I2', 'native SBML value', 'I2. Maps to SBML symbol `I2`.'), 'viral_load': ('V', 'native SBML value', 'V. Maps to SBML symbol `V`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1812040005.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Smith2016CombinationTherapyToPreventBacteriModel1812040005Model = Smith2016combinationtherapytopreventbacterimodel1812040005model
