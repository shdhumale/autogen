import autogen

# Configuration for the LLM (replace with your actual API key)
config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-2.5-flash-preview-05-20"], # Using a model with cost calculation support
    },
)

# Outer agents
ceo = autogen.AssistantAgent(
    name="CEO",
    system_message="You are the CEO. You delegate tasks to your team.",
    llm_config={"config_list": config_list_gemini},
)

project_manager = autogen.AssistantAgent(
    name="ProjectManager",
    system_message="You are a project manager. You oversee project execution and report to the CEO.",
    llm_config={"config_list": config_list_gemini},
)

# Inner agents (for a sub-task)
developer = autogen.AssistantAgent(
    name="Developer",
    system_message="You are a developer. You write code.",
    llm_config={"config_list": config_list_gemini},
)

tester = autogen.AssistantAgent(
    name="Tester",
    system_message="You are a tester. You test the code.",
    llm_config={"config_list": config_list_gemini},
)

user_initiator = autogen.UserProxyAgent(
    name="UserInitiator",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "nested_chats", "use_docker": False},
    llm_config={"config_list": config_list_gemini},
)

# Create a group chat for the development team (inner chat)
dev_team_group_chat = autogen.GroupChat(
    agents=[developer, tester],
    messages=[],
    max_round=5
)
dev_team_manager = autogen.GroupChatManager(
    groupchat=dev_team_group_chat,
    llm_config={"config_list": config_list_gemini},
)

print("\n--- Nested Chat Example ---")
# CEO initiates a chat with the Project Manager
ceo.initiate_chat(
    project_manager,
    message="We need a new simple 'hello world' script. Project Manager, please handle this with the development team.",
    # This is where the nested chat happens: Project Manager initiates a chat with the dev_team_manager
    # In a real scenario, the Project Manager's response would trigger the sub-chat.
    # For demonstration, we'll simulate the Project Manager's action.
    callback=lambda manager, messages, sender, config: dev_team_manager.initiate_chat(
        sender,
        message="Okay, Developer and Tester, let's create a 'hello world' Python script.",
    )
)

# The user_initiator can then chat with the ProjectManager to get updates or
# to trigger the entire process.
user_initiator.initiate_chat(
    ceo,
    message="Start a project to create a Python script that just prints 'Hello, World!'",
)