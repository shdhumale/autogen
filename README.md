# autogen
This repo shows the python code for using Autogen AI framework.
---

````markdown
AutoGen
Overview
AutoGen is a framework designed to simplify the creation and management of AI agents for multi-agent workflows. It provides a modular and extensible platform for building conversational AI systems, leveraging large language models (LLMs), tools, and human-in-the-loop interactions. This project is a fork of the original Microsoft AutoGen repository, with custom enhancements and modifications tailored for specific use cases.
Features

Multi-Agent Workflows: Build and orchestrate complex agent interactions with support for diverse conversation patterns.
Customizable Agents: Create agents with configurable LLMs, tools, and system messages for tailored functionality.
Extensible Architecture: Leverage a layered design with Core and AgentChat APIs for flexibility and rapid prototyping.
Cross-Language Support: Supports Python and .NET, with plans for additional language interoperability.
Community Extensions: Integrate with built-in and third-party extensions for enhanced capabilities.
AutoGen Studio: A low-code interface for prototyping multi-agent systems (not production-ready).

Installation
To get started with AutoGen, ensure you have Python 3.10 or later installed. Follow these steps:

Clone the Repository:
git clone https://github.com/shdhumale/autogen.git
cd autogen


Install Dependencies:
pip install -U "autogen-agentchat" "autogen-ext[openai]"


Optional: Install AutoGen Studio:
pip install -U "autogenstudio"
autogenstudio ui --port 8080 --appdir ./myapp

Open your browser and navigate to http://localhost:8080 to use the AutoGen Studio interface.


Usage
Below is a basic example of creating a simple information validation workflow with two agents using the AutoGen framework:
from autogen import ConversableAgent, LLMConfig

# Define LLM configuration (requires OPENAI_API_KEY environment variable)
llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini")

# Create an assistant agent
assistant = ConversableAgent(
    name="assistant",
    system_message="You are an assistant that responds concisely.",
    llm_config=llm_config
)

# Create a fact-checking agent
fact_checker = ConversableAgent(
    name="fact_checker",
    system_message="You are a fact-checking assistant.",
    llm_config=llm_config
)

# Initiate a chat between agents
assistant.initiate_chat(
    fact_checker,
    message="Verify the accuracy of the statement: The moon is made of cheese."
)

For more examples, check the notebooks directory.
Contributing
We welcome contributions to enhance AutoGen! To get started:

Review the CONTRIBUTING.md file for guidelines.
Join our Discord server for real-time discussions.
Check the project roadmap for current priorities.
Submit issues or pull requests with the proj-studio tag for AutoGen Studio-related contributions.

License
This project is licensed under the MIT License for the original code from microsoft/autogen (see LICENSE_original_MIT). Modifications and additions in this fork are licensed under the Apache License, Version 2.0 (see LICENSE).
Acknowledgments

Built upon the original AutoGen project by Microsoft.
Contributions from the open-source community and collaborators from various organizations.

Contact
For questions or support, reach out via:

GitHub Discussions
Discord
Email: support@ag2.ai
