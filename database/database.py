#(©)CodeXBotz
#recoded by its_tartaglia_Childe


import pymongo
from pymongo.errors import ServerSelectionTimeoutError
from config import DB_URI, DB_NAME

async def connect_to_mongodb():
    try:
        dbclient = pymongo.MongoClient(DB_URI)
        database = dbclient[DB_NAME]
        user_data = database['users']
        return user_data
    except ServerSelectionTimeoutError as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

async def close_mongodb_connection(client):
    if client:
        client.close()

async def database_operations():
    client = await connect_to_mongodb()
    if client:
        try:
            # Now you can use the user_data object for your database operations
            # For example:
            user_id = 12345
            await add_user(user_id, client)
            await present_user(user_id, client)
            await full_userbase(client)
            await del_user(user_id, client)
        finally:
            await close_mongodb_connection(client)
    else:
        # Handle the case where the MongoDB connection could not be established
        pass

# Usage example
if __name__ == '__main__':
    import asyncio
    asyncio.run(database_operations())
