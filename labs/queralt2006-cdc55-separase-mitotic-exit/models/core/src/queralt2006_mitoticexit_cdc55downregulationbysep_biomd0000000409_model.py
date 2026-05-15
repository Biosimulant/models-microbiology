# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Queralt2006_MitoticExit_Cdc55DownregulationBySeparase."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Queralt2006mitoticexitcdc55downregulationbysepbiomd0000000409model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000409'
    _TITLE = 'Queralt2006_MitoticExit_Cdc55DownregulationBySeparase'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['AA', 'Clb2', 'degr', 'Cdc20', 'Cdh1', 'Cdh1_i', 'securinT', 'securin', 'separaseT', 'separase', 'securinseparase', 'Net1', 'Net1Cdc14', 'PoloT', 'Polo', 'Polo_i', 'Tem1', 'Tem1_i', 'Cdc15', 'Cdc15_i', 'MEN', 'PP2A', 'Net1P', 'Cdc14']
    _SPECIES_LABELS = {'AA': 'AA', 'Clb2': 'Clb2', 'degr': 'Degr', 'Cdc20': 'Cdc20', 'Cdh1': 'Cdh1', 'Cdh1_i': 'Inactive Cdh1', 'securinT': 'SecurinT', 'securin': 'Securin', 'separaseT': 'SeparaseT', 'separase': 'Separase', 'securinseparase': 'Securin:separase', 'Net1': 'Net1', 'Net1Cdc14': 'Net1Cdc14', 'PoloT': 'PoloT', 'Polo': 'Polo', 'Polo_i': 'Inactive Polo', 'Tem1': 'Tem1', 'Tem1_i': 'Inactive Tem1', 'Cdc15': 'Cdc15', 'Cdc15_i': 'Inactive Cdc15', 'MEN': 'MEN', 'PP2A': 'PP2A', 'Net1P': 'Net1P', 'Cdc14': 'Cdc14'}
    _PARAMETER_INPUTS = {'amino_acid_pool_level': ('AA', 1.0, 'native SBML value', 'Amino-acid pool boundary species from the bundled SBML source.'), 'degradation_signal_level': ('degr', 1.0, 'native SBML value', 'Degradation-signal boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'amino_acid_pool': ('AA', 'native SBML value', 'AA. Maps to SBML symbol `AA`.'), 'clb2_cyclin_level': ('Clb2', 'native SBML value', 'Clb2. Maps to SBML symbol `Clb2`.'), 'degradation_signal': ('degr', 'native SBML value', 'Degr. Maps to SBML symbol `degr`.'), 'cdc20_level': ('Cdc20', 'native SBML value', 'Cdc20. Maps to SBML symbol `Cdc20`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000409.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Queralt2006MitoticexitCdc55downregulationbysepBiomd0000000409Model = Queralt2006mitoticexitcdc55downregulationbysepbiomd0000000409model
