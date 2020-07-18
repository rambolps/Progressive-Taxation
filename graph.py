from matplotlib import pyplot as plt
import numpy as np


def fvp(ftax,ptax,country,prov,total):
    plt.style.use("fivethirtyeight")

    tax_names = [str(country), str(prov)] 
    amounts = [int(ftax), int(ptax)]

    plt.pie(amounts, labels=tax_names, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

    plt.title("You owe $"+ str(total) + " in taxes!")
    plt.tight_layout()
    plt.show()
