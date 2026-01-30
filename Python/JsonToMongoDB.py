import os
import json
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "Articles"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Input directory containing JSON files
json_base_dir = "articlesJson"

# Track slugs per collection to handle duplicates
collection_slugs = {}

# Recursively walk through all directories
for root, dirs, files in os.walk(json_base_dir):
    # Get the main folder name (first level under articlesJson)
    relative_path = os.path.relpath(root, json_base_dir)
    
    if relative_path == ".":
        main_folder = "root"
    else:
        # Extract the first folder name
        parts = relative_path.replace("\\", "/").split("/")
        main_folder = parts[0]
    
    # Get or create collection with main folder name
    collection = db[main_folder]
    
    # Initialize slug tracking for this collection
    if main_folder not in collection_slugs:
        collection_slugs[main_folder] = {}
    
    for filename in files:
        if filename.endswith(".json"):
            json_file_path = os.path.join(root, filename)
            
            try:
                with open(json_file_path, "r", encoding="utf-8") as f:
                    doc = json.load(f)
                
                # Handle duplicate slugs
                original_slug = doc.get("slug", filename.replace(".json", ""))
                slug = original_slug
                counter = 1
                
                while slug in collection_slugs[main_folder]:
                    counter += 1
                    slug = f"{original_slug}_{counter:02d}"
                
                collection_slugs[main_folder][slug] = True
                doc["slug"] = slug
                
                # Add metadata
                doc["imported_at"] = datetime.utcnow()
                doc["source_file"] = json_file_path
                doc["folder_path"] = relative_path
                
                # Insert document
                collection.insert_one(doc)
                print(f"✓ Inserted: {main_folder} -> {doc.get('title', filename)} (slug: {slug})")
                    
            except json.JSONDecodeError as e:
                print(f"✗ Error reading {json_file_path}: {e}")
            except Exception as e:
                print(f"✗ Error inserting {json_file_path}: {e}")

print("\n✓ All documents imported to MongoDB!")
print(f"\nDatabase: {DB_NAME}")
print(f"Collections created:")
for collection_name in db.list_collection_names():
    count = db[collection_name].count_documents({})
    print(f"  - {collection_name}: {count} documents")
