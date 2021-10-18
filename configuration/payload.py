from configuration.configuration import *

def bookpayload(gquery):
    row = rungquery(gquery)
    inputbook = {}
    inputbook["name"]= row[0]
    inputbook["isbn"]= row[1]
    inputbook["aisle"]= row[2]
    inputbook["author"]= row[3]
    return inputbook