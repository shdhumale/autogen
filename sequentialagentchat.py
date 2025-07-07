import autogen

# Configuration for the LLM (replace with your actual API key)
config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-2.5-flash-preview-05-20"], # Using a model with cost calculation support
    },
)

planner = autogen.AssistantAgent(
    name="Planner",
    system_message="You are a task planner. You will break down a request into smaller, manageable steps.",
    llm_config={"config_list": config_list_gemini},
)

executor = autogen.AssistantAgent(
    name="Executor",
    system_message="You are a task executor. You will execute the steps provided by the planner.",
    llm_config={"config_list": config_list_gemini},
)

user_client = autogen.UserProxyAgent(
    name="UserClient",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "sequential_tasks", "use_docker": False},
    llm_config={"config_list": config_list_gemini},
)

print("\n--- Sequential Chat Example ---")
# User initiates with the Planner
chat_result = user_client.initiate_chat(
    planner,
    message="I need to calculate the sum of numbers from 1 to 100 and then print the result.",
    summary_method="last_msg",
)

# Planner's response (the plan) is then sent to the Executor
# In a real-world scenario, you might parse the plan from chat_result
# For simplicity, we'll manually send a message that the planner might generate.
print("\n--- Executor takes over from Planner ---")
executor.initiate_chat(
    user_client, # The executor can respond to the user_client if needed.
    message=f"Execute the following plan: '{chat_result.summary}'",
)

# You can access the conversation history from chat_result
print(executor.chat_history)