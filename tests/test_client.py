import unittest
from unittest.mock import MagicMock, patch
from veeva.client import VaultClient
from veeva.models.auth_discovery_request import AuthDiscoveryRequest

class TestVaultClient(unittest.TestCase):

    def setUp(self):
        self.vault_dns = "test.veevavault.com"
        with patch('veeva.client.VeevaApi') as self.mock_veeva_api_class:
            self.client = VaultClient(self.vault_dns)
            self.mock_veeva_api = self.mock_veeva_api_class.return_value
            self.client.veeva_api = self.mock_veeva_api

    def test_init(self):
        self.assertEqual(self.client.configuration.host, f"https://{self.vault_dns}")
        self.assertIsNotNone(self.client.api_client)
        self.assertIsNotNone(self.client.veeva_api)
        self.assertIsNone(self.client.session_id)

    def test_authenticate_success(self):
        mock_response = MagicMock()
        mock_response.response = "SUCCESS"
        mock_response.session_id = "test_session_id"
        self.mock_veeva_api.auth_post.return_value = mock_response

        result = self.client.authenticate("test_user", "test_password")

        self.assertTrue(result)
        self.assertEqual(self.client.session_id, "test_session_id")
        self.mock_veeva_api.auth_post.assert_called_once_with(username="test_user", password="test_password")
        self.assertEqual(self.client.api_client.default_headers["Authorization"], "test_session_id")

    def test_authenticate_failure(self):
        mock_response = MagicMock()
        mock_response.response = "FAILURE"
        self.mock_veeva_api.auth_post.return_value = mock_response

        result = self.client.authenticate("test_user", "test_password")

        self.assertFalse(result)
        self.assertIsNone(self.client.session_id)

    def test_query(self):
        vql = "SELECT id FROM documents"
        self.client.query(vql)
        self.mock_veeva_api.query_vql_query_get.assert_called_once_with(q=vql)

    def test_create_document(self):
        file_path = "/tmp/test.txt"
        doc_attributes = {"name__v": "Test Document"}

        with patch("builtins.open", unittest.mock.mock_open(read_data=b"test data")) as mock_file:
            self.client.create_document(file_path, doc_attributes)
            self.mock_veeva_api.objects_documents_post.assert_called_once()
            call_args = self.mock_veeva_api.objects_documents_post.call_args
            self.assertIn(('json', '{"name__v": "Test Document"}'), call_args[1]['post_params'])
            self.assertEqual(file_path, call_args[1]['files']['file'])

    def test_retrieve_document(self):
        doc_id = 123
        self.client.retrieve_document(doc_id)
        self.mock_veeva_api.objects_documents_doc_id_get.assert_called_once_with(doc_id=doc_id)

    def test_update_document(self):
        doc_id = 123
        doc_attributes = {"status__v": "Approved"}
        self.client.update_document(doc_id, doc_attributes)
        self.mock_veeva_api.objects_documents_doc_id_put.assert_called_once_with(
            doc_id=doc_id,
            body='{"status__v": "Approved"}'
        )

    def test_discover_authentication(self):
        username = "test_user@veeva.com"
        self.client.discover_authentication(username)
        self.mock_veeva_api.auth_discovery_post.assert_called_once()
        call_args = self.mock_veeva_api.auth_discovery_post.call_args
        self.assertIn('body', call_args[1])
        body_arg = call_args[1]['body']
        self.assertIsInstance(body_arg, AuthDiscoveryRequest)
        self.assertEqual(body_arg.username, username)

if __name__ == '__main__':
    unittest.main()
