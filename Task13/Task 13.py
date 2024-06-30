import pandas as pd

df = pd.read_csv('timezone1.csv')

first_five_rows = df.head()

last_five_rows = df.tail()

df.set_index('Timezone', inplace=True)

specific_column_values = df['City']

multiple_columns_df = df[['Offset', 'Population', 'Country']]

subset_loc = df.loc['Africa/Accra']

subset_iloc = df.iloc[1:3, 1:3]

filtered_rows = df[df['Population'] > 5000000]

grouped_mean = df.groupby('Country')['Population'].mean()

grouped_sum = df.groupby(['Offset', 'Country'])['Population'].sum()

grouped_agg = df.groupby('Country').agg({'Population': ['mean', 'sum'], 'Offset': 'max'})

group_sizes = df.groupby('Country').size()

multiple_conditions = df[(df['Population'] > 1000000) & (df['Offset'] > 0)]

query_result = df.query('Population > 1000000 and Offset > 0')

isin_filter = df[df['Country'].isin(['Ghana', 'Japan', 'UK'])]

df_renamed = df[['City', 'Population']].rename(columns={'City': 'City_Name', 'Population': 'Pop'})

print(first_five_rows, last_five_rows, specific_column_values, multiple_columns_df, subset_loc, subset_iloc, 
 filtered_rows, grouped_mean, grouped_sum, grouped_agg, group_sizes, multiple_conditions, query_result, 
 isin_filter, df_renamed)
