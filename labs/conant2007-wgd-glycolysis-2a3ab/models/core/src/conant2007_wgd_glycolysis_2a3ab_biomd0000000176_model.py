# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Conant2007_WGD_glycolysis_2A3AB."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Conant2007wgdglycolysis2a3abbiomd0000000176model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000176'
    _TITLE = 'Conant2007_WGD_glycolysis_2A3AB'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLCi', 'ATP', 'G6P', 'ADP', 'F6P', 'F16bP', 'F26bP', 'AMP', 'DHAP', 'GAP', 'NAD', 'BPG', 'NADH', 'P3G', 'P2G', 'PEP', 'PYR', 'AcAld', 'GLCo', 'CO2', 'EtOH', 'Glycerol', 'Glycogen', 'Trehalose', 'Succinate']
    _SPECIES_LABELS = {'GLCi': 'GLCi', 'ATP': 'ATP', 'G6P': 'G6P', 'ADP': 'ADP', 'F6P': 'F6P', 'F16bP': 'F16bP', 'F26bP': 'Fru2,6-P2', 'AMP': 'AMP', 'DHAP': 'DHAP', 'GAP': 'GAP', 'NAD': 'NAD', 'BPG': 'BPG', 'NADH': 'NADH', 'P3G': 'P3G', 'P2G': 'P2G', 'PEP': 'PEP', 'PYR': 'PYR', 'AcAld': 'AcAld', 'GLCo': 'GLCo', 'CO2': 'CO2', 'EtOH': 'EtOH', 'Glycerol': 'Glycerol', 'Glycogen': 'Glycogen', 'Trehalose': 'Trehalose', 'Succinate': 'Succinate'}
    _PARAMETER_INPUTS = {'external_glucose': ('GLCo', 50.0, 'native SBML value', 'External glucose boundary species from the bundled SBML source.'), 'fructose_26_bisphosphate_pool': ('F26bP', 0.02, 'native SBML value', 'Fructose 2,6-bisphosphate boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'intracellular_glucose': ('GLCi', 'native SBML value', 'GLCi. Maps to SBML symbol `GLCi`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'G6P. Maps to SBML symbol `G6P`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000176.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Conant2007WgdGlycolysis2a3abBiomd0000000176Model = Conant2007wgdglycolysis2a3abbiomd0000000176model
