# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Tellurium-backed SBML wrapper for Nishio2008 - Design of the phosphotransferase system for enhanced glucose uptake in E. coli.."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nishio2008designofthephosphotransferasesystbiomd0000000571model(TelluriumSBMLBioModule):
    _SBML_ID = 'BIOMD0000000571'
    _TITLE = 'Nishio2008 - Design of the phosphotransferase system for enhanced glucose uptake in E. coli.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CRP', 'CRPsiteI_crp', 'CRPsiteII_crp', 'CRPsite_cyaA', 'CRPsite_genome', 'CRPsite_ptsGp1', 'CRPsite_ptsGp2', 'CRPsite_ptsHp0', 'CRPsite_ptsHp1', 'CRPsite_ptsIp0', 'CRPsite_ptsIp1', 'CRPsite_mlcp1', 'CRPsite_mlcp2', 'Mlc', 'Mlcsite_mlcp1', 'Mlcsite_mlcp2', 'Mlcsite_ptsGp1', 'Mlcsite_ptsGp2', 'Mlcsite_ptsHp0', 'Mlcsite_ptsIp0', 'CRP_cAMP', 'CRP_cAMP_CRPsiteI_crp', 'CRP_cAMP_CRPsiteII_crp', 'CRP_cAMP_CRPsite_cyaA', 'CRP_cAMP_CRPsite_genome', 'CRP_cAMP_CRPsite_ptsGp1', 'CRP_cAMP_CRPsite_ptsGp2', 'CRP_cAMP_CRPsite_ptsHp0', 'CRP_cAMP_CRPsite_ptsHp1', 'CRP_cAMP_CRPsite_ptsIp0', 'CRP_cAMP_CRPsite_ptsIp1', 'CRP_cAMP_CRPsite_mlcp1', 'CRP_cAMP_CRPsite_mlcp2', 'Mlc_Mlcsite_ptsGp1', 'Mlc_Mlcsite_ptsGp2', 'Mlc_Mlcsite_ptsIp0', 'Mlc_Mlcsite_ptsHp0', 'Mlc_Mlcsite_mlcp1', 'Mlc_Mlcsite_mlcp2', 'IICB', 'IICB_Mlc', 'CYA', 'IIA_P', 'IIA_P_CYA', 'mRNA_cyaA', 'mRNA_crp', 'mRNA_ptsG', 'mRNA_ptsH', 'mRNA_ptsI', 'mRNA_crr', 'mRNA_mlc', 'IICB_P', 'IIA', 'HPr_P', 'HPr', 'EI_P', 'EI', 'cAMP', 'cyaA', 'cyaA_basal', 'crp', 'crp_basal', 'ptsGp1', 'ptsGp2', 'ptsHp0', 'ptsHp1', 'ptsIp0', 'ptsIp1', 'crr', 'mlcp1', 'mlcp2', 'Pyr', 'PEP', 'Glc6P', 'Glucose', 'ATP']
    _SPECIES_LABELS = {'CRP': 'CRP', 'CRPsiteI_crp': 'CRPsiteI crp', 'CRPsiteII_crp': 'CRPsiteII crp', 'CRPsite_cyaA': 'CRPsite cyaA', 'CRPsite_genome': 'CRPsite genome', 'CRPsite_ptsGp1': 'CRPsite ptsGp1', 'CRPsite_ptsGp2': 'CRPsite ptsGp2', 'CRPsite_ptsHp0': 'CRPsite ptsHp0', 'CRPsite_ptsHp1': 'CRPsite ptsHp1', 'CRPsite_ptsIp0': 'CRPsite ptsIp0', 'CRPsite_ptsIp1': 'CRPsite ptsIp1', 'CRPsite_mlcp1': 'CRPsite mlcp1', 'CRPsite_mlcp2': 'CRPsite mlcp2', 'Mlc': 'Mlc', 'Mlcsite_mlcp1': 'Mlcsite mlcp1', 'Mlcsite_mlcp2': 'Mlcsite mlcp2', 'Mlcsite_ptsGp1': 'Mlcsite ptsGp1', 'Mlcsite_ptsGp2': 'Mlcsite ptsGp2', 'Mlcsite_ptsHp0': 'Mlcsite ptsHp0', 'Mlcsite_ptsIp0': 'Mlcsite ptsIp0', 'CRP_cAMP': 'CRP cAMP', 'CRP_cAMP_CRPsiteI_crp': 'CRP cAMP CRPsiteI crp', 'CRP_cAMP_CRPsiteII_crp': 'CRP cAMP CRPsiteII crp', 'CRP_cAMP_CRPsite_cyaA': 'CRP cAMP CRPsite cyaA', 'CRP_cAMP_CRPsite_genome': 'CRP cAMP CRPsite genome', 'CRP_cAMP_CRPsite_ptsGp1': 'CRP cAMP CRPsite ptsGp1', 'CRP_cAMP_CRPsite_ptsGp2': 'CRP cAMP CRPsite ptsGp2', 'CRP_cAMP_CRPsite_ptsHp0': 'CRP cAMP CRPsite ptsHp0', 'CRP_cAMP_CRPsite_ptsHp1': 'CRP cAMP CRPsite ptsHp1', 'CRP_cAMP_CRPsite_ptsIp0': 'CRP cAMP CRPsite ptsIp0', 'CRP_cAMP_CRPsite_ptsIp1': 'CRP cAMP CRPsite ptsIp1', 'CRP_cAMP_CRPsite_mlcp1': 'CRP cAMP CRPsite mlcp1', 'CRP_cAMP_CRPsite_mlcp2': 'CRP cAMP CRPsite mlcp2', 'Mlc_Mlcsite_ptsGp1': 'Mlc Mlcsite ptsGp1', 'Mlc_Mlcsite_ptsGp2': 'Mlc Mlcsite ptsGp2', 'Mlc_Mlcsite_ptsIp0': 'Mlc Mlcsite ptsIp0', 'Mlc_Mlcsite_ptsHp0': 'Mlc Mlcsite ptsHp0', 'Mlc_Mlcsite_mlcp1': 'Mlc Mlcsite mlcp1', 'Mlc_Mlcsite_mlcp2': 'Mlc Mlcsite mlcp2', 'IICB': 'IICB', 'IICB_Mlc': 'IICB Mlc', 'CYA': 'CYA', 'IIA_P': 'IIA P', 'IIA_P_CYA': 'IIA P CYA', 'mRNA_cyaA': 'MRNA cyaA', 'mRNA_crp': 'MRNA crp', 'mRNA_ptsG': 'MRNA ptsG', 'mRNA_ptsH': 'MRNA ptsH', 'mRNA_ptsI': 'MRNA ptsI', 'mRNA_crr': 'MRNA crr', 'mRNA_mlc': 'MRNA mlc', 'IICB_P': 'IICB P', 'IIA': 'IIA', 'HPr_P': 'HPr P', 'HPr': 'HPr', 'EI_P': 'EI P', 'EI': 'EI', 'cAMP': 'CAMP', 'cyaA': 'CyaA', 'cyaA_basal': 'CyaA basal', 'crp': 'Crp', 'crp_basal': 'Crp basal', 'ptsGp1': 'PtsGp1', 'ptsGp2': 'PtsGp2', 'ptsHp0': 'PtsHp0', 'ptsHp1': 'PtsHp1', 'ptsIp0': 'PtsIp0', 'ptsIp1': 'PtsIp1', 'crr': 'Crr', 'mlcp1': 'Mlcp1', 'mlcp2': 'Mlcp2', 'Pyr': 'Pyr', 'PEP': 'PEP', 'Glc6P': 'Glc6P', 'Glucose': 'Glucose', 'ATP': 'ATP'}
    _PARAMETER_INPUTS = {'glucose_concentration': ('Glucose', 0.2, 'native SBML value', 'Glucose boundary species from the bundled SBML source.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'camp_receptor_protein': ('CRP', 'native SBML value', 'CRP. Maps to SBML symbol `CRP`.'), 'camp_receptor_protein_bound_site_one': ('CRPsiteI_crp', 'native SBML value', 'CRPsiteI crp. Maps to SBML symbol `CRPsiteI_crp`.'), 'camp_receptor_protein_bound_site_two': ('CRPsiteII_crp', 'native SBML value', 'CRPsiteII crp. Maps to SBML symbol `CRPsiteII_crp`.'), 'camp_receptor_protein_bound_cyaa_site': ('CRPsite_cyaA', 'native SBML value', 'CRPsite cyaA. Maps to SBML symbol `CRPsite_cyaA`.')}
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000571.xml', integration_step: float = 1.0) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)


Nishio2008DesignOfThePhosphotransferaseSystBiomd0000000571Model = Nishio2008designofthephosphotransferasesystbiomd0000000571model
