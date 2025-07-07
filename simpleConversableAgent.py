import autogen


config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gemini-2.5-flash-preview-05-20"], # Using a model with cost calculation support
    },
)

# Create a ConversableAgent configured to use Gemini
assistant = autogen.ConversableAgent(
    name="GeminiAssistant",
    system_message="You are a helpful AI assistant powered by Google Gemini.",
    llm_config={"config_list": config_list_gemini},
    human_input_mode="NEVER", # Set to "ALWAYS" or "TERMINATE" for human interaction
)

# Create a UserProxyAgent to initiate the conversation
user_proxy = autogen.ConversableAgent(
    name="UserProxy",
    human_input_mode="ALWAYS", # Allows human input to drive the conversation
    llm_config=False, # User proxy doesn't need an LLM
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
)

# Initiate the chat
chat_result = user_proxy.initiate_chat(
    assistant,
    message="Tell me a fun fact about the universe.",
)
# You can access the conversation history from chat_result
print(chat_result.chat_history)