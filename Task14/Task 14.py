import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
df = pd.read_csv('data.csv')


missing_values = df.isnull()
df_dropna_rows = df.dropna()
df_dropna_columns = df.dropna(axis=1)
df_fillna = df.fillna(value=0)
df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')
df_interpolate = df.interpolate()

df['A'] = df['A'].fillna(0).astype(int)
df['E'] = df['E'].apply(lambda x: x * 10)
df['B_normalized'] = (df['B'] - df['B'].min()) / (df['B'].max() - df['B'].min())
df['E_standardized'] = (df['E'] - df['E'].mean()) / df['E'].std()

duplicate_rows = df.duplicated()
df_drop_duplicates = df.drop_duplicates()
df_drop_duplicates_specific = df.drop_duplicates(subset=['A', 'C'])

df['C_lower'] = df['C'].str.lower()
df['C_stripped'] = df['C'].str.strip()
df['C_replaced'] = df['C'].str.replace('ba', 'XX')

df['D_year'] = df['D'].dt.year
df['D_month'] = df['D'].dt.month
df['D_day'] = df['D'].dt.day

start_date = pd.to_datetime('2023-01-02')
end_date = pd.to_datetime('2023-01-04')
df_filtered_date = df[(df['D'] >= start_date) & (df['D'] <= end_date)]

df_encoded = pd.get_dummies(df, columns=['C'])

label_encoder = LabelEncoder()
df['C_encoded'] = label_encoder.fit_transform(df['C'].fillna(''))

df['C_grouped'] = df['C'].replace({'foo': 'Group1', 'bar': 'Group1', 'baz': 'Group2', 'qux': 'Group2'})

df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})
df_merged = pd.merge(df1, df2, on='key', how='inner')

df_concat_vertical = pd.concat([df1, df2], axis=0)
df_concat_horizontal = pd.concat([df1, df2], axis=1)

df['F'] = df['A'] + df['B']

bins = [0, 10, 20, 30, 40, 50]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50']
df['B_bins'] = pd.cut(df['B'], bins=bins, labels=labels)

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(df[['A', 'B']].fillna(0))

df.head(), df_dropna_rows.head(), df_dropna_columns.head(), df_fillna.head(), df_ffill.head(), df_bfill.head(), df_interpolate.head(), df_encoded.head(), df_merged.head(), df_concat_vertical.head(), df_concat_horizontal.head(), df_filtered_date.head(), df.tail()
