import pandas as pd


def extract_reviews(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df