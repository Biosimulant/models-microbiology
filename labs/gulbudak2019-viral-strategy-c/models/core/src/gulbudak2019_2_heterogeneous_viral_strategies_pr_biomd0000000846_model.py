# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Gulbudak2019.2 - Heterogeneous viral strategies promote coexistence in virus-microbe systems (Chronic)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gulbudak20192heterogeneousviralstrategiesprbiomd0000000846model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000846'
    _TITLE = 'Gulbudak2019.2 - Heterogeneous viral strategies promote coexistence in virus-microbe systems (Chronic)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'C', 'V_C']
    _SPECIES_LABELS = {'S': 'S', 'C': 'C', 'V_C': 'V C'}
    _PARAMETER_INPUTS = {'infection_rate': ('beta', 20.0, 'native SBML value', 'Infection-rate parameter beta from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'susceptible_hosts': ('S', 'native SBML value', 'S. Maps to SBML symbol `S`.'), 'carrier_hosts': ('C', 'native SBML value', 'C. Maps to SBML symbol `C`.'), 'free_chronic_virus': ('V_C', 'native SBML value', 'V C. Maps to SBML symbol `V_C`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000846.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Gulbudak20192HeterogeneousViralStrategiesPrBiomd0000000846Model = Gulbudak20192heterogeneousviralstrategiesprbiomd0000000846model
