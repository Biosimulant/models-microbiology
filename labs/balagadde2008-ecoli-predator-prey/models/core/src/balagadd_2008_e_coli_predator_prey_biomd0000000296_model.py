# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Balagaddé2008_E_coli_Predator_Prey."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Balagadd2008ecolipredatorpreybiomd0000000296model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000296'
    _TITLE = 'Balagaddé2008_E_coli_Predator_Prey'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IPTG', 'C1', 'C2', 'A1', 'A2', 'sink', 'source']
    _SPECIES_LABELS = {'IPTG': 'IPTG', 'C1': 'C1', 'C2': 'C2', 'A1': 'A1', 'A2': 'A2', 'sink': 'Sink', 'source': 'Source'}
    _PARAMETER_INPUTS = {'iptg_inducer_level': ('IPTG', 5.0, 'native SBML value', 'IPTG boundary species level from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'cell_population_1': ('C1', 'native SBML value', 'C1. Maps to SBML symbol `C1`.'), 'cell_population_2': ('C2', 'native SBML value', 'C2. Maps to SBML symbol `C2`.'), 'quorum_signal_1': ('A1', 'native SBML value', 'A1. Maps to SBML symbol `A1`.'), 'quorum_signal_2': ('A2', 'native SBML value', 'A2. Maps to SBML symbol `A2`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000296.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Balagadd2008EColiPredatorPreyBiomd0000000296Model = Balagadd2008ecolipredatorpreybiomd0000000296model
