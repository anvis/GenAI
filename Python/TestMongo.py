

from pymongo import MongoClient, errors

def fetch_data_from_mongodb(uri, db_name, collection_name, query=None):
    """
    Connects to MongoDB and fetches documents from a given collection.
    
    :param uri: MongoDB connection string (e.g., "mongodb://localhost:27017/")
    :param db_name: Name of the database
    :param collection_name: Name of the collection
    :param query: MongoDB query filter (default: None -> fetch all)
    :return: List of documents
    """
    try:
        # Connect to MongoDB
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        
        # Test connection
        client.server_info()
        
        # Access database and collection
        db = client[db_name]
        collection = db[collection_name]
        
        # Default query: fetch all documents
        if query is None:
            query = {}
        
        # Fetch documents
        documents = list(collection.find(query))
        
        return documents
    
    except errors.ServerSelectionTimeoutError:
        print("Error: Could not connect to MongoDB server.")
        return []
    except errors.PyMongoError as e:
        print(f"MongoDB Error: {e}")
        return []
    finally:
        # Close connection
        try:
            client.close()
        except:
            pass


# Example usage
if __name__ == "__main__":
    # Replace with your MongoDB URI and details
    MONGO_URI = "mongodb://localhost:27017/"
    DATABASE_NAME = "Articles"
    COLLECTION_NAME = "Basics"
    
    # Example query: fetch users with age > 25
    query_filter = {"age": {"$gt": 25}}
    
    results = fetch_data_from_mongodb(MONGO_URI, DATABASE_NAME, COLLECTION_NAME, None)
    
    if results:
        print("Fetched documents:")
        for doc in results:
            print(doc)
    else:
        print("No documents found or error occurred.")

