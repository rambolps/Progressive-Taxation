#Import graph library
from matplotlib import pyplot as plt

#create pie chart based of tax info
def fvp(ftax,ptax,country,prov,total):
    plt.close()
    plt.style.use("fivethirtyeight")

    tax_names = [str(country), str(prov)] 
    amounts = [int(ftax), int(ptax)]

    plt.pie(amounts, labels=tax_names, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

    plt.title("You owe $"+ str(total) + " in taxes!")
    plt.tight_layout()
    plt.show()
