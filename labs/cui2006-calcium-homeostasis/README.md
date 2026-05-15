# Cui2006 CalciumHomeostasis Lab

Curated microbiology lab for Cui2006_CalciumHomeostasis. The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **Does the calcium homeostasis model maintain bounded rule-state dynamics?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: microbiology model dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- External Calcium (Caex)
- Total Calmodulin (CaMtotal)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- M (m)
- Z (z)
- H (h)
- X (x)

## Model Wiring

- `cui2006_calcium_homeostasis` uses `models/core`
- `visualisation` uses `models/visualisation`

- `cui2006_calcium_homeostasis.state` -> `visualisation.cui2006_calcium_homeostasis_state`
- `cui2006_calcium_homeostasis.summary` -> `visualisation.cui2006_calcium_homeostasis_summary`
- `cui2006_calcium_homeostasis.species_labels` -> `visualisation.cui2006_calcium_homeostasis_species_labels`
- `cui2006_calcium_homeostasis.calcium_homeostasis_variable_one` -> `visualisation.cui2006_calcium_homeostasis_calcium_homeostasis_variable_one`
- `cui2006_calcium_homeostasis.calcium_homeostasis_variable_two` -> `visualisation.cui2006_calcium_homeostasis_calcium_homeostasis_variable_two`
- `cui2006_calcium_homeostasis.calcium_homeostasis_variable_three` -> `visualisation.cui2006_calcium_homeostasis_calcium_homeostasis_variable_three`
- `cui2006_calcium_homeostasis.calcium_homeostasis_variable_four` -> `visualisation.cui2006_calcium_homeostasis_calcium_homeostasis_variable_four`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: Does the calcium homeostasis model maintain bounded rule-state dynamics?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows M, Z, H, X through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:MODEL0913003363
- Upstream URL: https://www.ebi.ac.uk/biomodels/MODEL0913003363
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
