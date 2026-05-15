# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for MODEL2426780967_url.xml."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Model2426780967urlxmlmodel2426780967model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2426780967'
    _TITLE = 'MODEL2426780967_url.xml'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['GLCi', 'ATP', 'G6P', 'ADP', 'F6P', 'F16bP', 'AMP', 'DHAP', 'GAP', 'NAD', 'BPG', 'NADH', 'P3G', 'P2G', 'PEP', 'PYR', 'AcAld', 'GLCo', 'CO2', 'EtOH', 'Glycerol', 'Glycogen', 'Trehalose', 'Succinate', 'WGD_E']
    _SPECIES_LABELS = {'GLCi': 'GLCi', 'ATP': 'ATP', 'G6P': 'G6P', 'ADP': 'ADP', 'F6P': 'F6P', 'F16bP': 'F16bP', 'AMP': 'AMP', 'DHAP': 'DHAP', 'GAP': 'GAP', 'NAD': 'NAD', 'BPG': 'BPG', 'NADH': 'NADH', 'P3G': 'P3G', 'P2G': 'P2G', 'PEP': 'PEP', 'PYR': 'PYR', 'AcAld': 'AcAld', 'GLCo': 'GLCo', 'CO2': 'CO2', 'EtOH': 'EtOH', 'Glycerol': 'Glycerol', 'Glycogen': 'Glycogen', 'Trehalose': 'Trehalose', 'Succinate': 'Succinate', 'WGD_E': 'WGD E'}
    _PARAMETER_INPUTS = {'external_glucose': ('GLCo', 50.0, 'native SBML value', 'External glucose boundary species from the bundled SBML source.'), 'whole_genome_duplication_enzyme_scale': ('WGD_E', 1.0, 'native SBML value', 'Whole-genome-duplication enzyme scaling species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'intracellular_glucose': ('GLCi', 'native SBML value', 'GLCi. Maps to SBML symbol `GLCi`.'), 'atp': ('ATP', 'native SBML value', 'ATP. Maps to SBML symbol `ATP`.'), 'glucose_6_phosphate': ('G6P', 'native SBML value', 'G6P. Maps to SBML symbol `G6P`.'), 'adp': ('ADP', 'native SBML value', 'ADP. Maps to SBML symbol `ADP`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2426780967.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Model2426780967UrlXmlModel2426780967Model = Model2426780967urlxmlmodel2426780967model
