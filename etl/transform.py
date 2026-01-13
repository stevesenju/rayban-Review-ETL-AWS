import pandas as pd
import re
from datetime import datetime


def clean_html(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<.*?>", "", text)
    return text.strip()


def transform_reviews(df: pd.DataFrame) -> pd.DataFrame:

    df = df.rename(columns={
        "reviewID": "review_id",
        "name": "reviewer_name",
        "date": "review_date",
        "rating": "rating",
        "review": "review_text",
        "title": "review_title",
        "helpful": "helpful_count"
    })


    df["review_date"] = pd.to_datetime(
        df["review_date"],
        errors="coerce"
    ).dt.date

#Normalize
    df["rating"] = df["rating"].astype("Int64")

    df["verified_flag"] = df["verifiedPurchase"].astype(int)

    df["helpful_count"] = (pd.to_numeric(df["helpful_count"], errors="coerce").fillna(0).astype(int))


    df["review_text"] = df["review_text"].apply(clean_html)

    df["review_length"] = df["review_text"].str.len()

    df["country"] = df["country"].str.upper()

    df["processed_at"] = datetime.utcnow()

    final_columns = [
        "review_id",
        "reviewer_name",
        "review_date",
        "rating",
        "verified_flag",
        "helpful_count",
        "is_positive_review",
        "helpfulness_score",
        "review_title",
        "review_text",
        "review_length",
        "country",
        "processed_at"
    ]

    return df[final_columns]
