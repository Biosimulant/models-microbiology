# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Kuwahara2010_Fimbriation_Switch_28C."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kuwahara2010fimbriationswitch28cmodel1004010000model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1004010000'
    _TITLE = 'Kuwahara2010_Fimbriation_Switch_28C'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['FimE', 'FimB', 'Lrp', 'IHF', 'HNS', 'RNAP', 'switch', 'PfimE', 'PfimB', 's4', 'PfimB_RNAP', 'PfimE_HNS', 'Prom', 's6', 's25', 's22', 's21', 's23', 's19', 's8', 'PfimE_RNAP', 'PfimB_HNS', 's17', 's20', 's7', 's5', 's2', 's26', 's3', 's18', 's24']
    _SPECIES_LABELS = {'FimE': 'FimE', 'FimB': 'FimB', 'Lrp': 'Lrp', 'IHF': 'IHF', 'HNS': 'HNS', 'RNAP': 'RNAP', 'switch': 'Switch', 'PfimE': 'PfimE', 'PfimB': 'PfimB', 's4': 'Model state s4', 'PfimB_RNAP': 'PfimB RNAP', 'PfimE_HNS': 'PfimE HNS', 'Prom': 'Prom', 's6': 'Model state s6', 's25': 'Model state s25', 's22': 'Model state s22', 's21': 'Model state s21', 's23': 'Model state s23', 's19': 'Model state s19', 's8': 'Model state s8', 'PfimE_RNAP': 'PfimE RNAP', 'PfimB_HNS': 'PfimB HNS', 's17': 'Model state s17', 's20': 'Model state s20', 's7': 'Model state s7', 's5': 'Model state s5', 's2': 'Model state s2', 's26': 'Model state s26', 's3': 'Model state s3', 's18': 'Model state s18', 's24': 'Model state s24'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_fime_site_recombinase': ('FimE', 100.0, 'native SBML value', 'Initial FimE site-recombinase level from the bundled SBML source.'), 'initial_fimb_site_recombinase': ('FimB', 74.0, 'native SBML value', 'Initial FimB site-recombinase level from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'fime_site_recombinase': ('FimE', 'native SBML value', 'FimE. Maps to SBML symbol `FimE`.'), 'fimb_site_recombinase': ('FimB', 'native SBML value', 'FimB. Maps to SBML symbol `FimB`.'), 'leucine_responsive_regulatory_protein': ('Lrp', 'native SBML value', 'Lrp. Maps to SBML symbol `Lrp`.'), 'integration_host_factor': ('IHF', 'native SBML value', 'IHF. Maps to SBML symbol `IHF`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1004010000.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Kuwahara2010FimbriationSwitch28cModel1004010000Model = Kuwahara2010fimbriationswitch28cmodel1004010000model
