# Veeva Vault SDK

A Python SDK for the Veeva Vault API.

## Installation

```sh
pip install veeva-vault-sdk
```

## Usage

```python
import veeva

# Configure API key authorization: APIKeyHeader
configuration = veeva.Configuration(
    host="https://my-veeva-domain.veevavault.com/api/v25.1",
    api_key={'Authorization': 'YOUR_API_KEY'}
)

# Create an instance of the API class
with veeva.ApiClient(configuration) as api_client:
    api_instance = veeva.VeevaApi(api_client)
    try:
        # Retrieve API Versions
        api_response = api_instance.api_get()
        pprint(api_response)
    except veeva.ApiException as e:
        print("Exception when calling VeevaApi->api_get: %s\n" % e)
```

## Documentation

Full documentation for the API can be found in the `docs` directory.
