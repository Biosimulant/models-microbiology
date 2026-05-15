# Tan2012 - Antibiotic Treatment, Inoculum Effect Lab

Curated microbiology lab for Tan2012 - Antibiotic Treatment, Inoculum Effect. The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **How does the modeled bacterial concentration change during antibiotic exposure?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: microbiology model dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- Antibiotic Killing Rate (kd)
- Initial Ribosome Concentration (c)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- Ribosome concentration (c)

## Model Wiring

- `tan2012_antibiotic_inoculum_effect` uses `models/core`
- `visualisation` uses `models/visualisation`

- `tan2012_antibiotic_inoculum_effect.state` -> `visualisation.tan2012_antibiotic_inoculum_effect_state`
- `tan2012_antibiotic_inoculum_effect.summary` -> `visualisation.tan2012_antibiotic_inoculum_effect_summary`
- `tan2012_antibiotic_inoculum_effect.species_labels` -> `visualisation.tan2012_antibiotic_inoculum_effect_species_labels`
- `tan2012_antibiotic_inoculum_effect.ribosome_concentration` -> `visualisation.tan2012_antibiotic_inoculum_effect_ribosome_concentration`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: How does the modeled bacterial concentration change during antibiotic exposure?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows Ribosome concentration through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:BIOMD0000000425
- Upstream URL: https://www.ebi.ac.uk/biomodels/BIOMD0000000425
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
