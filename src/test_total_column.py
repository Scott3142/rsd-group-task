import total_column
import data_read_in_function as dr

file_path = 'test.csv'
df = dr.data_read_in(file_path)

assert total_column.sum(df,'total_rooms') == 21460
