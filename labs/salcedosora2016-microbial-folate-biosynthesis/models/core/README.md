# Salcedo-Sora2016 - Microbial folate biosynthesis and utilisation

This core model executes the bundled SBML file in `data/` through `biosim.contrib.sbml.TelluriumSBMLBioModule`.
The SBML file remains the scientific source of truth; this wrapper only declares Biosimulant metadata, conservative labels, and traceable public ports.

Scientific caveat: source symbols are exposed conservatively. Ambiguous identifiers are labeled as model states rather than reinterpreted biologically.
