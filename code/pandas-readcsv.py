import pandas as pd
import os

path = os.getcwd()

print(path)


# df = pd.read_csv("code/test.csv", header=None, quotechar=") 
df = pd.read_csv("code/test1.csv", header=None, quotechar='"', escapechar='\\') 

pd.set_option('display.max_columns', None)

print(df.head())

print("Hello World")