# config.py
class Config:
    from pymongo import MongoClient

    # Replace the following values with your MongoDB connection string and database name
    MONGODB_URI = "mongodb://localhost:27017"
    DATABASE_NAME = "mytestdb"

    # Create a MongoClient
    client = MongoClient(MONGODB_URI)

    # Access the database
    database = client[DATABASE_NAME]
