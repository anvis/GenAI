import csv
import os

with open(os.path.dirname(__file__) + '/moveies.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
####


import pandas as pd

df = pd.read_csv(os.path.dirname(__file__) + '/moveies.csv')
print(df.head())



with open(os.path.dirname(__file__) + '/moveiesHead.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row['Name'], row['Age'])
        print(row)
        print(row['Age'])

print("Reading CSV with Pandas")


# Read the first sheet
df = pd.read_excel(os.path.dirname(__file__) + '/movieees.xlsx')
print(df.head())

# Read a specific sheet
df = pd.read_excel(os.path.dirname(__file__) + '/movieees.xlsx', sheet_name='Sheet1')
print(df.head())

# Read multiple sheets
dfs = pd.read_excel(os.path.dirname(__file__) + '/movieees.xlsx', sheet_name=None)  # returns a dict of DataFrames
print(df.head())
