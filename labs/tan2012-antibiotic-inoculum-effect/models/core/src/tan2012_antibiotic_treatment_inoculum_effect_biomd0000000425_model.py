# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Tan2012 - Antibiotic Treatment, Inoculum Effect."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tan2012antibiotictreatmentinoculumeffectbiomd0000000425model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000425'
    _TITLE = 'Tan2012 - Antibiotic Treatment, Inoculum Effect'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['c']
    _SPECIES_LABELS = {'c': 'Ribosome concentration'}
    _PARAMETER_INPUTS = {'antibiotic_killing_rate': ('kd', 1.0, 'native SBML value', 'Antibiotic killing-rate parameter kd from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {'initial_ribosome_concentration': ('c', 1.0, 'native SBML value', 'Initial ribosome concentration from the bundled SBML source.')}
    _HEADLINE_OUTPUTS = {'ribosome_concentration': ('c', 'native SBML value', 'Ribosome concentration. Maps to SBML symbol `c`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000425.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Tan2012AntibioticTreatmentInoculumEffectBiomd0000000425Model = Tan2012antibiotictreatmentinoculumeffectbiomd0000000425model
