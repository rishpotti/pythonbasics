#parse a json file to count the number of shampoo items available from each e-retailer

import json

f = open("C:\\Users\\AppuAchuAnu\\Downloads\\search_result.json")

search_result_dictionary = json.load(f)
f.close()

merchant_set = set()

for product in search_result_dictionary['productList']:
    merchant_set.add(product['merchant'])
  
merchant_dict = {}
  
for merchant in merchant_set:
    merchant_dict.update({merchant: 0})
    
for product in search_result_dictionary['productList']:
    for merchant in merchant_set:
        if product['merchant'] == merchant:
            merchant_dict[merchant] = merchant_dict[merchant] + 1
            
outputjson = json.dumps(merchant_dict, indent = 2)

print(outputjson)