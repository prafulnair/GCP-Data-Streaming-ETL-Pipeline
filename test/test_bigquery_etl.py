import unittest
from unittest.mock import patch, MagicMock
from bigquery_etl import main

class TestBigQueryETL(unittest.TestCase):

    @patch('google.cloud.bigquery.Client')
    def test_main_success(self, MockBigQueryClient):
        # Setup mock client and job
        mock_client = MockBigQueryClient.return_value
        mock_load_job = MagicMock()
        mock_load_job.result.return_value = None
        mock_client.load_table_from_uri.return_value = mock_load_job
        mock_client.get_table.return_value = MagicMock(num_rows=100)

        event = {}
        context = {}

        result = main(event, context)

        self.assertEqual(result, "Loaded successfully")
        mock_client.load_table_from_uri.assert_called()
        self.assertEqual(mock_client.load_table_from_uri.call_count, 2)

    @patch('google.cloud.bigquery.Client')
    def test_main_failure(self, MockBigQueryClient):
        # Setup mock client to raise an exception
        mock_client = MockBigQueryClient.return_value
        mock_client.load_table_from_uri.side_effect = Exception("Error loading table")

        event = {}
        context = {}

        result = main(event, context)

        self.assertIn("No file name", result)

if __name__ == '__main__':
    unittest.main()
