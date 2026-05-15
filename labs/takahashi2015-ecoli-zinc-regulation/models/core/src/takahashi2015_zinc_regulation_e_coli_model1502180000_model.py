# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Takahashi2015 - Zinc regulation E.coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Takahashi2015zincregulationecolimodel1502180000model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1502180000'
    _TITLE = 'Takahashi2015 - Zinc regulation E.coli'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P1', 'P2', 'X', 'Y', 'R', 'Z', 'Zext']
    _SPECIES_LABELS = {'P1': 'P1', 'P2': 'P2', 'X': 'X', 'Y': 'Y', 'R': 'R', 'Z': 'Z', 'Zext': 'Zext'}
    _PARAMETER_INPUTS = {'external_zinc': ('Zext', 24700.0, 'native SBML value', 'External zinc boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'extracellular_zinc': ('Zext', 'native SBML value', 'Zext. Maps to SBML symbol `Zext`.'), 'intracellular_zinc': ('Z', 'native SBML value', 'Z. Maps to SBML symbol `Z`.'), 'receptor_state': ('R', 'native SBML value', 'R. Maps to SBML symbol `R`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1502180000.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Takahashi2015ZincRegulationEColiModel1502180000Model = Takahashi2015zincregulationecolimodel1502180000model
