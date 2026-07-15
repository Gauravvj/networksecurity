from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gaurav_joshi:gaurav123@cluster0.zpbfhnd.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)