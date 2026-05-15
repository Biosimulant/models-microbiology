# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Shaw2019 - Digital biosensor model from Yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shaw2019digitalbiosensormodelfromyeastmodel1901300002model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1901300002'
    _TITLE = 'Shaw2019 - Digital biosensor model from Yeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R1', 'Rstar1', 'Goff1', 'Gon1', 'Effector1', 'Gon1Effector1', 'z11', 'z21', 'preafactor', 'afactor', 'R2', 'Rstar2', 'Goff2', 'Gon2', 'Effector2', 'Gon2Effector2', 'z12', 'z22', 'preGFP', 'z32', 'L', 'Bar1', 'inactiveBar1', 'GFP']
    _SPECIES_LABELS = {'R1': 'R1', 'Rstar1': 'Rstar1', 'Goff1': 'Goff1', 'Gon1': 'Gon1', 'Effector1': 'Effector1', 'Gon1Effector1': 'Gon1Effector1', 'z11': 'Z11', 'z21': 'Z21', 'preafactor': 'Preafactor', 'afactor': 'Afactor', 'R2': 'R2', 'Rstar2': 'Rstar2', 'Goff2': 'Goff2', 'Gon2': 'Gon2', 'Effector2': 'Effector2', 'Gon2Effector2': 'Gon2Effector2', 'z12': 'Z12', 'z22': 'Z22', 'preGFP': 'PreGFP', 'z32': 'Z32', 'L': 'L', 'Bar1': 'Bar1', 'inactiveBar1': 'InactiveBar1', 'GFP': 'GFP'}
    _PARAMETER_INPUTS = {'ligand_level': ('L', 0.0, 'native SBML value', 'Ligand boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'receptor_state_1': ('R1', 'native SBML value', 'R1. Maps to SBML symbol `R1`.'), 'active_receptor_state_1': ('Rstar1', 'native SBML value', 'Rstar1. Maps to SBML symbol `Rstar1`.'), 'inactive_gprotein_state_1': ('Goff1', 'native SBML value', 'Goff1. Maps to SBML symbol `Goff1`.'), 'active_gprotein_state_1': ('Gon1', 'native SBML value', 'Gon1. Maps to SBML symbol `Gon1`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1901300002.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Shaw2019DigitalBiosensorModelFromYeastModel1901300002Model = Shaw2019digitalbiosensormodelfromyeastmodel1901300002model
