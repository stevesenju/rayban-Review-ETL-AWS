from etl.extract import extract_reviews
from etl.transform import transform_reviews
from etl.load import load_to_csv

RAW_PATH = "data\\raw\\reviews.csv"
PROCESSED_PATH = "data\\processed\\reviews_clean.csv"


def main():
    df_raw = extract_reviews(RAW_PATH)
    df_clean = transform_reviews(df_raw)
    load_to_csv(df_clean, PROCESSED_PATH)
    print("ETL completed")


if __name__ == "__main__":
    main()
