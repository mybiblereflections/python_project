
#
# Write a program that:
# -will read a XLS file from a folder (e.g; c:/temp/incoming/employee.xls)
# -the program should then calculate values in “expense” columns and then sum them up
# -export all the columns data along with total expense (as a new column ) to a new CSV file in the same folder.
#
# Author: Mariasoosai Simeon
# Jan 29, 2023

import csv
import pandas as pd


data = pd.read_excel('/Users/simeonmariasoosai/PycharmProjects/temp/incoming/employee.xls')
df_export = pd.DataFrame(data)
df = pd.DataFrame(data)

# Avoid employeeid column for summing the expenses
df = df.loc[:, df.columns!='employeeid']
# Create the totalexpeses data

sum_row = df.sum(axis=1)

# Update the totalexpeses column with new values calculated bu adding expense1, expense2 and expense3
for idx, row in df_export.iterrows():
        df_export.loc[idx, 'totalexpense'] = sum_row.loc[idx];

print('\nCalculated total expenses\n')

print (sum_row)                 # print the calculated sum

print('\nNew table with total expense column populated\n')
print(df_export)                # print the table with totalexpeses column updated

# Export the new table to CSV file
df_export.to_csv('/Users/simeonmariasoosai/PycharmProjects/temp/incoming/employee.csv', index=False)

# Verify the newly created CSV file

print('\nNewly created CSV file\n')
with open('/Users/simeonmariasoosai/PycharmProjects/temp/incoming/employee.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print (row);



