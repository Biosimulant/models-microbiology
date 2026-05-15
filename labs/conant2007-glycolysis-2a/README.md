# MODEL2426780967 url.xml Lab

Curated microbiology lab for MODEL2426780967_url.xml. The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **Which glycolytic state changes most strongly in the bundled SBML run?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: metabolic pathway dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- External Glucose (GLCo)
- Whole Genome Duplication Enzyme Scale (WGD_E)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- GLCi (GLCi)
- ATP (ATP)
- G6P (G6P)
- ADP (ADP)

## Model Wiring

- `conant2007_glycolysis_2a` uses `models/core`
- `visualisation` uses `models/visualisation`

- `conant2007_glycolysis_2a.state` -> `visualisation.conant2007_glycolysis_2a_state`
- `conant2007_glycolysis_2a.summary` -> `visualisation.conant2007_glycolysis_2a_summary`
- `conant2007_glycolysis_2a.species_labels` -> `visualisation.conant2007_glycolysis_2a_species_labels`
- `conant2007_glycolysis_2a.intracellular_glucose` -> `visualisation.conant2007_glycolysis_2a_intracellular_glucose`
- `conant2007_glycolysis_2a.atp` -> `visualisation.conant2007_glycolysis_2a_atp`
- `conant2007_glycolysis_2a.glucose_6_phosphate` -> `visualisation.conant2007_glycolysis_2a_glucose_6_phosphate`
- `conant2007_glycolysis_2a.adp` -> `visualisation.conant2007_glycolysis_2a_adp`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: Which glycolytic state changes most strongly in the bundled SBML run?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows GLCi, ATP, G6P, ADP through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:MODEL2426780967
- Upstream URL: https://www.ebi.ac.uk/biomodels/MODEL2426780967
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
