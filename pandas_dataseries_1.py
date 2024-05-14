import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import openpyxl

ticker = input("Enter stock symbol:\n")
file = yf.download(ticker)

file = file.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1)
file = file.resample('Y').last()
max_price = file['Close'].max()


plt.plot(file.index,file['Close'], "o-")
plt.title(ticker + " Price since IPO")
plt.xlabel("Year")
plt.ylabel("Price")
plt.yticks(np.arange(0,max_price, step=10))

plt.show()

print(file)

excel_request = int(input("Would you like to download a spreadsheet (.xlsx) of this information?\n1 - Yes\n2 - No\n"))
if excel_request == 1:
    file = file.to_excel('output.xlsx')