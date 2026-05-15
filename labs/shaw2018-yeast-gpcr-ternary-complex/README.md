# Shaw 2018 - Yeast GPCR Ternary Complex Model Lab

Curated microbiology lab for Shaw 2018 - Yeast GPCR Ternary Complex Model. The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **Which yeast GPCR complex dominates the simulated response?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: microbiology model dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- Initial Ligand Level (L)
- Initial Receptor Level (R)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- R (R)
- LR (LR)
- Rstar (Rstar)
- LRstar (LRstar)

## Model Wiring

- `shaw2018_yeast_gpcr_ternary_complex` uses `models/core`
- `visualisation` uses `models/visualisation`

- `shaw2018_yeast_gpcr_ternary_complex.state` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_state`
- `shaw2018_yeast_gpcr_ternary_complex.summary` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_summary`
- `shaw2018_yeast_gpcr_ternary_complex.species_labels` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_species_labels`
- `shaw2018_yeast_gpcr_ternary_complex.receptor_state` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_receptor_state`
- `shaw2018_yeast_gpcr_ternary_complex.ligand_bound_receptor` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_ligand_bound_receptor`
- `shaw2018_yeast_gpcr_ternary_complex.active_receptor` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_active_receptor`
- `shaw2018_yeast_gpcr_ternary_complex.active_ligand_bound_receptor` -> `visualisation.shaw2018_yeast_gpcr_ternary_complex_active_ligand_bound_receptor`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: Which yeast GPCR complex dominates the simulated response?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows R, LR, Rstar, LRstar through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:MODEL1901300001
- Upstream URL: https://www.ebi.ac.uk/biomodels/MODEL1901300001
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
