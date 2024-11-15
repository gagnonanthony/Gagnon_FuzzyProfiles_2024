#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from cyclopts import App, Parameter
from typing_extensions import Annotated


# Initializing the app.
app = App(default_parameter=Parameter(negative=()))


@app.default()
def main(
    in_root_folder: Annotated[
        str,
        Parameter(
            help="ABCD Release >= 5.0 root folder path.",
            show_default=False,
            group="Essential Files Options",
        ),
    ],
    output: Annotated[
        str,
        Parameter(
            help="Output dataset filename and path.",
            show_default=False,
            group="Essential Files Options",
        ),
    ],
):
    """
    generating_disorders_dataset.py is a script that reproduce the variables
    used in [1] but for youth KSADS data. This script is specifically
    designed and hard-coded for the mh_p_ksads_ss.csv from the ABCD Data
    Release 5.0 and is adapted in python
    from this R code [2].

    [1] Bernanke, J., Luna, A., Chang, L., Bruno, E., Dworkin, J., & Posner, J.
        (2022). Structural brain measures among children with and without ADHD
        in the Adolescent Brain and Cognitive Development Study cohort: A
        cross-sectional US population-based study. The Lancet Psychiatry, 9(3),
        222–231. https://doi.org/10.1016/S2215-0366(21)00505-8

    [2] Source R Code:
    https://github.com/jabernanke/lancet/blob/main/JB%20-%20consolidated%20for%20Lancet%20-%20final.R

    """

    # Load dataset for KSADS diagnosis data.
    df_ksads = pd.read_csv(
        f'{in_root_folder}/core/mental-health/mh_y_ksads_ss.csv',
        dtype={'ksads_import_id_p': str,
               'ksads_timestamp_p': str,
               'ksads2_import_id_p': str,
               'ksads2_timestamp_p': str})

    # Using only baseline data.
    df_ksads_baseline = \
        df_ksads.loc[df_ksads["eventname"] == "baseline_year_1_arm_1"]

    # Little selector function where if any values in a row == 1, return 1
    # else 0.
    def selector(row):
        if 1 in row.values:
            return 1
        return 0

    # Anxiety disorders.
    # Using PD, agoraphobia, separation anxiety, social anxiety and
    # GAD (if one of them == 1, then 1 is returned).
    anx_vars = [
        # "ksads_5_857_t", Not available in the youth dataset.
        # "ksads_6_859_t", Not available in the youth dataset.
        # "ksads_7_861_t", Not available in the youth dataset.
        "ksads_8_863_t",
        # "ksads_9_867_t", Not available in the youth dataset.
        "ksads_10_869_t",
    ]
    anx_df = df_ksads_baseline[anx_vars]

    anx_score = anx_df.apply(selector, axis=1)

    # Depressive disorders.
    # Using PDD present, PDD partial remission, MDD present and MDD partial
    # remission.
    dep_vars = ["ksads_1_843_t",
                "ksads_1_844_t",
                "ksads_1_840_t",
                "ksads_1_841_t"]
    dep_df = df_ksads_baseline[dep_vars]

    dep_score = dep_df.apply(selector, axis=1)

    # Merging concatenated scores and fetching OCD, ODD, CD and PTSD at the
    # same time. All from the present variable.
    concat_output = pd.concat(
        [
            df_ksads_baseline["src_subject_id"],
            anx_score,
            # df_ksads_baseline["ksads_11_917_t"], Not available in the youth
            # dataset.
            dep_score,
            # df_ksads_baseline["ksads_15_901_t"], Not available in the youth
            # dataset.
            # df_ksads_baseline["ksads_16_897_t"], Not available in the youth
            # dataset.
        ],
        axis=1,
    )
    concat_output.columns = [
        "subjectkey",
        "AD_youth",
        "DD_youth",
    ]

    # Filtering df for values = 888 and considering them as NaNs.
    concat_output = concat_output.replace(888, np.nan)
    clean_output = concat_output.dropna()
    clean_output.to_excel(f"{output}", header=True, index=False)


if __name__ == "__main__":
    app()
