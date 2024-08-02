import unittest
from unittest.mock import patch, MagicMock
from wordcloud_generator import connection_bg

class TestWordCloudGenerator(unittest.TestCase):

    @patch('google.cloud.bigquery.Client')
    @patch('google.cloud.storage.Client')
    @patch('matplotlib.pyplot.savefig')
    def test_connection_bg(self, mock_savefig, MockStorageClient, MockBigQueryClient):
        # Mock BigQuery client
        mock_bq_client = MockBigQueryClient.return_value
        mock_query_job = MagicMock()
        mock_query_job.__iter__.return_value = iter([MagicMock(text="Sample review text")])
        mock_bq_client.query.return_value = mock_query_job

        # Mock Cloud Storage client
        mock_storage_client = MockStorageClient.return_value
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_bucket.blob.return_value = mock_blob
        mock_storage_client.get_bucket.return_value = mock_bucket

        request = {}
        result = connection_bg(request)

        self.assertIn('Successfully generated WordCloud image', result)
        mock_bq_client.query.assert_called()
        mock_storage_client.get_bucket.assert_called()
        mock_blob.upload_from_file.assert_called()

if __name__ == '__main__':
    unittest.main()
