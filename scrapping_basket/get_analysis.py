import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path


def get_analysis(csv):
    """
    Description: Function to preprocess the data set to perform the analysis
    :param csv: Resulting csv from scrapping
    :return: void
    """

    df_nba = pd.read_csv(csv)
    description = df_nba.describe()

    analysis = "analysis"

    if not os.path.exists(analysis):
        os.mkdir(analysis)
    description.to_csv(os.path.join(analysis, "description_data.csv"))

    df_types_variable = df_nba.dtypes
    df_types_variable.to_csv(os.path.join(analysis, "type_of_variables.csv"))

    number_of_nans = df_nba.isna().sum()
    number_of_nans.to_csv(os.path.join(analysis, "number_of_nans.csv"))

    ####All histogtrams#####

    df = df_nba
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
            df.hist(column=col)
            plt.savefig(os.path.join(analysis, f"{col}.png"))
        except ValueError:
            print('This column can not be represented as a histogram')




if __name__ == "__main__":

    csv_name = "nba_stats_1.csv"
    path = "/Users/Stephi/Documents/academic/UOC/tercer_semestre/tipologia/PRAC1/skobsar_jordiba90_prac1/output_csv"
    abs_path_input_df = os.path.join(path, csv_name)
    get_analysis(abs_path_input_df)

