import os
import base64
import json
import re
from openai import AzureOpenAI

AZURE_OPENAI_RESOURCE = os.environ["AZURE_OPENAI_RESOURCE"]
AZURE_OPENAI_KEY = os.environ["AZURE_OPENAI_KEY"]

EMBEDDINGS_AZURE_OPENAI_RESOURCE = os.environ["EMBEDDINGS_AZURE_OPENAI_RESOURCE"]
EMBEDDINGS_AZURE_OPENAI_KEY = os.environ["EMBEDDINGS_AZURE_OPENAI_KEY"]

AZURE_AI_SEARCH_ENDPOINT = os.environ["AZURE_AI_SEARCH_ENDPOINT"]
AZURE_AI_SEARCH_KEY = os.environ["AZURE_AI_SEARCH_KEY"]
AZURE_AI_SEARCH_INDEX_NAME = os.environ["AZURE_AI_SEARCH_INDEX_NAME"]

azure_openai_client = AzureOpenAI(
            api_version="2024-06-01",
            api_key=AZURE_OPENAI_KEY,
            azure_endpoint=f"https://{AZURE_OPENAI_RESOURCE}.openai.azure.com/",
        )

messages = [
    {
      "role": "system",
      "content": "You are sports store assistant. you only speak about the products available to you in the context."
    },
]

extra_body = {
  "data_sources": [
    {
      "type": "azure_search",
      "parameters": {
        "endpoint": AZURE_AI_SEARCH_ENDPOINT,
        "authentication": {
            "key": AZURE_AI_SEARCH_KEY,
            "type": "api_key"
        },
        "key": AZURE_AI_SEARCH_KEY,
        "index_name": AZURE_AI_SEARCH_INDEX_NAME,
        "top_n_documents": 3,
        "query_type": "vector",
        "embedding_dependency": {
            "endpoint": f"https://{EMBEDDINGS_AZURE_OPENAI_RESOURCE}.openai.azure.com/openai/deployments/text-embedding-3-small/embeddings",
            "type": "endpoint",
            "authentication": {
                "key": EMBEDDINGS_AZURE_OPENAI_KEY,
                "type": "api_key"
            }
        },
        "fields_mapping": {
            "vector_fields": ["description_vector"],
            "content_fields": ["name", "category", "price", "description"],
            "title_field": "name"
        }
      },
    }
  ],
}

try:
    while True:
        user_input = input("> ")
        print()
        messages.append({
                "role": "user",
                "content": user_input
            })

        full_response = ''
        stream = azure_openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=512,
            extra_body=extra_body,
            stream=True
        )

        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="")

        if full_response:
            messages.append({
                "role": "assistant",
                "content": full_response
            })

        print()
        print()

except KeyboardInterrupt:
    print("\nChat ended.")