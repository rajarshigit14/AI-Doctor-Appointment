import os
from dotenv import load_dotenv
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
query=collection.find({"Department":"Allergist","Priority":"junior"})
#print(list(query))
a=list(query)
print(type(a))


today = date.today()
day=today + timedelta(days=2)
print(day)

Thursday={"9763820415":[0,0],"3658924710":[0,0,0,0,0,0,0,0],"8475092163":[0,0,0,0,0,0,0,0],
          "4210935678":[0,0,0,0,0,0,0,0],"9274610835":[0,0,0,0,0,0,0,0],"8745120936":[0,0,0,0,0,0],
          "4567890123":[0,0,0,0,0,0,0,0,0,0],"9368275410":[0,0,0,0],"7045821963":[0,0,0,0,0,0],
          "2187465039":[0,0,0,0,0,0,0,0],"8041967325":[0,0,0,0,0,0,0,0,0,0],"2501639487":[0,0,0,0,0,0,0,0],
          "1240938576":[0,0,0,0,0,0],"8240967315":[0,0,0,0,0,0],"5723019846":[0,0,0,0,0,0,0,0,0,0],
          "9048275163":[0,0,0,0],"9482637105":[0,0,0,0,0,0],"4976825310":[0,0,0,0,0,0,0,0,0,0],
          "6328491705":[0,0,0,0,0,0],"4827956103":[0,0,0,0,0,0,0,0],"8396172054":[0,0,0,0,0,0,0,0],
          "2163845790":[0,0,0,0,0,0,0,0],"8146903275":[0,0,0,0,0,0],"7314825609":[0,0,0,0,0,0],
          "5297840631":[0,0,0,0,0,0,0,0],"6827315940":[0,0,0,0,0,0],"6318425709":[0,0,0,0,0,0,0,0,0,0],
          "5361928470":[0,0,0,0,0,0],"6205831749":[0,0,0,0,0,0],"2583617940":[0,0,0,0,0,0],
          "5276938401":[0,0,0,0,0,0],"6704952138":[0,0,0,0,0,0],"8293614750":[0,0,0,0,0,0,0,0,0,0,0,0],
          "3984715620":[0,0,0,0,0,0,0,0,0,0,0,0],"5274093168":[0,0,0,0,0,0,0,0,0,0,0,0],
          "2361578940":[0,0,0,0,0,0,0,0,0,0,0,0],"3275086941":[0,0,0,0,0,0,0,0,0,0,0,0],
          "5723169840":[0,0,0,0,0,0,0,0,0,0,0,0],"4296187503":[0,0,0,0,0,0,0,0,0,0,0,0],
          "1432765980":[0,0,0,0,0,0,0,0,0,0,0,0]}

result=doctors_list(a,day,Thursday)
print(result)
