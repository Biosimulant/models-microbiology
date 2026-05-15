# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Shaw 2018 - Yeast GPCR Ternary Complex Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Shaw2018yeastgpcrternarycomplexmodelmodel1901300001model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1901300001'
    _TITLE = 'Shaw 2018 - Yeast GPCR Ternary Complex Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R', 'LR', 'Rstar', 'LRstar', 'RG', 'LRG', 'RstarG', 'LRstarG', 'G', 'aGDP', 'bg', 'aGTP', 'bgstar', 'Ste5', 'bgstarSte5', 'bgSte5', 'L', 'observable']
    _SPECIES_LABELS = {'R': 'R', 'LR': 'LR', 'Rstar': 'Rstar', 'LRstar': 'LRstar', 'RG': 'RG', 'LRG': 'LRG', 'RstarG': 'RstarG', 'LRstarG': 'LRstarG', 'G': 'G', 'aGDP': 'AGDP', 'bg': 'Bg', 'aGTP': 'AGTP', 'bgstar': 'Bgstar', 'Ste5': 'Ste5', 'bgstarSte5': 'BgstarSte5', 'bgSte5': 'BgSte5', 'L': 'L', 'observable': 'Observable'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_ligand_level': ('L', 0.0001, 'native SBML value', 'Initial ligand level from the bundled SBML source.'), 'initial_receptor_level': ('R', 4.15e-10, 'native SBML value', 'Initial receptor level from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'receptor_state': ('R', 'native SBML value', 'R. Maps to SBML symbol `R`.'), 'ligand_bound_receptor': ('LR', 'native SBML value', 'LR. Maps to SBML symbol `LR`.'), 'active_receptor': ('Rstar', 'native SBML value', 'Rstar. Maps to SBML symbol `Rstar`.'), 'active_ligand_bound_receptor': ('LRstar', 'native SBML value', 'LRstar. Maps to SBML symbol `LRstar`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1901300001.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Shaw2018YeastGpcrTernaryComplexModelModel1901300001Model = Shaw2018yeastgpcrternarycomplexmodelmodel1901300001model
