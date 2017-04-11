# Create a simple list of blocks of stock. 
# These could be tuples with ticker symbols, number of shares, dates and price.

stockDict = { 'GE': 'General Electric',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]

## OLD CODE REFACTORED BELOW

# portfolio = dict()

# for purchase in purchases:
# 	ticker = purchase[0]
# 	full_company_name = stockDict[ticker]
# 	full_date = purchase[2]

# 	try:
# 		portfolio[ticker].append(purchase)
# 	except KeyError:
# 		portfolio[ticker] = list()
# 		portfolio[ticker].append(purchase)

# 	number_of_shares = purchase[1] 
# 	purchase_price = purchase[3]
# 	full_purchase_price = number_of_shares * purchase_price

# 	print("I purchased {} sock for ${} on {}".format(full_company_name, full_purchase_price, full_date))
# 	print("-------")
# 	print("-------")
	

# print(portfolio)
# print("-------")
# print("-------")

# for ticker,purchase in portfolio.items():
# 	print("----{}-----".format(ticker))
# 	total_portfolio_stock_value = 0
# 	for purchase in purchases:
# 		total_portfolio_stock_value += purchase[1] * purchase [3]
# 		print("    {}.".format(purchase))
# 	print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))

##########################################################################

# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock 
# and uses the stockDict to look up the full company name. 
# This is the basic relational database join algorithm between two tables.
print('Stock Purchase History Report')
for purchase in purchases:
    print('Purchased ${3} of {1}({0}) on {2}'.format(purchase[0], stockDict.get(purchase[0]), purchase[2], purchase[1]*purchase[3]))

# Create a second purchase summary that which accumulates total investment by ticker symbol. 
# In the above sample data, there are two blocks of GE.
# These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. 
# The program makes one pass through the data to create the dict. 
# A pass through the dict can then create a report showing each ticker symbol and all blocks of stock. 
print('Total Stocks Purchased')
stock_block = set()
for purchase in purchases:
    stock_block.add(purchase[0])
print(stock_block)
stocks = dict()
for ticker in stock_block:
    stocks[ticker] = 0
    for purchase in purchases:
        if ticker == purchase[0]:
            stocks[ticker] = stocks[ticker] + purchase[1]*purchase[3]
print(stocks)
	