import autogen
# import os
# from dotenv import load_dotenv

# It's good practice to set up your API key from environment variables
# import os
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
# Load environment variables from .env file if available
# load_dotenv()

# Get your Google API key from environment variables
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# if not GOOGLE_API_KEY:
#     raise ValueError(
#         "Google API key not found. Set the GOOGLE_API_KEY environment variable "
#         "or ensure it's in your .env file."
#     )
# Configuration for the LLM (replace with your actual API key)

config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-2.5-flash-preview-05-20"], # Using a model with cost calculation support
    },
)

assistant = autogen.AssistantAgent(
    name="Coder",
    llm_config={"config_list": config_list_gemini},
)

user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "coding", "use_docker": False},
    llm_config={"config_list": config_list_gemini},
)

print("\n--- Two-Agent Chat Example ---")
# Initiate the chat
chat_result = user_proxy.initiate_chat(
    assistant,
    message="Write a Python function to calculate the factorial of a number. Make sure to include docstrings and type hints.",
)

# You can access the conversation history from chat_result
print(chat_result.chat_history)