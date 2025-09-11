"""
A user-friendly client for interacting with the Veeva Vault API.
"""
from veeva.api.veeva_api import VeevaApi
from veeva.api_client import ApiClient
from veeva.configuration import Configuration
from veeva.models.auth_discovery_request import AuthDiscoveryRequest


class VaultClient:
    """
    The main client for a Veeva Vault API.

    This client provides a high-level, convenient interface for performing
    common operations like authentication, querying, and document management.
    """

    def __init__(self, vault_dns: str):
        """
        Initializes the VaultClient.

        :param vault_dns: The DNS of the vault (e.g., "your-vault.veevavault.com").
        """
        self.configuration = Configuration(host=f"https://{vault_dns}")
        self.api_client = ApiClient(configuration=self.configuration)
        self.veeva_api = VeevaApi(api_client=self.api_client)
        self.session_id = None

    def discover_authentication(self, username: str):
        """
        Discovers the available authentication methods for a user.

        :param username: The username to discover authentication methods for.
        :return: The authentication discovery response.
        """
        auth_discovery_request = AuthDiscoveryRequest(username=username)
        return self.veeva_api.auth_discovery_post(body=auth_discovery_request)

    def authenticate(self, username, password):
        """
        Authenticates with the Veeva Vault and stores the session ID.

        :param username: The username for authentication.
        :param password: The password for authentication.
        :return: True if authentication is successful, False otherwise.
        """
        response = self.veeva_api.auth_post(username=username, password=password)
        if response.response == "SUCCESS":
            self.session_id = response.session_id
            # Update the ApiClient's default header with the session ID
            self.api_client.set_default_header("Authorization", self.session_id)
            return True
        return False

    def query(self, vql: str):
        """
        Executes a VQL query.

        :param vql: The VQL query string.
        :return: The query response data.
        """
        return self.veeva_api.query_vql_query_get(q=vql)

    def create_document(self, file_path: str, doc_attributes: dict):
        """
        Creates a new document in Vault.

        :param file_path: The local path to the file.
        :param doc_attributes: A dictionary of document attributes (fields).
        :return: The response from the API.
        """
        import json
        return self.veeva_api.objects_documents_post(
            post_params=[('json', json.dumps(doc_attributes))],
            files={'file': file_path}
        )

    def retrieve_document(self, doc_id: int):
        """
        Retrieves a single document by its ID.

        :param doc_id: The ID of the document to retrieve.
        :return: The document metadata.
        """
        return self.veeva_api.objects_documents_doc_id_get(doc_id=doc_id)

    def update_document(self, doc_id: int, doc_attributes: dict):
        """
        Updates an existing document.

        :param doc_id: The ID of the document to update.
        :param doc_attributes: A dictionary of document attributes to update.
        :return: The response from the API.
        """
        import json
        return self.veeva_api.objects_documents_doc_id_put(
            doc_id=doc_id,
            body=json.dumps(doc_attributes)
        )
