from pymongo import MongoClient
import pprint

print("begin mongo experience!")

client = MongoClient('localhost', 27017)


dev = client.fluidlyDevelopment

print("******dev.invoices.find_one()")
pprint.pprint(dev.invoices.find_one())


print("******dev.invoices.find()")
for invoice in dev.invoices.find({"organisationId":2}, limit = 3):
  print("******invoice")
  pprint.pprint(invoice)
  print()
