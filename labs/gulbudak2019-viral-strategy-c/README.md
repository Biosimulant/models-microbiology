# Gulbudak2019.2 - Heterogeneous viral strategies promote coexistence in virus-microbe systems (Chronic) Lab

Curated microbiology lab for Gulbudak2019.2 - Heterogeneous viral strategies promote coexistence in virus-microbe systems (Chronic). The bundled SBML is executed directly through Tellurium and visualised with conservative, source-traceable labels.

This lab asks: **Do host and viral compartments remain bounded in the coexistence model?**

## Model Context

The core model executes the bundled sbml source through Biosimulant and publishes traceable state, summary, and observable ports. The visualisation model turns those ports into dark-mode run cards for quick inspection of microbiology dynamics.

Scope: microbial population and host-interaction dynamics.

Caveat: The bundled SBML is the executable source of truth; labels are conservative where source symbols are ambiguous.

## Run Context

- Duration: 10
- Communication step: 0.01
- Initial inputs: lab defaults

## Primary Inputs

- Infection Rate (beta)

## Primary Outputs

- Model state (state)
- Simulation summary (summary)
- Observable labels (species_labels)
- S (S)
- C (C)
- V C (V_C)

## Model Wiring

- `gulbudak2019_viral_strategy_c` uses `models/core`
- `visualisation` uses `models/visualisation`

- `gulbudak2019_viral_strategy_c.state` -> `visualisation.gulbudak2019_viral_strategy_c_state`
- `gulbudak2019_viral_strategy_c.summary` -> `visualisation.gulbudak2019_viral_strategy_c_summary`
- `gulbudak2019_viral_strategy_c.species_labels` -> `visualisation.gulbudak2019_viral_strategy_c_species_labels`
- `gulbudak2019_viral_strategy_c.susceptible_hosts` -> `visualisation.gulbudak2019_viral_strategy_c_susceptible_hosts`
- `gulbudak2019_viral_strategy_c.carrier_hosts` -> `visualisation.gulbudak2019_viral_strategy_c_carrier_hosts`
- `gulbudak2019_viral_strategy_c.free_chronic_virus` -> `visualisation.gulbudak2019_viral_strategy_c_free_chronic_virus`

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

#### visualisation table

The summary table records the numeric run outputs used to answer the lab question: Do host and viral compartments remain bounded in the coexistence model?

![visualisation table](assets/01-visualisation-table.png)

#### visualisation timeseries

The time-series view follows S, C, V C through the simulated run so the transient and final microbial dynamics are visible in one panel.

![visualisation timeseries](assets/02-visualisation-timeseries.png)

#### visualisation bar

The comparison view ranks the headline outputs from this run, making the dominant endpoint responses easy to scan.

![visualisation bar](assets/03-visualisation-bar.png)

<!-- BIOSIMULANT_VISUALS_END -->

## Source and Dependencies

- Core model: `models/core`
- Visualisation model: `models/visualisation`
- Upstream source: biomodels_ebi:BIOMD0000000846
- Upstream URL: https://www.ebi.ac.uk/biomodels/BIOMD0000000846
- License: CC0
- Runtime packages: tellurium==2.2.11.2

## Running in Biosimulant

Open this folder as a Biosimulant lab, then run the canvas. The screenshots above were captured from the served lab UI in dark mode using the automated README visualisation workflow.
