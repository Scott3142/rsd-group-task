'''
Function to run simple data analysis on data set housing.csv
'''

import total_column
import data_read_in_function as dr

def run():

    file_path = '../data/housing.csv'
    data_frame = dr.data_read_in(file_path)

    total_rooms = total_column.sum(data_frame,'total_rooms')

    return total_rooms

run()
