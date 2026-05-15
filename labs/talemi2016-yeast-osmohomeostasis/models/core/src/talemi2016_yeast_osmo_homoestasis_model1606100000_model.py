# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Talemi2016 - Yeast osmo-homoestasis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Talemi2016yeastosmohomoestasismodel1606100000model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1606100000'
    _TITLE = 'Talemi2016 - Yeast osmo-homoestasis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Glyin', 'Osmin', 'Hog1', 'Hog1PP', 'Slt2', 'Slt2P', 'Glyex', 'Osmex', 'Fps1', 'Fps1P', 'Sensitizer']
    _SPECIES_LABELS = {'Glyin': 'Glyin', 'Osmin': 'Osmin', 'Hog1': 'Hog1', 'Hog1PP': 'Hog1PP', 'Slt2': 'Slt2', 'Slt2P': 'Slt2P', 'Glyex': 'Glyex', 'Osmex': 'Osmex', 'Fps1': 'Fps1', 'Fps1P': 'Fps1P', 'Sensitizer': 'Sensitizer'}
    _PARAMETER_INPUTS = {'external_osmolarity': ('Osmex', 13000000000.0, 'native SBML value', 'External osmolarity species from the bundled SBML source.'), 'hog_pathway_signal': ('HOGSignal', 0.0140453338344206, 'native SBML value', 'HOG pathway signal parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'intracellular_glycerol': ('Glyin', 'native SBML value', 'Glyin. Maps to SBML symbol `Glyin`.'), 'osmotic_signal': ('Osmin', 'native SBML value', 'Osmin. Maps to SBML symbol `Osmin`.'), 'phosphorylated_hog1_mapk': ('Hog1PP', 'native SBML value', 'Hog1PP. Maps to SBML symbol `Hog1PP`.'), 'phosphorylated_slt2_mapk': ('Slt2P', 'native SBML value', 'Slt2P. Maps to SBML symbol `Slt2P`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1606100000.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Talemi2016YeastOsmoHomoestasisModel1606100000Model = Talemi2016yeastosmohomoestasismodel1606100000model
