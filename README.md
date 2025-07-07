# autogen
This repo shows the python code for using Autogen AI framework.
---

````markdown
# AutoGen 🧠

A Python framework for building **agentic AI systems** — enabling autonomous agents to converse, use tools, execute code, and collaborate to solve complex tasks.

## 🚀 Features

- **Multi-agent conversation**: Design workflows where LLM-based agents (or human users) talk and collaborate seamlessly. :contentReference[oaicite:1]{index=1}  
- **Tool and code execution**: Embed tools into agents’ workflows, including code execution in controlled environments. :contentReference[oaicite:2]{index=2}  
- **LLM flexibility**: Compatible with multiple LLM providers—OpenAI, Anthropic, Gemini, local models, and more. :contentReference[oaicite:3]{index=3}  
- **Human-in-the-loop**: Agents can defer to humans when needed for oversight or input. :contentReference[oaicite:4]{index=4}  
- **Advanced orchestration**: Supports nested chats, group discussions, assistants, proxies, structured messaging, and real-time agents. :contentReference[oaicite:5]{index=5}  
- **Observability & debugging**: Built-in tracing, telemetry, cost calculation, and AgentOps support. :contentReference[oaicite:6]{index=6}  

---

## 📦 Installation

```bash
# Latest release from PyPI
pip install autogen

# Alias-supported (e.g. older/prefixed)
pip install pyautogen
````

---

## 🧪 Quick Start

Hello‑World example using two agents:

```python
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

assistant = AssistantAgent(name="Assistant", llm_config={…})
user = UserProxyAgent(name="User", human_input_mode="NEVER", llm_config={…})

group = GroupChat(agents=[user, assistant], messages=[], max_round=5)
manager = GroupChatManager(groupchat=group, llm_config={…})

user.initiate_chat(manager, message="Say hello!")
```

See full docs for detailed walkthroughs. ([ouyemed.com][1], [reddit.com][2], [autogenhub.github.io][3])

---

## 📚 Examples & Tutorials

Explore notebooks and demos covering:

* Multi-agent group chat
* Nested conversations
* Code generation/execution & debugging
* RAG systems with retrieval agents
* Multimodal and real-time voice agents
* Local LLM integrations (vicuna, chatglm)
* Observability, cost tracking, and tool usage
  ([reddit.com][4], [gist.github.com][5], [autogenhub.github.io][3], [microsoft.github.io][6])

---

## 🧩 Integrations

Supports a wide array of backends:

| Type          | Providers                                                                                |
| ------------- | ---------------------------------------------------------------------------------------- |
| LLMs          | OpenAI, Anthropic, Gemini, Cohere, Llama, Mistral, local LLMs, etc. ([pypi.org][7])      |
| Tooling       | Langchain, Qdrant, Chromadb, MongoDB, WebSearch, Apify, SQL tools, Whisper, DALLE, etc.  |
| Execution     | Docker-based or local code execution agents                                              |
| Observability | OpenTelemetry, AgentOps, cost tracking                                                   |

---

## 🏛️ License & Citation

* Licensed under **Apache 2.0** from v0.3.0 onwards ([pypi.org][8])
* For prior code from Microsoft’s AutoGen, MIT applies—see `LICENSE_original_MIT` ([pypi.org][9])
* If using in a paper:

  ```
  @software{AG2_2024,
    author = {Chi Wang and Qingyun Wu and the AG2 Community},
    title = {AG2: Open‑Source AgentOS for AI Agents},
    year = {2024},
    url = {https://github.com/ag2ai/ag2},
    version = {latest}
  }
  ```



---

## 🌐 Community & Governance

Originally part of Microsoft’s LF AML contributions, AutoGen has since spun off under the **AG2** organization, welcoming open governance and community collaboration. ([pypi.org][8])

Weekly office hours and community forums are supported; join us to ask questions, suggest features, or contribute code.

---

## 📈 Changelog Highlights

Significant updates:

* **v0.3.0**: Switched to Apache 2.0 license, PyPI renamed to `autogen` ([ouyemed.com][1], [pypi.org][8])
* **v0.4.x**: Fixed input bugs, improved component configs, stable console I/O ([reddit.com][10])
* **v0.7.0**: Added tool DI, real-time (WebRTC) agents, structured messages ([reddit.com][11])

For full release details, refer to GitHub releases.

---

## 🤝 Getting Involved

1. Fork & clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run notebooks under `examples/` or `.ipynb` files
4. Open a PR against `main`—ensure no API keys are included
5. Join office hours, file issues, or propose enhancements on GitHub

---

## 🔗 Useful Links

* Official docs & tutorials: [https://autogenhub.github.io/autogen](https://autogenhub.github.io/autogen) ([github.com][12], [autogenhub.github.io][13])
* AG2 GitHub org: `github.com/ag2ai/ag2` ([reddit.com][2])
* Foundational ICLR ’24 paper: *AutoGen: Enabling Next‑Gen LLM Applications via Multi‑Agent Conversation* ([arxiv.org][14])

---

*Happy building autonomous AI systems!*

[1]: https://www.ouyemed.com/microsoft/autogen/blob/main/README.md?utm_source=chatgpt.com "autogen/README.md at main · microsoft/autogen · GitHub"
[2]: https://www.reddit.com/r/AutoGenAI/comments/1gqtk3o?utm_source=chatgpt.com "AG2's AutoGen (autogen / pyautogen packages)"
[3]: https://autogenhub.github.io/autogen/docs/Examples/?utm_source=chatgpt.com "Examples | AutoGen"
[4]: https://www.reddit.com/r/learnmachinelearning/comments/1bo5yrz?utm_source=chatgpt.com "Multi-Agent Conversation using AutoGen using HuggingFace models"
[5]: https://gist.github.com/mberman84/ea207e7d9e5f8c5f6a3252883ef16df3?utm_source=chatgpt.com "AutoGen + Ollama Instructions · GitHub"
[6]: https://microsoft.github.io/autogen/0.2/blog/2023/07/14/Local-LLMs/?utm_source=chatgpt.com "Use AutoGen for Local LLMs | AutoGen 0.2"
[7]: https://pypi.org/project/autogen/0.7.4/?utm_source=chatgpt.com "autogen · PyPI"
[8]: https://pypi.org/project/autogen/0.3.0/?utm_source=chatgpt.com "autogen·PyPI"
[9]: https://pypi.org/project/autogen/?utm_source=chatgpt.com "autogen·PyPI"
[10]: https://www.reddit.com/r/AutoGenAI/comments/1i18fft?utm_source=chatgpt.com "AutoGen v0.4.1 released"
[11]: https://www.reddit.com/r/AutoGenAI/comments/1hxhcaq?utm_source=chatgpt.com "AG2 v0.7.0 released"
[12]: https://github.com/Sideshsundar/Autogen?utm_source=chatgpt.com "GitHub - Sideshsundar/Autogen"
[13]: https://autogenhub.github.io/autogen/?utm_source=chatgpt.com "AutoGen | AutoGen"
[14]: https://arxiv.org/abs/2308.08155?utm_source=chatgpt.com "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
