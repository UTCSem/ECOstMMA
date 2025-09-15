
# Placeholder for ETL / feature engineering pipeline for MMA analytics
import pandas as pd

def extract_features(df):
    # Example: compute strikes per minute
    df = df.copy()
    if 'fight_minutes' in df.columns and 'strikes' in df.columns:
        df['strikes_per_min'] = df['strikes'] / df['fight_minutes'].replace({0:1})
    return df

if __name__ == '__main__':
    print('Run your ETL here')
