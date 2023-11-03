#(©)CodeXBotz
#recoded by its_tartaglia_Childe

import pymongo
from pymongo.errors import ServerSelectionTimeoutError
from config import DB_URI, DB_NAME

def connect_to_mongodb():
    try:
        dbclient = pymongo.MongoClient(DB_URI)
        database = dbclient[DB_NAME]
        user_data = database['users']
        return user_data
    except ServerSelectionTimeoutError as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

async def present_user(user_id: int, user_data):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int, user_data):
    user_data.insert_one({'_id': user_id})

async def full_userbase(user_data):
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

async def del_user(user_id: int, user_data):
    user_data.delete_one({'_id': user_id})

# Usage example
if __name__ == '__main__':
    user_data = connect_to_mongodb()
    if user_data:
        # Now you can use the user_data object for your database operations
        pass
    else:
        # Handle the case where the MongoDB connection could not be established
        pass
