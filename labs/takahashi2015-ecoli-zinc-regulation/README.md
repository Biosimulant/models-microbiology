# Takahashi2015 - Zinc regulation E.coli Lab

Curated microbiology lab for Takahashi2015 - Zinc regulation E.coli. The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **How does the zinc regulation system respond across its tracked molecular states?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: microbial stress response dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- External Zinc (Zext)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- Zext (Zext)
- Z (Z)
- R (R)

## Model Wiring

- `takahashi2015_ecoli_zinc_regulation` uses `models/core`
- `visualisation` uses `models/visualisation`

- `takahashi2015_ecoli_zinc_regulation.state` -> `visualisation.takahashi2015_ecoli_zinc_regulation_state`
- `takahashi2015_ecoli_zinc_regulation.summary` -> `visualisation.takahashi2015_ecoli_zinc_regulation_summary`
- `takahashi2015_ecoli_zinc_regulation.species_labels` -> `visualisation.takahashi2015_ecoli_zinc_regulation_species_labels`
- `takahashi2015_ecoli_zinc_regulation.extracellular_zinc` -> `visualisation.takahashi2015_ecoli_zinc_regulation_extracellular_zinc`
- `takahashi2015_ecoli_zinc_regulation.intracellular_zinc` -> `visualisation.takahashi2015_ecoli_zinc_regulation_intracellular_zinc`
- `takahashi2015_ecoli_zinc_regulation.receptor_state` -> `visualisation.takahashi2015_ecoli_zinc_regulation_receptor_state`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: How does the zinc regulation system respond across its tracked molecular states?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows Zext, Z, R through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:MODEL1502180000
- Upstream URL: https://www.ebi.ac.uk/biomodels/MODEL1502180000
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
