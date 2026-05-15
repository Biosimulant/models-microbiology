# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Voit2003 - Trehalose Cycle."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Voit2003trehalosecyclebiomd0000000266model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000266'
    _TITLE = 'Voit2003 - Trehalose Cycle'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']
    _SPECIES_LABELS = {'X0': 'Glucose', 'X1': 'Glucose', 'X2': 'G6P', 'X3': 'G1P', 'X4': 'UDPG', 'X5': 'Glycogen', 'X6': 'T6P', 'X7': 'Trehalose'}
    _PARAMETER_INPUTS = {'heat_shock': ('heat_shock', 0.0, 'dimensionless', 'Heat-shock control parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'glucose': ('X0', 'native SBML value', 'Glucose. Maps to SBML symbol `X0`.'), 'glucose_pool_2': ('X1', 'native SBML value', 'Glucose. Maps to SBML symbol `X1`.'), 'glucose_6_phosphate': ('X2', 'native SBML value', 'G6P. Maps to SBML symbol `X2`.'), 'glucose_1_phosphate': ('X3', 'native SBML value', 'G1P. Maps to SBML symbol `X3`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000266.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Voit2003TrehaloseCycleBiomd0000000266Model = Voit2003trehalosecyclebiomd0000000266model
