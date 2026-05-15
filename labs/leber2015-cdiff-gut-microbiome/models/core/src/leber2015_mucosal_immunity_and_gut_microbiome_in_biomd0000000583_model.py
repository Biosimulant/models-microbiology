# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Leber2015 - Mucosal immunity and gut microbiome interaction during C. difficile infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leber2015mucosalimmunityandgutmicrobiomeinbiomd0000000583model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000583'
    _TITLE = 'Leber2015 - Mucosal immunity and gut microbiome interaction during C. difficile infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cdiff', 'Commensal_Beneficial', 'Commensal_Dead', 'tDC_LP', 'tDC_MLN', 'Commensal_Harmful', 'N_Lum', 'E', 'E_d', 'iDC_E', 'E_i', 'M_LP', 'eDC_LP', 'M0', 'N_LP', 'Th17_LP', 'Th1_LP', 'iTreg_LP', 'eDC_MLN', 'iTreg_MLN', 'nT', 'Th17_MLN', 'Th1_MLN']
    _SPECIES_LABELS = {'Cdiff': 'Cdiff', 'Commensal_Beneficial': 'Commensal Beneficial', 'Commensal_Dead': 'Commensal Dead', 'tDC_LP': 'TDC LP', 'tDC_MLN': 'TDC MLN', 'Commensal_Harmful': 'Commensal Harmful', 'N_Lum': 'N Lum', 'E': 'E', 'E_d': 'E d', 'iDC_E': 'IDC E', 'E_i': 'E i', 'M_LP': 'M LP', 'eDC_LP': 'EDC LP', 'M0': 'M0', 'N_LP': 'N LP', 'Th17_LP': 'Th17 LP', 'Th1_LP': 'Th1 LP', 'iTreg_LP': 'ITreg LP', 'eDC_MLN': 'EDC MLN', 'iTreg_MLN': 'ITreg MLN', 'nT': 'NT', 'Th17_MLN': 'Th17 MLN', 'Th1_MLN': 'Th1 MLN'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_clostridioides_difficile': ('Cdiff', 484.0, 'native SBML value', 'Initial Clostridioides difficile state from the bundled SBML source.'), 'initial_beneficial_commensals': ('Commensal_Beneficial', 1.0, 'native SBML value', 'Initial beneficial commensal state from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'clostridioides_difficile': ('Cdiff', 'native SBML value', 'Cdiff. Maps to SBML symbol `Cdiff`.'), 'beneficial_commensals': ('Commensal_Beneficial', 'native SBML value', 'Commensal Beneficial. Maps to SBML symbol `Commensal_Beneficial`.'), 'harmful_commensals': ('Commensal_Harmful', 'native SBML value', 'Commensal Harmful. Maps to SBML symbol `Commensal_Harmful`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000583.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Leber2015MucosalImmunityAndGutMicrobiomeInBiomd0000000583Model = Leber2015mucosalimmunityandgutmicrobiomeinbiomd0000000583model
