import autogen
import os
import requests
import json

# Load LLM config
config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-2.5-flash-preview-05-20"], # Using a model with cost calculation support
    },
    
)

llm_config = {
    "config_list": config_list_gemini,
    "cache_seed": 42,    
}
BASE_URL = "https://api.restful-api.dev/objects"
# Define the function to get objects from the API
def get_all_objects():
    """
    Fetches all objects from the https://api.restful-api.dev/objects API.
    Returns the JSON response as a string.
    """

    try:
        response = requests.get(BASE_URL)
        response.raise_for_status() # Raise an exception for HTTP errors
        return json.dumps(response.json(), indent=2)
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {e}"

def get_object_by_id(object_id: str):
    """
    Fetches a specific object from the https://api.restful-api.dev/objects API by its ID.
    Args:
        object_id (str): The ID of the object to retrieve.
    Returns:
        The JSON response as a string, or an error message.
    """
    url = f"https://api.restful-api.dev/objects/{object_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return json.dumps(response.json(), indent=2)
    except requests.exceptions.RequestException as e:
        return f"Error fetching object with ID {object_id}: {e}"

def add_object(name: str, data: dict):
    """
    Adds a new object to the https://api.restful-api.dev/objects API.

    Args:
        name (str): The name of the new object.
        data (dict): A dictionary containing the data for the new object.
                     Example: {'year': 2023, 'price': 123.45}
    Returns:
        dict: The JSON response from the API containing the new object's details, including its ID, or an error dictionary.
    """
    payload = {"name": name, "data": data}
    try:
        response = requests.post(BASE_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def update_object(object_id: str, name: str, data: dict):
    """Updates an existing object."""
    payload = {"name": name, "data": data}
    try:
        response = requests.put(f"{BASE_URL}/{object_id}", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
def partially_update_object(object_id: str, data: dict):
    """Partially updates an object."""
    try:
        response = requests.patch(f"{BASE_URL}/{object_id}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def delete_object(object_id: str):
    """Deletes an object by ID."""
    try:
        response = requests.delete(f"{BASE_URL}/{object_id}")
        response.raise_for_status()
        return {"message": f"Object {object_id} deleted successfully."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}    
def partially_update_object(object_id: str, data: dict):
    """Partially updates an object."""
    try:
        response = requests.patch(f"{BASE_URL}/{object_id}", json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
       
# 1. Create a UserProxyAgent that can execute functions
user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False, # Disable general code execution for this example, only rely on registered functions
)

# 2. Create an AssistantAgent and register the functions
assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config,
    system_message="""You are a helpful AI assistant.
    You have access to functions to interact with the restful-api.dev/objects API.
    Use the 'get_all_objects()' function to retrieve all objects.
    Use the 'get_object_by_id(object_id: str)' function to retrieve a specific object.
    Use the 'add_object(name: str, data: dict)' function to add a new object. `data` should be a dictionary (e.g., {'year': 2023, 'price': 1000}).
    When you have successfully completed the requested tasks, say "TERMINATE".
    """
)

# Register the functions with the user_proxy. This makes the functions callable by the assistant
# when the assistant sends a message indicating it wants to call a function.
user_proxy.register_for_execution(assistant, get_all_objects)
user_proxy.register_for_execution(assistant, get_object_by_id)
user_proxy.register_for_execution(assistant, add_object)
user_proxy.register_for_execution(assistant, update_object)
user_proxy.register_for_execution(assistant, partially_update_object)
user_proxy.register_for_execution(assistant, delete_object)

# 3. Initiate the chat
user_proxy.initiate_chat(
    assistant,
    message="Add a new object with atrtibute name 'My Test Object' and data {'year': 2023, 'price': 123.45, 'CPU model': 'Intel Core i9'} and then Please list all objects from the API."
    )