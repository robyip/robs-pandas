import pandas as pd
import os

path = os.getcwd()

print(path)


df = pd.read_csv("code/test.csv", header=None)

print(df.head())

print("Hello World")