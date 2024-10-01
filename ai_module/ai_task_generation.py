# ai_task_generation.py

def generate_ai_task(task_name: str, parameters: dict):
    """
    Generate an AI task based on the given name and parameters.
    Args:
        task_name (str): Name of the task to generate.
        parameters (dict): Parameters for task generation.

    Returns:
        dict: Task details.
    """
    task = {
        "task_name": task_name,
        "parameters": parameters,
        "status": "generated"
    }
    return task
