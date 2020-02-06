# ATDx: Building an Architectural Technical Debt Index, replication Package

This repository is a companion page for the paper _"ATDx: Building an Architectural Technical Debt Index"_.

It contains all the material required to replicate our viability investigation, including (i) the scripts utilized to mine the raw experimental data, (ii) the scripts utilized for data processing and statistical analysis, and (iii) the entirety of the raw and processed results gathered for the investigation.

The comprehensive dataset of initial raw data mined for the viability investigation is made available, due to size limitations, at the following dedicated repository [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3595502.svg)](https://doi.org/10.5281/zenodo.3595502)

Content
---------------
The entirety of the experiment data required for the replication of the prototype implementation and results analysis are provided in three separate folders, namely:

* [data](https://github.com/ATDindeX/ATDx/tree/master/data) - Raw and processed data of the viability investigation
* [rule_classification](https://github.com/ATDindeX/ATDx/tree/master/rule_classification) - Initial rule set and architectural rule set (including _Gr_ and _ATDD_ mapping process data).
* [scripts](https://github.com/ATDindeX/ATDx/tree/master/scripts) 
    * [analysis_scripts](https://github.com/ATDindeX/ATDx/tree/master/scripts/analysis_scripts) - Scripts adopted to mine via [SonarCloud API](https://sonarcloud.io/) the data of the viability investigation.
    * [mining_scripts](https://github.com/ATDindeX/ATDx/tree/master/scripts/mining_scripts) - Scripts adopted for data processing and statistical analysis.


For further information on the content of the folders see the following Directory Structure Overview.

Directory Structure Overview
---------------
This reposisory is structured as follows:
 
    ATDx
    .
    ├── ATDx_Prototype_Tech_Report.pdf      Technical report on the prototype impementation
    │
    ├── data/
    │   ├── ar_values.csv                   Architectural rule violation values of filtered repository set
    │   ├── manual_repo_inspection.csv      Manual repository inspection data
    │   └── total_repo_metadata.csv         Matadata of initial repository set
    ├── rule_classification/
    │   ├── architectural_rules.csv         List of architectural rule set
    │   └── initial_rule_set.csv            List of initial rule set
    └── scripts/
        ├── analysis_scripts
        │   ├── calculate_ATDD_ATDx.r       Calculation of ATDD and ATDx values
        │   ├── filter_dataset.r            Repository filtering process
        │   ├── heatmap_plot.r              Correlation analysis
        │   └── vioplot.r                   Violin plot
        └── mining_scripts
            ├── filter_ar_values.py         Filter architectural rule values from mined rule violation values 
            ├── mine_repo_metadata.py       Mine initial repository metadata 
            └── mine_rule_values.py         Mine rule violation values 
