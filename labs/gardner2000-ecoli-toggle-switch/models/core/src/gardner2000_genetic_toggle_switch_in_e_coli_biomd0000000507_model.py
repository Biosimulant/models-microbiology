# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Gardner2000 - genetic toggle switch in E.coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gardner2000genetictoggleswitchinecolibiomd0000000507model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000507'
    _TITLE = 'Gardner2000 - genetic toggle switch in E.coli'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3']
    _SPECIES_LABELS = {'species_1': 'U', 'species_2': 'V', 'species_3': 'IPTG'}
    _PARAMETER_INPUTS = {'iptg_inducer_level': ('species_3', 0.0, 'native SBML value', 'IPTG inducer species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'iptg_inducer': ('species_3', 'native SBML value', 'IPTG. Maps to SBML symbol `species_3`.'), 'first_toggle_repressor': ('species_1', 'native SBML value', 'U. Maps to SBML symbol `species_1`.'), 'second_toggle_repressor': ('species_2', 'native SBML value', 'V. Maps to SBML symbol `species_2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000507.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gardner2000GeneticToggleSwitchInEColiBiomd0000000507Model = Gardner2000genetictoggleswitchinecolibiomd0000000507model
