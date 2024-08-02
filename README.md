# Distributed System Design: Data Streaming Pipeline Project


## Overview
This project involves designing a data streaming pipeline using Google Cloud Functions. The aim is to stream all the data present in the files of our dataset as soon as they are uploaded to Google Cloud Storage to the appropriate tables in BigQuery.

## Components
The system consists of three components of GCP:
1. **Google Cloud Functions**: The primary focus of this project.
2. **Google Cloud Storage (GCS)**: Used to upload our dataset files and store analysis results.
3. **BigQuery**: Where our data ends up and where we perform queries to clean and prepare data for analysis.

## Cloud Functions
We have created and deployed four cloud functions:
1. To stream data from GCS to BigQuery.
2. To perform SQL operations, extract user review data, and generate word clouds.
3. To test the scalability, concurrency, and openness of our system.

## Dataset
- **Amazon Books Review**: This dataset has around 2.9 GB of data that we aim to process.

## Features Demonstrated
1. **Scalability**: Achieved by setting the maximum number of instances in Google Cloud Functions.
2. **Concurrency**: Gen 1 functions handle one request per instance; Gen 2 can handle up to 1000 requests per instance.
3. **Data Sharing**
4. **Openness**

## Methodology
The project primarily uses Google Cloud Functions to set up an information streaming pipeline to Extract, Transform, and Load (ETL) data from Google Cloud Storage to BigQuery. The cloud function has an event trigger, which is a ‘cloud storage’ type trigger set up for creating/finalizing files in the specified bucket.

- **Instance Memory**: 256 MB for each instance (modifiable).
- **Entry Point**: A defined method for code execution.

### Steps
1. Create a bucket to upload dataset files.
2. Create datasets and tables in BigQuery.
3. Develop cloud functions to trigger specific events.

### Testing
- Deployed functions are tested via Google Cloud Console.
- Dataset “Amazon Book Reviews” files uploaded to the bucket.
- Logs provide detailed execution results.

### Concurrency Testing
A Python program was created using multiprocessing to send concurrent requests to the cloud function’s trigger URI. This demonstrated the automatic creation of instances to handle requests.

## Preprocessing Queries
**Books_rating.csv:**
- Replace null user reviews with "NIL".
- Replace null values in the price column with 0.

**books_data.csv:**
- Replace null descriptions with "No description".
- Replace null authors with "Anonymous".
- Replace missing preview links with "no link available".
- Replace missing publisher information with "no info".
- Replace missing published dates with "no info".
- Replace missing info links with "no info".
- Replace missing categories with "not defined".
- Replace null ratingsCount with 0.

## Scalability in ETL Pipeline
Scalability refers to the system's ability to handle increasing workloads. GCP allows scaling by adjusting resources, such as increasing memory or the number of instances.

### Generation Differences
- **1st Generation Functions**: Each instance handles one request; up to 3000 instances can be deployed.
- **2nd Generation Functions**: Each instance can handle up to 1000 concurrent requests.

### Auto-Scaling
Google Cloud Functions automatically scale by deploying multiple instances based on request volume, known as auto-scaling behaviour.

## Conclusion
This project showcases the effective use of Google Cloud Functions, Cloud Storage, and BigQuery to create a scalable, concurrent, and open data streaming pipeline. The system efficiently processes large datasets by automatically scaling and handling multiple requests concurrently.

