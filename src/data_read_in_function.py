""" This function reads in a CSV file and returns a df frame """

import pandas as pd
def data_read_in(file_path):

# the file path should be: ../rsd-group-task/housing.csv

    """
    Reads a csv file and returns a df.

    Inputs:
       - file_path - the file path of the csv

    Output:
       df - a pandas dataframe
    """

    df = pd.read_csv(file_path)

    return df
