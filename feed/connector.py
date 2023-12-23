from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Ashutoshkrh:qwerty123@cometcluster.uy4wmvi.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection

def initialize():
    try:
        client.admin.command('ping')
        print(" successfully connected to MongoDB!")
        db=client["Nimbus"]
        return db
    except Exception as e:
        print(e)

    return "Error"
# try:
#     client.admin.command('ping')
#     db = client["Comets"]
#     # db.create_collection('user2')
#     # result = db.list_collection_names()
#     # print(result)
#     user_col = db["users"]
#     # data = {'name' : 'Navneet', 'roll_no' : '2101AI07', 'college' : 'IITP'}
#     # data_list = [data ,{'hello' : 'World'}]
#     user2_col = db["user2"]
#     # user2_col.insert_many(data_list)
#     # user_col.insert_one(data)
#     # data = {'name' : 'Ashutosh', 'roll_no' : '2101AI23', 'college' : 'IITJ'}

#     # user2_col.insert_one(data)
#     # CURD
#     # print(user2_col.delete_one({ 'name': { '$regex': "^Nav" }}))
#     # user2_col.update_one({'name' :{'$regex': "Ashutosh"}},{'$set': {'name' : 'Kush'}})
#     l = user2_col.find({'name' : {'$regex': "^"}},{'_id': 0,'name' : 1,'college' : 1 }).sort('name')
#     for i in l:
#         print(i)      
    
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)