'use strict';

 function main (datasetId = 'my_dataset', tableId = 'my_table')  {
  // [START bigquery_load_table_gcs_csv]
  // Import the Google Cloud client libraries
  const {BigQuery} = require('@google-cloud/bigquery');
  const {Storage} = require('@google-cloud/storage');

  // Instantiate clients
  const bigquery = new BigQuery();
  const storage = new Storage();

  /**
   * This sample loads the CSV file at
   * https://storage.googleapis.com/cloud-samples-data/bigquery/us-states/us-states.csv
   *
   * TODO(developer): Replace the following lines with the path to your file.
   */
  const bucketName = 'test-functionn';
  const filename = 'my_table.csv';

  //   const bucketName = 'cloud-samples-data';
  // const filename = 'bigquery/us-states/us-states.csv';

  async function loadCSVFromGCS() {
    // Imports a GCS file into a table with manually defined schema.

    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */

    const datasetId = 'c_dataset';
    const tableId = 'my_table_copy2';

    // Configure the load job. For full list of options, see:
    // https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationLoad
    const metadata = {
      sourceFormat: 'CSV',
      skipLeadingRows: 1,
      schema: {
        fields: [
          {name: 'Title', type: 'STRING'},
          {name: 'description', type: 'STRING'},
          {name: 'authors', type: 'STRING'},
          {name: 'image', type: 'STRING'},
          {name: 'previewLink', type: 'STRING'},
          {name: 'publisher', type: 'STRING'},
          {name: 'publishedDate', type: 'STRING'},
          {name: 'infoLink', type: 'STRING'},
          {name: 'categories', type: 'STRING'},
          {name: 'ratingsCount', type: 'STRING'},

        ],
      },
 
    };

    // Load data from a Google Cloud Storage file into the table
    const [job] = await bigquery
      .dataset(datasetId)
      .table(tableId)
      .load(storage.bucket(bucketName).file(filename), metadata);

    // load() waits for the job to finish
    console.log(`Job ${job.id} completed.`);
  }
  // [END bigquery_load_table_gcs_csv]
  loadCSVFromGCS();
}
main(...process.argv.slice(2));


module.exports.main = main;
