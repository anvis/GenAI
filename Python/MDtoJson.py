import os
import json
import re
from datetime import datetime

input_dir = "Basics/Linear Algebra"
output_dir = "articlesJson"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()
        
        # Strip leading numbers and underscores
        clean_name = re.sub(r'^[0-9_]+', '', filename.replace(".md", ""))
        
        doc = {
            "title": clean_name.replace("_", " ").title(),
            "slug": clean_name,
            "content": content,
            "tags": [],
            "created_at": datetime.utcnow().isoformat(),
            "source": "GitHub"
        }
        
        # Create a new JSON file for each markdown file
        output_file = os.path.join(output_dir, f"{clean_name}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2)