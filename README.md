# models-microbiology

Curated collection of **microbiology** simulation models for the **biosim** platform. This repository contains computational models of microbial systems, including bacterial genetics, yeast metabolism, synthetic biology circuits, viral strategies, and microbial population dynamics.

## What's Inside

### Models (57 packages)

**Microbiology** — bacterial and fungal systems, synthetic circuits, and microbial dynamics:

**Key Areas:** Glycolytic oscillations (yeast), E. coli genetic circuits (toggle switch, predator-prey), calcium homeostasis, Min system spatial patterning, viral infection strategies, synthetic gene circuits, transcriptional responses, Corynebacterium metabolism, and budding yeast size control.

**Note:** This repository contains 57 models covering diverse microbial processes. For a complete list, see the `models/` directory.

## Standards & Usage

All models use SBML format with tellurium runtime. Models implement the `biosim.BioModule` interface and can be composed into multi-scale simulations.

### Prerequisites
- Python 3.11+
- `biosim` framework

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

## License

Dual-licensed: Apache-2.0 (code), CC BY 4.0 (content)
