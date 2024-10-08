import pandas as pd
import json

def load_metadata(metadata_path):
    with open(metadata_path, 'r') as file:
        return json.load(file)

metadata = load_metadata("../rag-chat/data/metadata_structured.json")

formatted_data = []
for item in metadata:
    formatted_data.append({
        'id': item['id'],
        'image': item['image_blob_path'],
        'details': f"Name: {item['name']}, Category: {item['category']}, Price: {item['price']}, Description: {item['description']}"
    })

df = pd.DataFrame(formatted_data)

csv_file_path = "../rag-chat/data/products.csv"
df.to_csv(csv_file_path, index=False)