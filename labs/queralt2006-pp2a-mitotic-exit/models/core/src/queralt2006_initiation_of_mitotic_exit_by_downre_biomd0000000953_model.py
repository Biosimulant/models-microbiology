# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Queralt2006 - Initiation of mitotic exit by downregulation of PP2A in budding yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Queralt2006initiationofmitoticexitbydownrebiomd0000000953model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000953'
    _TITLE = 'Queralt2006 - Initiation of mitotic exit by downregulation of PP2A in budding yeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['clb2', 'cdc20', 'cdh1', 'securin_total', 'separase_total', 'securin_separase', 'net1', 'net1p', 'cdc14', 'net1cdc14', 'polo_total', 'cdk', 'pp2a', 'men', 'polo', 'tem1', 'cdc15', 'pp2a_total', 'cdh1_total', 'net1_total', 'tem1_total', 'cdc15_total', 'securin', 'separase', 'Inh', 'cdc14_total', 'Cdc14x2']
    _SPECIES_LABELS = {'clb2': 'Clb2', 'cdc20': 'Cdc20', 'cdh1': 'Cdh1', 'securin_total': 'Securin total', 'separase_total': 'Separase total', 'securin_separase': 'Securin separase', 'net1': 'Net1', 'net1p': 'Net1p', 'cdc14': 'Cdc14', 'net1cdc14': 'Net1cdc14', 'polo_total': 'Polo total', 'cdk': 'Cdk', 'pp2a': 'Pp2a', 'men': 'Men', 'polo': 'Polo', 'tem1': 'Tem1', 'cdc15': 'Cdc15', 'pp2a_total': 'Pp2a total', 'cdh1_total': 'Cdh1 total', 'net1_total': 'Net1 total', 'tem1_total': 'Tem1 total', 'cdc15_total': 'Cdc15 total', 'securin': 'Securin', 'separase': 'Separase', 'Inh': 'Inh', 'cdc14_total': 'Cdc14 total', 'Cdc14x2': 'Cdc14x2'}
    _PARAMETER_INPUTS = {'total_pp2a': ('pp2a_total', 1.0, 'native SBML value', 'Total PP2A boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'clb2_cyclin_level': ('clb2', 'native SBML value', 'Clb2. Maps to SBML symbol `clb2`.'), 'cdc20_level': ('cdc20', 'native SBML value', 'Cdc20. Maps to SBML symbol `cdc20`.'), 'cdh1_level': ('cdh1', 'native SBML value', 'Cdh1. Maps to SBML symbol `cdh1`.'), 'securin_total': ('securin_total', 'native SBML value', 'Securin total. Maps to SBML symbol `securin_total`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000953.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Queralt2006InitiationOfMitoticExitByDownreBiomd0000000953Model = Queralt2006initiationofmitoticexitbydownrebiomd0000000953model
