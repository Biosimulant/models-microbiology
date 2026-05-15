# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Heldt2018 - Budding yeast size control by titration of nuclear sites."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Heldt2018buddingyeastsizecontrolbytitratiomodel1803220002model(TelluriumSBMLBioModule):
    _SBML_ID = 'MODEL1803220002'
    _TITLE = 'Heldt2018 - Budding yeast size control by titration of nuclear sites'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['TM', 'GI', 'GD', 'GITM', 'GDTM', 'CLN3', 'WHI', 'WHIp', 'SBF', 'WHISBF', 'WHIn', 'WHIt', 'SBFt', 'SBFu', 'SBFp', 'CLN', 'CLB', 'CDHa', 'CDHi', 'CDCa', 'CDCi', 'TMt', 'active_SBF', 'CLN3WHISBF', 'WHIpSBF', 'CLN3t']
    _SPECIES_LABELS = {'TM': 'TM', 'GI': 'GI', 'GD': 'GD', 'GITM': 'GITM', 'GDTM': 'GDTM', 'CLN3': 'CLN3', 'WHI': 'WHI', 'WHIp': 'WHIp', 'SBF': 'SBF', 'WHISBF': 'WHISBF', 'WHIn': 'WHIn', 'WHIt': 'WHIt', 'SBFt': 'SBFt', 'SBFu': 'SBFu', 'SBFp': 'SBFp', 'CLN': 'CLN', 'CLB': 'CLB', 'CDHa': 'CDHa', 'CDHi': 'CDHi', 'CDCa': 'CDCa', 'CDCi': 'CDCi', 'TMt': 'TMt', 'active_SBF': 'Active SBF', 'CLN3WHISBF': 'CLN3WHISBF', 'WHIpSBF': 'WHIpSBF', 'CLN3t': 'CLN3t'}
    _PARAMETER_INPUTS = {'total_cln3': ('CLN3t', 0.17, 'native SBML value', 'Total CLN3 boundary species from the bundled SBML source.'), 'total_whi5': ('WHIt', 5.1, 'native SBML value', 'Total Whi5 boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'titration_module_state': ('TM', 'native SBML value', 'TM. Maps to SBML symbol `TM`.'), 'growth_initiation_state': ('GI', 'native SBML value', 'GI. Maps to SBML symbol `GI`.'), 'growth_division_state': ('GD', 'native SBML value', 'GD. Maps to SBML symbol `GD`.'), 'growth_initiation_titration_complex': ('GITM', 'native SBML value', 'GITM. Maps to SBML symbol `GITM`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1803220002.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Heldt2018BuddingYeastSizeControlByTitratioModel1803220002Model = Heldt2018buddingyeastsizecontrolbytitratiomodel1803220002model
