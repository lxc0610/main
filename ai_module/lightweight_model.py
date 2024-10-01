# lightweight_model.py

def compress_model(model_path):
    """
    Compress the model to reduce size.
    Args:
        model_path (str): Path to the model.

    Returns:
        str: Path to the compressed model.
    """
    # Placeholder for model compression code
    compressed_model_path = model_path.replace(".joblib", "_compressed.joblib")
    print(f"Model compressed to {compressed_model_path}")
    return compressed_model_path
