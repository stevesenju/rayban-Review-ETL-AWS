## Ray-Ban Reviews ETL (AWS-Ready)

A server-ready ETL pipeline for Amazon Ray-Ban product reviews.
It extracts raw CSV data from an S3 bucket, cleans and transforms it using Python & Pandas, and writes the processed dataset back to another S3 bucket.

This pipeline is designed to run on AWS EC2  with an IAM role for secure, credentials-free S3 access.

## Features

Extract raw reviews directly from S3

Transform data: clean missing values, normalize ratings, and compute helpfulness

Load processed data back to S3

Fully AWS-ready — runs on EC2 with IAM roles

Free-tier friendly

## Dependencies

boto3 — AWS SDK for Python

pandas — Data manipulation & cleaning

## Future Improvements

Schedule automatically with AWS Lambda + EventBridge

Add logging and notifications for each run

Extend to multiple product datasets
