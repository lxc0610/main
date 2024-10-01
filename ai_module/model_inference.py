# model_inference.py
import joblib
import numpy as np

def load_model(model_path):
    """
    Load the trained model from the given path.
    Args:
        model_path (str): Path to the saved model.

    Returns:
        Model: Loaded model object.
    """
    return joblib.load(model_path)

def predict(model, input_data):
    """
    Make a prediction using the loaded model.
    Args:
        model (object): Trained model object.
        input_data (array-like): Input features.

    Returns:
        array: Prediction results.
    """
    return model.predict(np.array(input_data).reshape(1, -1))
