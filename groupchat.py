import autogen

# Configuration for the LLM (replace with your actual API key)
config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-2.5-flash-preview-05-20"], # Using a model with cost calculation support
    },
)


# Create agents for the group chat
product_manager = autogen.AssistantAgent(
    name="ProductManager",
    system_message="You are a product manager. You define requirements and review solutions.",
    llm_config={"config_list": config_list_gemini},
)

software_engineer = autogen.AssistantAgent(
    name="SoftwareEngineer",
    system_message="You are a software engineer. You implement solutions based on requirements.",
    llm_config={"config_list": config_list_gemini},
)

qa_engineer = autogen.AssistantAgent(
    name="QAEgineer",
    system_message="You are a QA engineer. You test the implemented solutions.",
    llm_config={"config_list": config_list_gemini},
)

group_chat_manager = autogen.GroupChatManager(
    groupchat=autogen.GroupChat(
        agents=[product_manager, software_engineer, qa_engineer],
        messages=[],
        max_round=10
    ),
    llm_config={"config_list": config_list_gemini},
)

user_reporter = autogen.UserProxyAgent(
    name="UserReporter",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "group_chat_tasks", "use_docker": False},
    llm_config={"config_list": config_list_gemini},
)

print("\n--- Group Chat Example ---")
user_reporter.initiate_chat(
    group_chat_manager,
    message="We need a new feature: a simple Python script that takes two numbers and returns their sum. The software engineer should write it, and the QA engineer should test it.",
)