import pandas as pd
import numpy as np


my_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(my_list)


my_array = np.array([10, 20, 30, 40, 50])
series_from_array = pd.Series(my_array)


my_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}
custom_index = ['B', 'C', 'D', 'E', 'F']
series_from_dict = pd.Series(my_dict, index=custom_index)

print(series_from_list)
print(series_from_array)
print( series_from_dict)





result_add = series_from_list + series_from_array
result_subtract = series_from_list - series_from_array
result_multiply = series_from_list * series_from_array
result_divide = series_from_list / series_from_array

print(result_add)
print(result_subtract)
print( result_multiply)
print(result_divide)





print(series_from_dict['B'])
print(series_from_dict.iloc[2])




threshold = 30
filtered_series = series_from_dict[series_from_dict > threshold]
print( filtered_series)




data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_from_dict = pd.DataFrame(data_dict)
print( df_from_dict)



data_array = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
df_from_array = pd.DataFrame(data_array, columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])
print(df_from_array)



df_from_csv = pd.read_csv('data.csv')
print( df_from_csv)



print( df_from_csv.head())
print( df_from_csv.tail())



summary = df_from_csv.describe()
print( summary)




specific_column = df_from_csv['Column_Name']
print(specific_column)



filtered_rows = df_from_csv[df_from_csv['Column_Name'] > threshold]
print(filtered_rows)




multiple_conditions = df_from_csv[(df_from_csv['Column1'] > value1) & (df_from_csv['Column2'] < value2)]
print(multiple_conditions)




df_from_csv['New_Column'] = [value1, value2, value3, ...]
print(df_from_csv)




df_without_column = df_from_csv.drop(columns=['Column_Name'])
print(df_without_column)




renamed_df = df_from_csv.rename(columns={'Old_Name': 'New_Name'})
print(renamed_df)
