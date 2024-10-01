# model_evaluation.py

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the test data.
    Args:
        model (object): Trained model object.
        X_test (array-like): Test features.
        y_test (array-like): True test values.

    Returns:
        dict: Evaluation metrics.
    """
    score = model.score(X_test, y_test)
    return {"accuracy": score}
