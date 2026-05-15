# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Gulbudak2019.1 - Heterogeneous viral strategies promote coexistence in virus-microbe systems (Lytic)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gulbudak20191heterogeneousviralstrategiesprbiomd0000000845model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000845'
    _TITLE = 'Gulbudak2019.1 - Heterogeneous viral strategies promote coexistence in virus-microbe systems (Lytic)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'I', 'V_L']
    _SPECIES_LABELS = {'S': 'S', 'I': 'I', 'V_L': 'V L'}
    _PARAMETER_INPUTS = {'infection_rate': ('beta', 20.0, 'native SBML value', 'Infection-rate parameter beta from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'susceptible_hosts': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'infected_hosts': ('I', 'native SBML value', 'I. Maps to SBML symbol `I`.'), 'free_lytic_virus': ('V_L', 'native SBML value', 'V L. Maps to SBML symbol `V_L`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000845.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gulbudak20191HeterogeneousViralStrategiesPrBiomd0000000845Model = Gulbudak20191heterogeneousviralstrategiesprbiomd0000000845model
