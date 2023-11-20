import pandas as pd
import os

path = os.getcwd()

file_path = 'code/test2.csv'
print(file_path)

matches = [' ""', '"" ']
try:
    with open(file_path, 'r') as file:
        for line in file:
            # if ' ""' or '"" ' in line:
            if any(i in line for i in matches):
                print("Characters in line: ", line)
            else:
                print("Characters NOT in line")

except FileNotFoundError:
    print(f"File not found at '{file_path}'.")


exit()

# df = pd.read_csv("code/test.csv", header=None, quotechar=") 
df = pd.read_csv("code/test1.csv", header=None, quotechar='"', escapechar='\\') 

pd.set_option('display.max_columns', None)

print(df.head())

print("Hello World")