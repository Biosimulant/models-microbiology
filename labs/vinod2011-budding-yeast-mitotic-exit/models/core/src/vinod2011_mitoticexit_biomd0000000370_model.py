# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Vinod2011_MitoticExit."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vinod2011mitoticexitbiomd0000000370model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000370'
    _TITLE = 'Vinod2011_MitoticExit'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Clb2T_1', 'Clb5T_1', 'Cln_1', 'Cdc20_1', 'Cdh1_1', 'Sic1T_1', 'Trim2_1', 'Trim5_1', 'Swi5_1', 'Mcm_1', 'MBF_1', 'Pds1T_1', 'Esp1T_1', 'PoloT_1', 'Polo_1', 'Net1dep_1', 'Net1pp_1', 'RENT_1', 'RENTp_1', 'Cdc14n_1', 'Tem1_1', 'Cdc15_1', 'MEN_1', 'Clb2_2', 'Clb5_1', 'Sic1_1', 'Pds1_1', 'Esp1b_1', 'Esp1_1', 'Net1p_1', 'Net1_2', 'Cdc14c_1']
    _SPECIES_LABELS = {'Clb2T_1': 'Clb2T', 'Clb5T_1': 'Clb5T', 'Cln_1': 'Cln', 'Cdc20_1': 'Cdc20', 'Cdh1_1': 'Cdh1', 'Sic1T_1': 'Sic1T', 'Trim2_1': 'Trim2', 'Trim5_1': 'Trim5', 'Swi5_1': 'Swi5', 'Mcm_1': 'Mcm', 'MBF_1': 'MBF', 'Pds1T_1': 'Pds1T', 'Esp1T_1': 'Esp1T', 'PoloT_1': 'PoloT', 'Polo_1': 'Polo', 'Net1dep_1': 'Net1dep', 'Net1pp_1': 'Net1pp', 'RENT_1': 'RENT', 'RENTp_1': 'RENTp', 'Cdc14n_1': 'Cdc14n', 'Tem1_1': 'Tem1', 'Cdc15_1': 'Cdc15', 'MEN_1': 'MEN', 'Clb2_2': 'Clb2', 'Clb5_1': 'Clb5', 'Sic1_1': 'Sic1', 'Pds1_1': 'Pds1', 'Esp1b_1': 'Esp1b', 'Esp1_1': 'Esp1', 'Net1p_1': 'Net1p', 'Net1_2': 'Net1', 'Cdc14c_1': 'Cdc14c'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_total_clb2_cyclin': ('Clb2T_1', 0.999107, 'native SBML value', 'Initial total Clb2 cyclin from the bundled SBML source.'), 'initial_total_clb5_cyclin': ('Clb5T_1', 0.201977, 'native SBML value', 'Initial total Clb5 cyclin from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'total_clb2_cyclin': ('Clb2T_1', 'native SBML value', 'Clb2T. Maps to SBML symbol `Clb2T_1`.'), 'total_clb5_cyclin': ('Clb5T_1', 'native SBML value', 'Clb5T. Maps to SBML symbol `Clb5T_1`.'), 'cln_cyclin': ('Cln_1', 'native SBML value', 'Cln. Maps to SBML symbol `Cln_1`.'), 'cdc20_activator': ('Cdc20_1', 'native SBML value', 'Cdc20. Maps to SBML symbol `Cdc20_1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000370.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Vinod2011MitoticexitBiomd0000000370Model = Vinod2011mitoticexitbiomd0000000370model
