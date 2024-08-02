from google.cloud import bigquery


def main(event,context):
   """
    Load CSV data from Google Cloud Storage (GCS) into BigQuery tables.

    Args:
        event (dict): Event data passed by the Cloud Function trigger.
        context (google.cloud.functions.Context): Metadata about the event.

    Returns:
        str: Success message indicating that the data has been loaded into BigQuery tables.

    Raises:
        Exception: Prints error messages if the loading process fails for either file.

    This function performs the following tasks:
    1. Initializes a BigQuery client.
    2. Defines configurations for loading two CSV files into separate BigQuery tables.
    3. Attempts to load the first CSV file (`Books_rating.csv`) from GCS into the corresponding BigQuery table.
       - Configures the schema to match the CSV file structure.
       - Handles any errors that occur during this process.
    4. Attempts to load the second CSV file (`books_data.csv`) from GCS into the other BigQuery table.
       - Configures the schema to match the CSV file structure.
       - Handles any errors that occur during this process.
    5. Prints the number of rows loaded and the table name if successful, or an error message if not.

    Example usage:
        The function is designed to be triggered by a Cloud Function event.
    """
  # Construct a BigQuery client object.
  client = bigquery.Client()

  # TODO(developer): Set table_id to the ID of the table to create.
  table_id_1 = "a_dataset.my_table"
  table_id_2 = "a_dataset.correct_csv"

  config_1 = bigquery.LoadJobConfig(
      schema=[

            bigquery.SchemaField("Title","STRING"),
            bigquery.SchemaField("description","STRING"),
            bigquery.SchemaField("authors","STRING"),
            bigquery.SchemaField("image","STRING"),
            bigquery.SchemaField("previewLink","STRING"),
            bigquery.SchemaField("publisher","STRING"),
            bigquery.SchemaField("publishedDate","STRING"),
            bigquery.SchemaField("infoLink","STRING"),
            bigquery.SchemaField("categories","STRING"),
            bigquery.SchemaField("ratingsCount","STRING"),
      ],
      skip_leading_rows=1,
      # The source format defaults to CSV, so the line below is optional.
      source_format=bigquery.SourceFormat.CSV,
  )
  config_2 = bigquery.LoadJobConfig(
      schema = [
          bigquery.SchemaField("Id","STRING"),
          bigquery.SchemaField("Title","STRING"),
          bigquery.SchemaField("Price","FLOAT"),
          bigquery.SchemaField("User_id","STRING"),
          bigquery.SchemaField("profileName","STRING"),
          bigquery.SchemaField("helpfulness","STRING"),
          bigquery.SchemaField("score","FLOAT"),
          bigquery.SchemaField("time","STRING"),
          bigquery.SchemaField("summary","STRING"),
          bigquery.SchemaField("text","STRING"),
      ],
      skip_leading_rows = 1,
      source_format = bigquery.SourceFormat.CSV,
  )

  job_config_1 = config_1
  job_config_2 = config_2
  
  uri_1 = "gs://test-functionn/books_data.csv"
  uri_2 = "gs://test-functionn/Books_rating.csv"
  filename_1 = "books_data.csv"
  filename_2 = "Books_rating.csv"

  try:
      load_job_2 = client.load_table_from_uri(
          uri_2, table_id_2, job_config = job_config_2
      )
      load_job_2.result()
      destination_table2 = client.get_table(table_id_2)
      print("Loaded {} ROWS to {} table.".format(destination_table2.num_rows,table_id_2))
      return "Loaded successfully" 
  except:
      print("No file name {} loaded yet. Please wait".format(filename_2))

  try:
      load_job_1 = client.load_table_from_uri(
          uri_1, table_id_1, job_config = job_config_1
      )
      load_job_1.result()
      destination_table1 = client.get_table(table_id_1)
      print("Loaded {} ROWS to {} table.".format(destination_table1.num_rows,table_id_1))
      return "Loaded successfully"
  except:
      print("No file name {} loaded yet. Please wait".format(filename_1))

  
