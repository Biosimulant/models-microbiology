# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Shen-Orr2002_Single_Input_Module."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shenorr2002singleinputmodulebiomd0000000317model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000317'
    _TITLE = 'Shen-Orr2002_Single_Input_Module'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X', 'Z1', 'Z2', 'Z3']
    _SPECIES_LABELS = {'X': 'X', 'Z1': 'Z1', 'Z2': 'Z2', 'Z3': 'Z3'}
    _PARAMETER_INPUTS = {'input_regulator_level': ('X', 0.0, 'native SBML value', 'Input regulator boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'input_regulator': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.'), 'target_gene_1': ('Z1', 'native SBML value', 'Z1. Maps to SBML symbol `Z1`.'), 'target_gene_2': ('Z2', 'native SBML value', 'Z2. Maps to SBML symbol `Z2`.'), 'target_gene_3': ('Z3', 'native SBML value', 'Z3. Maps to SBML symbol `Z3`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000317.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


ShenOrr2002SingleInputModuleBiomd0000000317Model = Shenorr2002singleinputmodulebiomd0000000317model
