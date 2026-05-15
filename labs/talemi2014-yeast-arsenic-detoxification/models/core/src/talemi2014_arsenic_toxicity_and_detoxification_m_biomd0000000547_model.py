# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Talemi2014 - Arsenic toxicity and detoxification mechanisms in yeast."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Talemi2014arsenictoxicityanddetoxificationmbiomd0000000547model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000547'
    _TITLE = 'Talemi2014 - Arsenic toxicity and detoxification mechanisms in yeast'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_6', 'species_5', 'species_10', 'species_9', 'species_15', 'species_11', 'species_14', 'species_4', 'species_3', 'species_1', 'species_2', 'species_7']
    _SPECIES_LABELS = {'species_6': 'AsIIIex', 'species_5': 'Ycf1', 'species_10': 'Hog1PP', 'species_9': 'Hog1', 'species_15': 'Fps1P', 'species_11': 'Fps1', 'species_14': 'Acr3', 'species_4': 'VAsGS3', 'species_3': 'AsGS3', 'species_1': 'AsIIIin', 'species_2': 'AsIIIProt', 'species_7': 'GSH'}
    _PARAMETER_INPUTS = {'arsenite_shock_level': ('parameter_6', 1000.0, 'native SBML value', 'Extracellular arsenite shock level from the bundled SBML source.'), 'arsenite_shock_start_time': ('parameter_7', 0.0, 'native SBML value', 'Extracellular arsenite shock start time from the bundled SBML source.'), 'extracellular_arsenite_initial': ('parameter_5', 100.0, 'native SBML value', 'Initial extracellular arsenite parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'extracellular_arsenite': ('species_6', 'native SBML value', 'AsIIIex. Maps to SBML symbol `species_6`.'), 'ycf1_transporter': ('species_5', 'native SBML value', 'Ycf1. Maps to SBML symbol `species_5`.'), 'phosphorylated_hog1': ('species_10', 'native SBML value', 'Hog1PP. Maps to SBML symbol `species_10`.'), 'hog1_mapk': ('species_9', 'native SBML value', 'Hog1. Maps to SBML symbol `species_9`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000547.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Talemi2014ArsenicToxicityAndDetoxificationMBiomd0000000547Model = Talemi2014arsenictoxicityanddetoxificationmbiomd0000000547model
