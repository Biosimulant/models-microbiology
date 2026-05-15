# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Bruggeman2005_AmmoniumAssimilation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bruggeman2005ammoniumassimilationbiomd0000000217model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000217'
    _TITLE = 'Bruggeman2005_AmmoniumAssimilation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['PII', 'UTP', 'PIIUMP', 'PPi', 'GLN', 'PIIUMP2', 'PIIUMP3', 'UMP', 'GS', 'AMP', 'NH4', 'KG', 'NADPH', 'GLU', 'NADP', 'AZGLU', 'ATP', 'ADP', 'AZglu', 'AZGLN', 'AZgln', 'P_i']
    _SPECIES_LABELS = {'PII': 'PII', 'UTP': 'UTP', 'PIIUMP': 'PIIUMP', 'PPi': 'PPi', 'GLN': 'GLN', 'PIIUMP2': 'PIIUMP2', 'PIIUMP3': 'PIIUMP3', 'UMP': 'UMP', 'GS': 'GS', 'AMP': 'AMP', 'NH4': 'NH4', 'KG': 'KG', 'NADPH': 'NADPH', 'GLU': 'GLU', 'NADP': 'NADP', 'AZGLU': 'AZGLU', 'ATP': 'ATP', 'ADP': 'ADP', 'AZglu': 'AZglu', 'AZGLN': 'AZGLN', 'AZgln': 'AZgln', 'P_i': 'P i'}
    _PARAMETER_INPUTS = {'external_ammonium': ('NH4', 0.05, 'native SBML value', 'Ammonium boundary species from the bundled SBML source.'), 'alpha_ketoglutarate_pool': ('KG', 0.2, 'native SBML value', 'Alpha-ketoglutarate boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'pii_regulatory_protein': ('PII', 'native SBML value', 'PII. Maps to SBML symbol `PII`.'), 'uridine_triphosphate': ('UTP', 'native SBML value', 'UTP. Maps to SBML symbol `UTP`.'), 'uridylylated_pii_protein': ('PIIUMP', 'native SBML value', 'PIIUMP. Maps to SBML symbol `PIIUMP`.'), 'inorganic_pyrophosphate': ('PPi', 'native SBML value', 'PPi. Maps to SBML symbol `PPi`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000217.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Bruggeman2005AmmoniumassimilationBiomd0000000217Model = Bruggeman2005ammoniumassimilationbiomd0000000217model
