"""
first we have to install the package with pip
- pip install pandas
"""
# import pandas module into the file
import pandas as pd

# import numpy module into the file
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

def clean(df):
    for i in range(len(df)):
        df.loc[i," Einkaufspreis "] = re.sub("�","",str(df.loc[i," Einkaufspreis "]))
    return df

if __name__== "__main__":
        # __name__ == "__main__" is used to run the code only when the file is executed directly and not called in different program
    
    # create a dataframe object
    # dataframe is a 2D data structure
    # it is a table like structure with rows and columns 
    # we can set the delimiter of the dataframe and encoding with the help of read_csv function
    df = pd.read_csv("snack.csv", delimiter=";", encoding="utf-8")

    # there are many functions in pandas like read_csv, read_excel, htlm, json, etc
    # print the dataframe
    print(df[" Einkaufspreis "])
    df = clean(df)
    print(df[" Einkaufspreis "])