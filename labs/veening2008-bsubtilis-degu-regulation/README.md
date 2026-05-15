# Veening2008 DegU Regulation Lab

Curated microbiology lab for Veening2008_DegU_Regulation. The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **Which DegU regulation state changes most over the simulated window?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: microbiology model dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- Maximum DegU Activation Rate (Imax)
- Initial DegU Response Regulator (DegU)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- AprE (AprE)
- DegU (DegU)
- DegUP (DegUP)

## Model Wiring

- `veening2008_bsubtilis_degu_regulation` uses `models/core`
- `visualisation` uses `models/visualisation`

- `veening2008_bsubtilis_degu_regulation.state` -> `visualisation.veening2008_bsubtilis_degu_regulation_state`
- `veening2008_bsubtilis_degu_regulation.summary` -> `visualisation.veening2008_bsubtilis_degu_regulation_summary`
- `veening2008_bsubtilis_degu_regulation.species_labels` -> `visualisation.veening2008_bsubtilis_degu_regulation_species_labels`
- `veening2008_bsubtilis_degu_regulation.apre_extracellular_protease` -> `visualisation.veening2008_bsubtilis_degu_regulation_apre_extracellular_protease`
- `veening2008_bsubtilis_degu_regulation.degu_response_regulator` -> `visualisation.veening2008_bsubtilis_degu_regulation_degu_response_regulator`
- `veening2008_bsubtilis_degu_regulation.phosphorylated_degu_response_regulator` -> `visualisation.veening2008_bsubtilis_degu_regulation_phosphorylated_degu_response_regulator`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: Which DegU regulation state changes most over the simulated window?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows AprE, DegU, DegUP through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:BIOMD0000000240
- Upstream URL: https://www.ebi.ac.uk/biomodels/BIOMD0000000240
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
