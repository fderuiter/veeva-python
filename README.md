# Veeva Vault SDK

A Python SDK for the Veeva Vault API, providing a user-friendly interface for common Vault operations.

## Installation

This project uses Poetry for dependency management. To install the necessary dependencies, run:

```sh
poetry install
```

## Getting Started

Here's a quick example of how to authenticate and run a VQL query.

```python
from veeva import VaultClient

# Replace with your Vault's DNS
vault_dns = "your-vault-domain.veevavault.com"

# Initialize the client
client = VaultClient(vault_dns)

# Authenticate
if client.authenticate("your_username", "your_password"):
    print("Authentication successful!")
    print(f"Session ID: {client.session_id}")
else:
    print("Authentication failed.")
    exit()

# Run a VQL query
try:
    vql_query = "SELECT id, name__v FROM documents"
    results = client.query(vql_query)
    print("\nQuery Results:")
    for record in results.data:
        print(f"  - ID: {record.id}, Name: {record.name__v}")
except Exception as e:
    print(f"\nAn error occurred during query: {e}")

```

## Document Management

The `VaultClient` simplifies common document operations.

### Create a Document

To create a new document, you need to provide a path to the file and a dictionary of its attributes.

```python
import os

# Create a dummy file for upload
file_path = "my_document.txt"
with open(file_path, "w") as f:
    f.write("This is the content of my document.")

# Define document attributes
doc_attributes = {
    "name__v": "My New Document",
    "type__v": "general__c",  # Replace with a valid document type in your Vault
    "lifecycle__v": "general_lifecycle__c", # Replace with a valid lifecycle
}

try:
    response = client.create_document(file_path, doc_attributes)
    print("\nDocument created successfully:")
    print(response)
finally:
    # Clean up the dummy file
    os.remove(file_path)
```

### Retrieve a Document

Retrieve a document's metadata by its ID.

```python
try:
    # Assuming a document with ID 123 exists
    doc_id = 123
    document = client.retrieve_document(doc_id)
    print(f"\nRetrieved document {doc_id}:")
    print(document)
except Exception as e:
    print(f"\nAn error occurred while retrieving document: {e}")
```

### Update a Document

Update a document's attributes by its ID.

```python
try:
    # Assuming a document with ID 123 exists
    doc_id = 123
    update_attributes = {
        "description__v": "A new description for the document."
    }
    response = client.update_document(doc_id, update_attributes)
    print(f"\nDocument {doc_id} updated successfully:")
    print(response)
except Exception as e:
    print(f"\nAn error occurred while updating document: {e}")
```
