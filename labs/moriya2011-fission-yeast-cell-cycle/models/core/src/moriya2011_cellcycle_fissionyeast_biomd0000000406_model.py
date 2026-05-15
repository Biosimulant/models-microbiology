# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Moriya2011_CellCycle_FissionYeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Moriya2011cellcyclefissionyeastbiomd0000000406model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000406'
    _TITLE = 'Moriya2011_CellCycle_FissionYeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s4', 's9', 's46', 's47', 's48', 's49', 's50', 's51', 's52', 's55', 's56', 's57', 's60', 's61', 's63', 's64', 's65', 's66', 's67', 's70', 's71', 's72', 's73', 's74', 's75', 's76', 's77', 's78', 's79', 's80', 's81', 's82', 's83', 's84', 's85', 's88', 's89', 's90', 's91', 's92', 's93', 's94', 's130', 's137', 's149', 's153', 's157', 's161', 's166']
    _SPECIES_LABELS = {'s4': 'Vdrum', 's9': 'Vdcyc', 's46': 'Sa4 degraded', 's47': 'Srw1', 's48': 'Slp1A', 's49': 'Puc1', 's50': 'IE', 's51': 'IIE', 's52': 'Rum1+', 's55': 'Cig2+', 's56': 'Cdc13', 's57': 'Cdc13+', 's60': 'PCdc13', 's61': 'Sa161 degraded', 's63': 'Cig2p', 's64': 'Pyp3', 's65': 'ISrw1', 's66': 'ISlp1', 's67': 'Cig2', 's70': 'ICdc10', 's71': 'Cdc10', 's72': 'Mik1', 's73': 'Mik1+', 's74': 'Sa347 degraded', 's75': 'Cig1', 's76': 'Cig1+', 's77': 'Sa353 degraded', 's78': 'Clp1+', 's79': 'IWee1', 's80': 'Wee1', 's81': 'Clp1', 's82': 'ICdc25', 's83': 'Cdc25', 's84': 'Cdc18T', 's85': 'Cdc18+', 's88': 'Sa386 degraded', 's89': 'PreRC', 's90': 'PostRC', 's91': 'Repldna', 's92': 'Irepldna', 's93': 'Sa370 degraded', 's94': 'Sa44 degraded', 's130': 'Vdc18', 's137': 'Cdc13p-Rum1', 's149': 'Cig2-Rum1', 's153': 'Cig2p-Rum1', 's157': 'UDNA', 's161': 'Cdc13-Rum1', 's166': 'Rum1'}
    _PARAMETER_INPUTS = {'drum_cycle_velocity_control': ('s4', 0.0, 'native SBML value', 'Vdrum boundary control from the bundled SBML source.'), 'cell_cycle_velocity_control': ('s9', 0.0, 'native SBML value', 'Vdcyc boundary control from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'drum_cycle_velocity_state': ('s4', 'native SBML value', 'Vdrum. Maps to SBML symbol `s4`.'), 'cell_cycle_velocity_state': ('s9', 'native SBML value', 'Vdcyc. Maps to SBML symbol `s9`.'), 'degraded_sa4_state': ('s46', 'native SBML value', 'Sa4 degraded. Maps to SBML symbol `s46`.'), 'srw1_regulator': ('s47', 'native SBML value', 'Srw1. Maps to SBML symbol `s47`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000406.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Moriya2011CellcycleFissionyeastBiomd0000000406Model = Moriya2011cellcyclefissionyeastbiomd0000000406model
