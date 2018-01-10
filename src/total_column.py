'''
Function to sum column of pandas data set given as input.
'''

def total_column(data_frame,column_title):

    return  data_frame[column_title].sum()
