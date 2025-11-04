# ml_training/data_preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load dataset from CSV."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Handle missing values and remove duplicates."""
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))
    return df

def split_features_labels(df, target):
    """Split into features (X) and label (y)."""
    X = df.drop(columns=[target])
    y = df[target]
    return X, y

def scale_data(X_train, X_test):
    """Standardize features."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler
