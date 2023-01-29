# ucsf_python_project
#
# This python program read an xls spreadsheet located in c:~/PycharmProjects/temp/incoming/employee.xls and 
# calculate values in “expense” columns and then sum them up and place it in totalexpense column. Thenit
# exports all the columns data along with total expense to a new CSV file in the same folder as c:~/PycharmProjects/temp/incoming/employee.csv
#
# Author: Mariasoosai Simeon
# Jan 29, 2023
#
# Python pandas library is used to import data from xls spreadsheets and python csv library is used to export the updated
# tables as a csv file in the same folder
#
# Setup Instructions
#
# 1. Install python3.7
# 2. pip install xlrd # This contains pandas library
# 3. pip show pandas
#
# Create incomin following data as employee.xls in c:~/PycharmProjects/temp/incoming
#
#  
# employeeid	expense1	expense2	expense3	totalexpense
# 1	11.11	3	0.55	 
# 2	1000	4	0.55	 
# 3	333	5	0.55	 
# 4	24.45	6	0.55	 
# 5	113.45	7	0.55	 
#
# Create csv_rw.py in c:~/PycharmProjects/ucsf_csv_rw directory
#
# Run the csv_rw.py and it will create c:~/PycharmProjects/temp/incoming/employee.csv with the following content that has totalexpense column filled with
# summation of values from expense1, expense2 and expense3 columns
#




