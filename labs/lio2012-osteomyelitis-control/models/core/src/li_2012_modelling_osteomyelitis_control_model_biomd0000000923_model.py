# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Liò2012_Modelling osteomyelitis_Control Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Li2012modellingosteomyelitiscontrolmodelbiomd0000000923model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000923'
    _TITLE = 'Liò2012_Modelling osteomyelitis_Control Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Bone_Density__z', 'Osteoblasts__O_b', 'Osteoclasts__O_c', 'B']
    _SPECIES_LABELS = {'Bone_Density__z': 'Bone Density (z)', 'Osteoblasts__O_b': 'Osteoblasts (O b)', 'Osteoclasts__O_c': 'Osteoclasts (O c)', 'B': 'B'}
    _PARAMETER_INPUTS = {'treatment_start_time': ('t_treat', 200.0, 'native SBML value', 'Treatment start time parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {'initial_bacterial_burden': ('B', 1.0, 'native SBML value', 'Initial bacterial burden from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'bacterial_burden': ('B', 'native SBML value', 'B. Maps to SBML symbol `B`.'), 'bone_density': ('Bone_Density__z', 'native SBML value', 'Bone Density (z). Maps to SBML symbol `Bone_Density__z`.'), 'osteoblasts': ('Osteoblasts__O_b', 'native SBML value', 'Osteoblasts (O b). Maps to SBML symbol `Osteoblasts__O_b`.'), 'osteoclasts': ('Osteoclasts__O_c', 'native SBML value', 'Osteoclasts (O c). Maps to SBML symbol `Osteoclasts__O_c`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000923.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Li2012ModellingOsteomyelitisControlModelBiomd0000000923Model = Li2012modellingosteomyelitiscontrolmodelbiomd0000000923model
