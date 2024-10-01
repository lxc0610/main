# train_ai_model.py
from sklearn.linear_model import LinearRegression
import joblib

def train_model(X, y):
    """
    Train a machine learning model using the provided data.
    Args:
        X (array-like): Features.
        y (array-like): Target values.

    Returns:
        str: Path to the saved model.
    """
    model = LinearRegression()
    model.fit(X, y)
    model_path = "trained_models/model.joblib"
    joblib.dump(model, model_path)
    return model_path
