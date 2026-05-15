# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Kaiser2014 - Salmonella persistence after ciprofloxacin treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kaiser2014salmonellapersistenceafterciproflobiomd0000000527model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000527'
    _TITLE = 'Kaiser2014 - Salmonella persistence after ciprofloxacin treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L']
    _SPECIES_LABELS = {'L': 'L'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_persistent_salmonella_load': ('L', 0.0, 'native SBML value', 'Initial persistent Salmonella load from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'persistent_salmonella_load': ('L', 'native SBML value', 'L. Maps to SBML symbol `L`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000527.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kaiser2014SalmonellaPersistenceAfterCiprofloBiomd0000000527Model = Kaiser2014salmonellapersistenceafterciproflobiomd0000000527model
