![Python](https://img.shields.io/badge/Python-3.11-green6)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

## **Embracing the fuzziness of cognition and behavior and its relationship with environmental factors: A multi-cohort study.**

Authors: Anthony Gagnon<sup>1</sup>, Virginie Gillet<sup>1</sup>, Anne-Sandrine Desautels<sup>1</sup>, Jean-François Lepage<sup>1</sup>, Andrea Baccarelli<sup>2</sup>, Jonathan Posner<sup>3</sup>, Maxime Descoteaux<sup>4</sup>, Marie Brunet<sup>1</sup>, Larissa Takser<sup>1</sup>.

Affiliations:\
<sup>1</sup> Department of Pediatrics, University of Sherbrooke, Québec, Canada\
<sup>2</sup> Department of Environmental Health, Harvard T. H. Chan School of Public Health, Boston, MA, USA\
<sup>3</sup> Department of Psychiatry and Behavioral Sciences, Duke University, Durham, NC, USA\
<sup>4</sup> Sherbrooke Connectivity Imaging Lab (SCIL), University of Sherbrooke, Quebec, Canada

The present repository contains all relevant code and scripts to reproduce the results found in Gagnon et al. 2024. 

### **To use the fuzzy profiles in your own population**

In the `models/` folder, you can find the PCA model used for dimensionality reduction of the ABCD cohort. In addition, you will also find the **centroids** needed for the projection of your data in the profiles' space. To use it in your research, simply follow the steps regarding the GESTE and BANDA cohorts in the jupyter notebooks located in the `notebooks/` folder. Briefly, you should follow the residualization, reduction (EFA/CFA), harmonization, and imputation (if needed) steps found in `notebooks/2-DataPreprocessing.ipynb`, then you can proceed with the projection by following the steps in `notebooks/3-FCMeansClustering.ipynb`. **Please raise an issue if you have any questions.**

#### **Setting up**

If you do not have the required packages installed, it is recommended that you setup a new python virtual environment in which we will install the required dependencies. 

**Installing `virtualenv`**

Please run the following in your terminal window:
```bash
pipx install virtualenv
```

**Setting up a new `virtualenv` with python 3.11**

```bash
virtualenv --python 3.11 /path/to/your/destination/folder/

# Activate your newly created environment

source /path/to/your/destination/folder/bin/activate
```

**Installing `NeuroStatX`**

> [!IMPORTANT]
> Run the following commands from within your virtual environment.

```bash
pip install neurostatx==0.1.0

# Test the installation by calling the help of a CLI script.

AddNodesAttributes -h
```

**Installing `GraphViz`**

For visualization of semplots from the `semopy` python package, `GraphViz` is required. If you do not have it installed, please run the following if you are on Linux `sudo apt get graphviz` or `brew install graphviz` if you are on MacOS.

#### **Output file structure.**

By design, the notebooks are made to be run in a particular order (denoted by the numbering in the file name). If you run all of them, you should obtain this specific output file structure:

```bash
<output_directory>
├── awp
│   ├── AWP_ABCD
│   ├── AWP_ABCD_youth
│   ├── AWP_BANDA
│   ├── AWP_GESTE
│   └── AWP_GLOBAL
├── datagathering
│   ├── abcd_data.xlsx
│   ├── abcd_dx_labels.xlsx
│   ├── banda_data.xlsx
│   ├── banda_dx_labels.xlsx
│   └── geste_data.xlsx
├── demographicstable
│   └── demo_table.xlsx
├── fuzzyclustering
│   ├── ABCDFuzzyCMeans
│   ├── BANDAProjected
│   ├── GESTEProjected
│   ├── GraphNetwork
│   ├── GraphNetwork.gml
│   ├── VizNetwork
│   ├── VizNetworkDxABCD
│   ├── VizNetworkDxBANDA
│   ├── VizNetworkDxGESTE
│   ├── VizNetworkDxGlobal
│   └── merged_fcm_data.xlsx
├── LongitudinalProfiles
│   ├── datagathering
│   │   ├── abcd_data_2y.xlsx
│   │   ├── abcd_data_4y.xlsx
│   │   ├── abcd_data_baseline.xlsx
│   │   ├── abcd_dx_labels_2y.xlsx
│   │   └── abcd_dx_labels_baseline.xlsx
│   ├── datapreprocessing
│   │   ├── ABCD_2y_Apply
│   │   ├── ABCD_2y_CFA
│   │   ├── ABCD_2y_EFA
│   │   ├── ABCD_4y_Apply
│   │   ├── ABCD_4y_CFA
│   │   ├── ABCD_4y_EFA
│   │   ├── abcd_2y_preprocessed.xlsx
│   │   ├── abcd_2y_residualized.xlsx
│   │   ├── abcd_4y_preprocessed.xlsx
│   │   └── abcd_4y_residualized.xlsx
│   ├── demographics
│   │   └── demo_table_followups.xlsx
│   └── fuzzyclustering
│       ├── ABCD_2y_FCM
│       ├── ABCD_4y_FCM
│       ├── GraphNetwork2y
│       ├── GraphNetwork4y
│       ├── RadarPlot2y.png
│       ├── RadarPlot4y.png
│       ├── Tukey_results_2y.xlsx
│       ├── Tukey_results_4y.xlsx
│       ├── VizNetwork2y
│       ├── VizNetwork4y
│       ├── anova_2y.xlsx
│       ├── anova_4y.xlsx
│       ├── fcm_2y.xlsx
│       ├── fcm_4y.xlsx
│       └── silhouette_scores.png
├── preprocessing
│   ├── ABCD_CFA
│   ├── ABCD_CFA_Apply
│   ├── ABCD_EFA
│   ├── BANDA_CFA
│   ├── BANDA_CFA_Apply
│   ├── BANDA_EFA
│   ├── GESTE_CFA
│   ├── GESTE_CFA_Apply
│   ├── GESTE_EFA
│   ├── abcd_data_preprocessed.xlsx
│   ├── abcd_data_residualized.xlsx
│   ├── banda_data_preprocessed.xlsx
│   ├── banda_data_residualized.xlsx
│   ├── geste_data_preprocessed.xlsx
│   └── geste_data_residualized.xlsx
├── profileanalysis
│   ├── ABCD_coef1.png
│   ├── ABCD_coef2.png
│   ├── ABCD_coef3.png
│   ├── ABCD_coef4.png
│   ├── ABCD_coef5.png
│   ├── ABCD_coef6.png
│   ├── ABCD_coef7.png
│   ├── ABCD_coef_heatmap.png
│   ├── ABCD_env_loadings.png
│   ├── ABCD_plsr_coef.xlsx
│   ├── ABCD_plsr_coef_pval.xlsx
│   ├── ABCD_plsr_coef_pval_fdr_corrected.xlsx
│   ├── ABCD_plsr_scatter.png
│   ├── ABCD_plsr_stats.xlsx
│   ├── ABCD_profile_loadings.png
│   ├── GESTE_coef1.png
│   ├── GESTE_coef2.png
│   ├── GESTE_coef3.png
│   ├── GESTE_coef4.png
│   ├── GESTE_coef5.png
│   ├── GESTE_coef6.png
│   ├── GESTE_coef7.png
│   ├── GESTE_coef_heatmap.png
│   ├── GESTE_env_loadings.png
│   ├── GESTE_plsr_coef.xlsx
│   ├── GESTE_plsr_coef_pval.xlsx
│   ├── GESTE_plsr_coef_pval_fdr_corrected.xlsx
│   ├── GESTE_plsr_scatter.png
│   ├── GESTE_plsr_stats.xlsx
│   ├── GESTE_profile_loadings.png
│   ├── abcd_barplot_dx.png
│   ├── all_studies_barplot.png
│   ├── banda_barplot_dx.png
│   ├── circular_ABCD_dx.png
│   ├── circular_BANDA_dx.png
│   ├── circular_GESTE_dx.png
│   └── circular_barplot_all.png
└── viz
    ├── ANOVA_results.xlsx
    ├── ANOVA_results_cohorts.xlsx
    ├── NetworkABCD_AD_youth.png
    ├── NetworkABCD_DD_youth.png
    ├── NetworkABCD_PSYPATHO_youth.png
    ├── NetworkCohort.png
    ├── RadarPlotABCD.png
    ├── RadarPlotBANDA.png
    ├── RadarPlotCombined.png
    ├── RadarPlotGESTE.png
    ├── Tukey_results.xlsx
    └── Tukey_results_cohorts.xlsx


```
