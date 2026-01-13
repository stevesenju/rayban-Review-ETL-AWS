import pandas as pd

def load_to_csv(df: pd.DataFrame, output_path: str):
    df.to_csv(output_path, index=False)