import os
import json
import re
from datetime import datetime

input_dir = "."
output_base_dir = "articlesJson"

# Create base output directory if it doesn't exist
os.makedirs(output_base_dir, exist_ok=True)

# Recursively walk through all directories
for root, dirs, files in os.walk(input_dir):
    # Skip the output directory and other irrelevant directories
    dirs[:] = [d for d in dirs if d not in [output_base_dir, '.git', '__pycache__', '.venv']]
    
    for filename in files:
        if filename.endswith(".md"):
            input_file_path = os.path.join(root, filename)
            
            with open(input_file_path, "r", encoding="utf-8") as f:
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
            
            # Create corresponding output directory structure
            relative_path = os.path.relpath(root, input_dir)
            if relative_path == ".":
                output_dir = output_base_dir
            else:
                output_dir = os.path.join(output_base_dir, relative_path)
            
            os.makedirs(output_dir, exist_ok=True)
            
            # Create a new JSON file for each markdown file
            output_file = os.path.join(output_dir, f"{clean_name}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(doc, f, indent=2)