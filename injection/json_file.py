import json

inject = {
    "total_money": 1000000,
    "rent": 300000,
    "groceries": 50000,
    "transportation": 20000,
    "utilities": 10000,
    "entertainment": 15000
}

file = open("inject.json","w")
json.dump(inject,file)
file.close()