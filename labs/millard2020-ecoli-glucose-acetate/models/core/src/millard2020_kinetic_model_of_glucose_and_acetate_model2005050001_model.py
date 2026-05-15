# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Millard2020 - Kinetic model of Glucose and Acetate metabolisms in E. coli."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Millard2020kineticmodelofglucoseandacetatemodel2005050001model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL2005050001'
    _TITLE = 'Millard2020 - Kinetic model of Glucose and Acetate metabolisms in E. coli'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Glc', 'AcP', 'Ace', 'AcCoA', 'X', 'Ace_out']
    _SPECIES_LABELS = {'Glc': 'Glc', 'AcP': 'AcP', 'Ace': 'Ace', 'AcCoA': 'AcCoA', 'X': 'X', 'Ace_out': 'Ace out'}
    _PARAMETER_INPUTS = {'external_glucose': ('Glc', 20.0, 'native SBML value', 'Glucose source species from the bundled SBML source.'), 'extracellular_acetate_level': ('Ace_out', 0.1, 'native SBML value', 'Extracellular acetate source species from the bundled SBML source.'), 'dilution_rate': ('_dilution_rate', 0.0, 'native SBML value', 'Dilution-rate parameter from the bundled SBML source.'), 'feed_rate': ('_feed', 0.0, 'native SBML value', 'Feed-rate parameter from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'glucose': ('Glc', 'native SBML value', 'Glc. Maps to SBML symbol `Glc`.'), 'acetate': ('Ace', 'native SBML value', 'Ace. Maps to SBML symbol `Ace`.'), 'extracellular_acetate': ('Ace_out', 'native SBML value', 'Ace out. Maps to SBML symbol `Ace_out`.'), 'input_regulator': ('X', 'native SBML value', 'X. Maps to SBML symbol `X`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2005050001.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Millard2020KineticModelOfGlucoseAndAcetateModel2005050001Model = Millard2020kineticmodelofglucoseandacetatemodel2005050001model
