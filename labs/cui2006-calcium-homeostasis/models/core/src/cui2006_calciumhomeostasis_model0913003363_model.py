# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Cui2006_CalciumHomeostasis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cui2006calciumhomeostasismodel0913003363model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL0913003363'
    _TITLE = 'Cui2006_CalciumHomeostasis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rate_rule'
    _OBSERVABLES = ['m', 'z', 'h', 'x']
    _SPECIES_LABELS = {'m': 'M', 'z': 'Z', 'h': 'H', 'x': 'X'}
    _PARAMETER_INPUTS = {'external_calcium': ('Caex', 1.0, 'native SBML value', 'External calcium parameter from the bundled SBML source.'), 'total_calmodulin': ('CaMtotal', 25.0, 'native SBML value', 'Total calmodulin parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'calcium_homeostasis_variable_one': ('m', 'native SBML value', 'M. Maps to SBML symbol `m`.'), 'calcium_homeostasis_variable_two': ('z', 'native SBML value', 'Z. Maps to SBML symbol `z`.'), 'calcium_homeostasis_variable_three': ('h', 'native SBML value', 'H. Maps to SBML symbol `h`.'), 'calcium_homeostasis_variable_four': ('x', 'native SBML value', 'X. Maps to SBML symbol `x`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL0913003363.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Cui2006CalciumhomeostasisModel0913003363Model = Cui2006calciumhomeostasismodel0913003363model
