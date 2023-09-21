import os
from dotenv import load_dotenv
from mis import date_conversion
from datetime import date,timedelta
from pymongo.mongo_client import MongoClient
from allocation import doctors_list
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
uri = SECRET_KEY 

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.database

# Created or Switched to collection names
collection = db.funky
#print(db.collection_names())


query=collection.find({"Department":"Allergist","Priority":"junior","Phone":"9763820415"})
#print(query)
print(list(query))
db1 = client.base
collection1 = db1.punky
print(db1.list_collection_names())

p=collection1.find_one({"date":"2023-09-21"})
print(p)
#a=list(query)
#print(type(a))
'''
for j in range(1,15):
    today = date.today()
    day=today + timedelta(days=j)
    print(day)
    d=str(day)
    p=collection1.find_one({"date":day})
    for k in p:
        print(k)
        print('~~~~\n\n')
    #y=p["Times"]
    #print(type(y))
    result=doctors_list(a,str(day),y)
    print(result)
    if result != "-1":
        break'''
