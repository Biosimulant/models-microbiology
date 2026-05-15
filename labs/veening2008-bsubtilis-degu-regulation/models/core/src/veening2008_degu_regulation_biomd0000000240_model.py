# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Veening2008_DegU_Regulation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Veening2008deguregulationbiomd0000000240model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000240'
    _TITLE = 'Veening2008_DegU_Regulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['AprE', 'DegU', 'DegUP', 'Dim', 'mAprE', 'mDegU']
    _SPECIES_LABELS = {'AprE': 'AprE', 'DegU': 'DegU', 'DegUP': 'DegUP', 'Dim': 'Dim', 'mAprE': 'MAprE', 'mDegU': 'MDegU'}
    _PARAMETER_INPUTS = {'maximum_degu_activation_rate': ('Imax', 0.048, 'native SBML value', 'Maximum DegU activation-rate parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {'initial_degu_response_regulator': ('DegU', 10.0, 'native SBML value', 'Initial DegU response regulator level from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'apre_extracellular_protease': ('AprE', 'native SBML value', 'AprE. Maps to SBML symbol `AprE`.'), 'degu_response_regulator': ('DegU', 'native SBML value', 'DegU. Maps to SBML symbol `DegU`.'), 'phosphorylated_degu_response_regulator': ('DegUP', 'native SBML value', 'DegUP. Maps to SBML symbol `DegUP`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000240.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Veening2008DeguRegulationBiomd0000000240Model = Veening2008deguregulationbiomd0000000240model
