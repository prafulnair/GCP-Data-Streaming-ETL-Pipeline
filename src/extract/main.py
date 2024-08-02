"""
Module: connection_bg

This module contains a function to query BigQuery and extract reviews for a specific book title from a dataset.

Function:
    - connection_bg(request): Queries BigQuery for user reviews of the book with the title 'Mere Christianity' and returns the results.

Dependencies:
    - google-cloud-bigquery: Required to interact with Google BigQuery.

Usage:
    - This function is designed to be used as a Google Cloud Function. It responds to HTTP requests and interacts with BigQuery to extract data.

Parameters:
    - request (flask.Request): An HTTP request object. It is used here to define the context in which the function is invoked. 

Returns:
    - str: A string containing user reviews for the book 'Mere Christianity'. If there are more than 10 reviews, only the first 10 reviews are included.

Details:
    1. The function initializes a BigQuery client.
    2. It constructs and executes a query to select reviews for the book titled 'Mere Christianity' from the dataset `unique-perigee-371022.a_dataset.correct_csv`.
    3. The results are processed, and the first 10 reviews (or fewer if there are less than 10) are concatenated into a single string.
    4. The concatenated review text is returned as the function's response.

Example:
    - A request to this function will trigger a query to BigQuery, and the function will return a string of reviews for 'Mere Christianity'.

Notes:
    - Ensure that the BigQuery client is properly authenticated and has access to the dataset.
    - The dataset and table names used in the query should be updated to match the actual dataset and table names in your BigQuery instance.
"""

from google.cloud import bigquery

def connection_bg(request):
        """
    Queries BigQuery for user reviews of the book titled 'Mere Christianity'.

    Args:
        request (flask.Request): An HTTP request object.

    Returns:
        str: A concatenated string of user reviews for the book 'Mere Christianity'.
    """
  
    client = bigquery.Client()
    #https://us-central1-unique-perigee-371022.cloudfunctions.net/extract_info
    query = """
    SELECT text as Reviews
    FROM `unique-perigee-371022.a_dataset.correct_csv`
    WHERE Title = 'Mere Christianity'
    """

    job = client.query(query)

    print("The extracted user review for given title is :")

    result = " "
    limit = 10

    for r in job:
        r = str(r)
        result = result + r
        limit = limit -1 
        if limit < 0:
            break

    return result
