from etl.extract import extract_reviews
from etl.transform import transform_reviews
from etl.load import load_to_s3
from datetime import datetime

RAW_BUCKET = "raw_bucket_name"  #origin bucket
RAW_KEY = "filename.csv" #raw csv file

PROCESSED_BUCKET = "processed_bucket_name"  #origin bucket
PROCESSED_KEY = "processed_filename.csv" #raw csv file

def main():
    print(f"[{datetime.utcnow()}] Starting ETL pipeline")

    df_raw = extract_reviews(RAW_BUCKET, RAW_KEY)
    print(f"[{datetime.utcnow()}] Extracted {len(df_raw)} records")

    df_clean = transform_reviews(df_raw)
    print(f"[{datetime.utcnow()}] Transformed {len(df_clean)} records")

    load_to_s3(df_clean, PROCESSED_BUCKET, PROCESSED_KEY)
    print(f"[{datetime.utcnow()}] Loaded processed data to S3")

if __name__ == "__main__":
    main()
