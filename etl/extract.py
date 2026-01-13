import pandas as pd
import boto3
from io import StringIO

s3 = boto3.client("s3")

def extract_reviews(bucket_name: str, object_key: str) -> pd.DataFrame:
    """
    Extract CSV directly from S3.
    """
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_content = response["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(csv_content))
    return df
