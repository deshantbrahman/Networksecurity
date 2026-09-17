
import pymongo
from pymongo.server_api import ServerApi

uri = "mongodb+srv://brahmandeshant_db_user:Deshant1234@cluster0.7ekk2ps.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = pymongo.MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)