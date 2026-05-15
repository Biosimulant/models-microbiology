# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Salcedo-Sora2016 - Microbial folate biosynthesis and utilisation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Salcedosora2016microbialfolatebiosynthesisabiomd0000000725model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000725'
    _TITLE = 'Salcedo-Sora2016 - Microbial folate biosynthesis and utilisation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['DAHP', 'PEP', 'Pi', 'DHQ', 'EP', 'DHSK', 'SK', 'SKP', 'CVPSK', 'CM', 'Gln', 'Glu', 'ADC', 'Pyr', 'pABA', 'DHNTP', 'GTP', 'AHMDHP', 'HAD', 'PTHP', 'AHMDPP', 'DHP', 'DHF', 'THF', 'THFGlu', 'Gly', 'Ser', 'myTHFGlu', 'MTHFGlu', 'Hcy', 'Met', 'dTMP', 'dUMP', 'meTHFGlu', 'fTHFGlu', 'fmtRNA', 'mtRNA', 'COTwo', 'ADP', 'ATP', 'NADP', 'NADPH', 'AMP', 'DLp', 'SAmDLp', 'Lp', 'NAD', 'NADH', 'Ammonia', 'Formyl', 'ffTHFGlu']
    _SPECIES_LABELS = {'DAHP': 'DAHP', 'PEP': 'PEP', 'Pi': 'Pi', 'DHQ': 'DHQ', 'EP': 'EP', 'DHSK': 'DHSK', 'SK': 'SK', 'SKP': 'SKP', 'CVPSK': 'CVPSK', 'CM': 'CM', 'Gln': 'Gln', 'Glu': 'Glu', 'ADC': 'ADC', 'Pyr': 'Pyr', 'pABA': 'PABA', 'DHNTP': 'DHNTP', 'GTP': 'GTP', 'AHMDHP': 'AHMDHP', 'HAD': 'HAD', 'PTHP': 'PTHP', 'AHMDPP': 'AHMDPP', 'DHP': 'DHP', 'DHF': 'DHF', 'THF': 'THF', 'THFGlu': 'THFGlu', 'Gly': 'Gly', 'Ser': 'Ser', 'myTHFGlu': 'Model state myTHFGlu', 'MTHFGlu': 'Model state MTHFGlu', 'Hcy': 'Hcy', 'Met': 'Met', 'dTMP': 'DTMP', 'dUMP': 'DUMP', 'meTHFGlu': 'Model state meTHFGlu', 'fTHFGlu': 'FTHFGlu', 'fmtRNA': 'FmtRNA', 'mtRNA': 'MtRNA', 'COTwo': 'COTwo', 'ADP': 'ADP', 'ATP': 'ATP', 'NADP': 'NADP', 'NADPH': 'NADPH', 'AMP': 'AMP', 'DLp': 'DLp', 'SAmDLp': 'SAmDLp', 'Lp': 'Lp', 'NAD': 'NAD', 'NADH': 'NADH', 'Ammonia': 'Ammonia', 'Formyl': 'Formyl', 'ffTHFGlu': 'FfTHFGlu'}
    _PARAMETER_INPUTS = {'phosphoenolpyruvate_pool': ('PEP', 16.01031821, 'native SBML value', 'Phosphoenolpyruvate boundary species from the bundled SBML source.'), 'glutamine_pool': ('Gln', 381.0009289, 'native SBML value', 'Glutamine boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'deoxy_arabino_heptulosonate_phosphate': ('DAHP', 'native SBML value', 'DAHP. Maps to SBML symbol `DAHP`.'), 'phosphoenolpyruvate': ('PEP', 'native SBML value', 'PEP. Maps to SBML symbol `PEP`.'), 'phosphate': ('Pi', 'native SBML value', 'Pi. Maps to SBML symbol `Pi`.'), 'dehydroquinate': ('DHQ', 'native SBML value', 'DHQ. Maps to SBML symbol `DHQ`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000725.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


SalcedoSora2016MicrobialFolateBiosynthesisABiomd0000000725Model = Salcedosora2016microbialfolatebiosynthesisabiomd0000000725model
