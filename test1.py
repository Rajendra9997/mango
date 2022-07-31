import  pymongo
client = pymongo.MongoClient("mongodb+srv://Rajendra123:mrkinghot@cluster0.cfvp5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"rajendra",
    "email":"rajendra@jadhav.ai",
    "surname":"jadhav"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )
