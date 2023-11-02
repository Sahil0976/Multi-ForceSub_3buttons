#(©)CodeXBotz




import pymongo
from config import DB_URI, DB_NAME

# Create a MongoClient instance outside the functions to reuse the connection.
dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]
user_data = database['users']

async def present_user(user_id: int):
    try:
        found = user_data.find_one({'_id': user_id})
        return bool(found)
    except Exception as e:
        # Handle the exception, e.g., log the error or return False
        print(f"Error in present_user: {e}")
        return False

async def add_user(user_id: int):
    try:
        user_data.insert_one({'_id': user_id})
    except Exception as e:
        # Handle the exception, e.g., log the error or raise it
        print(f"Error in add_user: {e}")
        raise e

async def full_userbase():
    try:
        user_docs = user_data.find()
        user_ids = [doc['_id'] for doc in user_docs]
        return user_ids
    except Exception as e:
        # Handle the exception, e.g., log the error or return an empty list
        print(f"Error in full_userbase: {e}")
        return []

async def del_user(user_id: int):
    try:
        user_data.delete_one({'_id': user_id})
    except Exception as e:
        # Handle the exception, e.g., log the error or raise it
        print(f"Error in del_user: {e}")
        raise e

# Close the MongoClient connection when you're done using it.
# dbclient.close()  # You can close the connection if needed when the script exits.
