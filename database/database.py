#(©)CodeXBotz
#recoded by its_tartaglia_Childe


import pymongo
from config import DB_URI, DB_NAME

# Create a function to connect to the MongoDB database
def connect_to_mongodb():
    try:
        # Connect to the MongoDB server using the DB_URI and select the database
        dbclient = pymongo.MongoClient(DB_URI)
        database = dbclient[DB_NAME]
        user_data = database['users']
        return user_data
    except pymongo.errors.ServerSelectionTimeoutError as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

# Create a function to close the MongoDB connection
def close_mongodb_connection(user_data):
    if user_data:
        user_data.close()

# Define your async functions for working with the MongoDB database
async def present_user(user_id, user_data):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id, user_data):
    user_data.insert_one({'_id': user_id})

async def full_userbase(user_data):
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

async def del_user(user_id, user_data):
    user_data.delete_one({'_id': user_id})

if __name__ == '__main__':
    user_data = connect_to_mongodb()  # Connect to MongoDB
    if user_data:
        try:
            # You can now use the user_data object for your database operations
            user_id = 12345
            await add_user(user_id, user_data)
            await present_user(user_id, user_data)
            await full_userbase(user_data)
            await del_user(user_id, user_data)
        finally:
            close_mongodb_connection(user_data)  # Close the MongoDB connection
    else:
        # Handle the case where the MongoDB connection could not be established
        pass
