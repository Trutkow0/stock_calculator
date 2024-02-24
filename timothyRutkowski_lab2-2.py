# Timothy Rutkowski 01/31/2024 timothyRutkowski_lab2-2.py

# This program will calculate and display stock calculations including:
# - The mount paid for stock per share and it's total
# - The price of commission paid on purchase of stock
# - The amount each stock was sold at and it's total
# - The price of commission paid on sale of stock
# - The profit or loss made on the entire stock transaction
# This program makes calulation based only on the assumption that all stocks 
# bought will be sold at once

#Gets math functions
import math

# Constant for broker commission rate (commRate)
commRate = .0325

# Displays input prompts and defines variables
sharesBought = int(input('Please enter the number of shares purchased: '))
pricePerShareBought = float(input('Please enter the price paid per share: '))

sharesSold = int(input('Please enter the number of shares sold: '))
pricePerShareSold = float(input('Please enter the selling price per share: '))



# Calculates and outputs the total price of shares purchased
totalSharePrice = sharesBought * pricePerShareBought
print('The total price of the shares purchased is: $',totalSharePrice)

# Calculates and outputs the commission rate on purchase
commPaidOnPurchase = float(commRate * totalSharePrice)
print('The total commission paid upon purchase is: $',commPaidOnPurchase)



# Calculates and outputs the total value of shares sold
totalValueOfSharesSold = float(sharesSold * pricePerShareSold)
print('The total value of the shares sold is: $',totalValueOfSharesSold)

# Calculates and outputs the total commission paid on sale
commPaidOnSale = float(totalValueOfSharesSold * commRate)
print('The price of commission paid upon sale is: $',commPaidOnSale)



# Calculates and outputs the total profit or loss on sale
totalProfit = (totalValueOfSharesSold - totalSharePrice) - (commPaidOnPurchase + commPaidOnSale)
print('The total profit (or loss) made on this sale is: $',totalProfit)