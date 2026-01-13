from etl.extract import extract_reviews
from etl.transform import transform_reviews
from etl.load import load_to_s3
from datetime import datetime

RAW_BUCKET = "rayban-etl-raw-steve"
RAW_KEY = "reviews.csv"

PROCESSED_BUCKET = "rayban-etl-processed-steve"
PROCESSED_KEY = "rayban_reviews_clean.csv"

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
