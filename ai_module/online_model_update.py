# online_model_update.py
from sklearn.linear_model import LinearRegression
import joblib

def update_model(model_path, new_data, new_target):
    """
    Update an existing model with new data.
    Args:
        model_path (str): Path to the saved model.
        new_data (array-like): New input features.
        new_target (array-like): New target values.

    Returns:
        str: Path to the updated model.
    """
    model = joblib.load(model_path)
    model.fit(new_data, new_target)
    joblib.dump(model, model_path)
    return model_path
