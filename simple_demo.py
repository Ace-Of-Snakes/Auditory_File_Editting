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


def plot_bestand():
    # plot the bestand
    df.plot(x="EAN", y="Menge", kind="bar")
    plt.title("Bestand")
    plt.xlabel("Artikel")
    plt.ylabel("Menge")
    plt.show()

def append(df):
    df.loc[:,"Amazon-Preis"] = 50
    df.loc[:,"Ebay-Preis"] = 50
    return df

def clean(df):
    for i in range(len(df)):
        df.loc[i," Einkaufspreis "] = re.sub("�","",str(df.loc[i," Einkaufspreis "]))
    return df


def calculate(df):
    for i in range(len(df)):
        #Gewinn = Verkaufspreis - AmazonGebühren in % - AmazonGebühren in €
        einkaufspreis = float(re.sub(",",".",str(df.iloc[i,3])))
        amazon_gebuhren_prozent = re.sub(r"\,",".",df.iloc[i,4])
        amazon_gebuhren_prozent = float(re.sub("%","",amazon_gebuhren_prozent))/100
        amazon_gebuhren_euro = float(re.sub(r"\,",".",df.iloc[i,5]))

        verkaufspreis_amazon = float(re.sub(r"\,",".",str(df.loc[i,"Amazon-Preis"])))

        gewinn_mit_mwst_amazon = verkaufspreis_amazon *(1-amazon_gebuhren_prozent) - amazon_gebuhren_euro
        gewinn_ohne_mwst_amazon = gewinn_mit_mwst_amazon/1.19
        umsatz_amazon = round((gewinn_ohne_mwst_amazon - einkaufspreis),2)
        marge_amazon = round((umsatz_amazon/einkaufspreis*100),2)
        df.loc[i,"Gewinn-Amazon"] = re.sub(r"\.",",",str(umsatz_amazon))
        df.loc[i,"Marge-Amazon"] = re.sub(r"\.",",",str(f"{marge_amazon}%"))

        #Gewinn = Verkaufspreis - EbayGebühren in % - EbayGebühren in €
        ebay_gebuhren_prozent = re.sub(",",".",df.iloc[i,6])
        ebay_gebuhren_prozent = float(re.sub("%","",ebay_gebuhren_prozent))/100
        ebay_gebuhren_euro = float(re.sub(r"\,",".",df.iloc[i,7]))

        verkaufspreis_ebay = float(re.sub(r"\,",".",str(df.loc[i,"Ebay-Preis"])))

        gewinn_mit_mwst_ebay = verkaufspreis_ebay *(1-ebay_gebuhren_prozent) - ebay_gebuhren_euro
        gewinn_ohne_mwst_ebay = gewinn_mit_mwst_ebay/1.19
        umsatz_ebay = round((gewinn_ohne_mwst_ebay - einkaufspreis),2)
        marge_ebay = round((umsatz_ebay/einkaufspreis*100),2)
        df.loc[i,"Gewinn-Ebay"] = re.sub(r"\.",",",str(umsatz_ebay))
        df.loc[i,"Marge-Ebay"] = re.sub(r"\.",",",str(f"{marge_ebay}%"))

        if umsatz_amazon > 10 or marge_amazon > 10:
            df.loc[i,"Potential-Amazon"] = "yes"
        else:
            df.loc[i,"Potential-Amazon"] = "no"

        if umsatz_ebay > 10 or marge_ebay > 10:
            df.loc[i,"Potential-Ebay"] = "yes"
        else:
            df.loc[i,"Potential-Ebay"] = "no"
    return df

if __name__ == "__main__":
    # __name__ == "__main__" is used to run the code only when the file is executed directly and not called in different program
    
    # create a dataframe object
    # dataframe is a 2D data structure
    # it is a table like structure with rows and columns 
    # we can set the delimiter of the dataframe and encoding with the help of read_csv function
    df = pd.read_csv("snack.csv", delimiter=";", encoding="utf-8")

    # there are many functions in pandas like read_csv, read_excel, htlm, json, etc
    # print the dataframe
    df = clean(df)
    df = append(df)
    df = calculate(df)
    plot_bestand()
    df.to_csv("output.csv", sep=";", encoding="utf-8", index=False)
