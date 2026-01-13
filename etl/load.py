import boto3
from io import StringIO

s3 = boto3.client("s3")

def load_to_s3(df, bucket_name: str, object_key: str):
    """
    Load processed DataFrame directly to S3.
    """
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=csv_buffer.getvalue())
