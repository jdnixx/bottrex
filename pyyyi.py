'''
Created on Sep 8, 2017

@author: john
'''
from bittrex import bittrex

# key, secret





# # set up text dump file
# outputFile = open("output.txt", "w")
#    
# markets = api.getmarkets()
# for mkt in markets:
#     for key in mkt:
#         lineToWrite = "{0} : {1}\n".format(key, mkt[key])
#         outputFile.write(lineToWrite)
#     outputFile.write("\n")
#    
# outputFile.close

currentMarket = 'ETH-XLMLOL'

lastPrice = []
lpDelta = [] # stores the deltas of each last price differential

# queries for (current) last price and returns the differential from previous price
def comparePrice():
    mktSummary = api.getmarketsummary(currentMarket)[0]
    lastValue = mktSummary["Last"]
    prevValue = lastPrice.pop()
    delta = lastValue - prevValue
    lastPrice.append(prevValue)
    lastPrice.append(lastValue)
    
    return delta
