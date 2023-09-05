from pymongo import MongoClient
# conn = MongoClient("mongodb://localhost:27017/rental") # localhost db
conn = MongoClient("mongodb+srv://admin:oWfBHWmnl77NQYao@cluster0.usi1jhb.mongodb.net/?retryWrites=true&w=majority") # Mongodb Atlas cloud

db = conn.leisure_db

collection_name = db["rental_work_collection"]

