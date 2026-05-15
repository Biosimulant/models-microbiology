# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Maeda2019_AmmoniumTransportAssimilation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Maeda2019ammoniumtransportassimilationmodel1901090001model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1901090001'
    _TITLE = 'Maeda2019_AmmoniumTransportAssimilation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['ADP', 'ATP', 'GLN', 'GLU', 'GS', 'GSAMP', 'GlnB', 'GlnBUMP', 'GlnBUMP2', 'GlnBUMP3', 'GlnK', 'GlnKUMP', 'GlnKUMP2', 'GlnKUMP3', 'NADP', 'NADPH', 'NHxint', 'OG', 'PPi', 'Pi', 'UMP', 'UTP']
    _SPECIES_LABELS = {'ADP': 'ADP', 'ATP': 'ATP', 'GLN': 'GLN', 'GLU': 'GLU', 'GS': 'GS', 'GSAMP': 'GSAMP', 'GlnB': 'GlnB', 'GlnBUMP': 'GlnBUMP', 'GlnBUMP2': 'GlnBUMP2', 'GlnBUMP3': 'GlnBUMP3', 'GlnK': 'GlnK', 'GlnKUMP': 'GlnKUMP', 'GlnKUMP2': 'GlnKUMP2', 'GlnKUMP3': 'GlnKUMP3', 'NADP': 'NADP', 'NADPH': 'NADPH', 'NHxint': 'NHxint', 'OG': 'OG', 'PPi': 'PPi', 'Pi': 'Pi', 'UMP': 'UMP', 'UTP': 'UTP'}
    _PARAMETER_INPUTS = {'external_ammonium': ('NH4ext', 0.00399999969144566, 'native SBML value', 'External ammonium parameter from the bundled SBML source.'), 'external_ph': ('pHext', 7.4, 'pH', 'External pH parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glutamine': ('GLN', 'native SBML value', 'GLN. Maps to SBML symbol `GLN`.'), 'glutamate': ('GLU', 'native SBML value', 'GLU. Maps to SBML symbol `GLU`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1901090001.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Maeda2019AmmoniumtransportassimilationModel1901090001Model = Maeda2019ammoniumtransportassimilationmodel1901090001model
