from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io
from google.cloud import storage

def connection_bg(request):
  """
    Generates and uploads WordCloud images based on text data from BigQuery.

    Args:
        request (flask.Request): HTTP request object. Not used in this function.

    Returns:
        str: Success message indicating that WordCloud images have been generated and uploaded to GCS.

    This function performs the following tasks:
    1. Initializes a BigQuery client.
    2. Defines a list of book titles to retrieve reviews for.
    3. Queries BigQuery for reviews of each book title.
    4. Generates a WordCloud image from the retrieved reviews.
    5. Saves the WordCloud image to a bytes buffer.
    6. Initializes a GCS client and uploads the image to a specified bucket.
    7. Prints progress messages for each generated WordCloud.
    
    Example usage:
        This function is designed to be triggered by an HTTP request in a Cloud Function environment.
    """
    #https://us-central1-unique-perigee-371022.cloudfunctions.net/extract_info
    titles = ['Finnegans Wake','Hotel World', 'Wartime Lies','The Well of Loneliness','Shirley','Mauritius Command']
    cnt=1
    for i in titles:
        client = bigquery.Client()
        query = """
        SELECT text as Reviews
        FROM `unique-perigee-371022.b_dataset.correct_csv_copy`
        WHERE Title = '"""+i+"""'"""

        job = client.query(query)

        print("The extracted user review for given title is :")

        result = " "
        # limit = 10

        for r in job:
            r = str(r)
            result = result + r
            # limit = limit -1 
            # if limit < 0:
            #     break
        
        wordcloud = WordCloud().generate(result)

    # Display the generated image:
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        fig_to_upload = plt.gcf()

        # Save figure image to a bytes buffer
        buf = io.BytesIO()
        fig_to_upload.savefig(buf, format='png')

        # init GCS client and upload buffer contents
        client = storage.Client()
        bucket = client.get_bucket('test-functionn')
        blob = bucket.blob('logs/20190116-195604/wordcloud'+str(cnt)+'.png')  
        blob.upload_from_file(buf, content_type='image/png', rewind=True)

        print("Wordcloud generated"+str(cnt))
        cnt+=1

    return f'Successfully generated WordCloud image, saved in the bucket'
