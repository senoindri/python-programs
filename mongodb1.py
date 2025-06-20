from pymongo import MongoClient
client = MongoClient("mongodb+srv://oindri:oindrimongodb2006@cluster0.9nvwl1j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.test
db=client['trial1']
col=db["my_record"]

#insert area for execution without repeatation 

data={'name':'oindri',
      'age':'18',
      'time':'flexi'}
col.insert_one(data)

data1={
    "mail_id":"oindri@gmail.com",
    "phone_no":84204,
    "addr":"kolkata"
}
col.insert_one(data1)

data2=[{"name":"amy","address":"apple st 652"},
    {"name":"hannah","address":"mountain 21"},
    {"name":"michael","address":"valley 345"},
    {"name":"sandy","address":"ocean bvd 2"},
    {"name":"betty","address":"green grass 1"},
    {"name":"richard","address":"sky st 331"},
    {"name":"susan","address":"one way 98"},
    {"name":"vicky","address":"yellow garden 2"},
    {"name":"ben","address":"park lane 38"},
    {"name":"william","address":"central sy 954"},
    {"name":"chuck","address":"main road 989"},
    {"name":"viola","address":"sideway 1633"}
]
col.insert_many(data2)

data3={
    "name":"notebook",
    "qty":50,
    "rating":[{"score":8},{"score":9}],
    "size":{"height":11,"width":8.5,"unit":"in"},
    "status":"A",
    "tags":["college-ruled","perforated"]
}
col.insert_one(data3)

list_of_records=[
    {"companyName":"iNeuron",
     "product":"affordable ai",
     "courseOffered":"Machine Learning with Deployment"},
     {"companyName":"iNeuron",
     "product":"affordable ai",
     "courseOffered":"Deep Learning for NLP and Computer Vision"},
     {"companyName":"iNeuron",
     "product":"affordable ai",
     "courseOffered":"Data Science Masters Program"}
]
col.insert_many(list_of_records)    

print(col.find_one())

for i in col.find():
    print(i)

for i in col.find({"companyName":"iNeuron"}):
    print(i)
    
random_data=[
    {'_id':'3','companyName':'iNeuron','faculty':'xyz'},
    {'_id':'4','companyName':'iNeuron','faculty':'abc'},
    {'_id':'5','companyName':'iNeuron','faculty':'pqr'}    
    ]
col.insert_many(random_data)

for i in col.find({"_id":{"$gte":"4"}}):
    print(i)

col.update_many({"companyName":"iNeuron"},{"$set":{"companyName":"WorkMates"}})

col.update_many({},{"$unset":{'copmanyName':''}}) #made an error, added coPManyName instead of coMPany name, so have to delete