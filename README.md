![image](https://github.com/user-attachments/assets/d1cfac6a-8c8e-4426-ae79-bfbdbd4c8310)

# Automatic Tool Generation
> [!NOTE]  
> This project is designed to work seamlessly with [create_react_agent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.react.agent.create_react_agent.html) from LangGraph.
> The generated tool functions are fully compatible with the `create_react_agent` framework. However, if you remove the `@tool` decorator, these functions can also be used in any other framework.

This is a subproject of [*Create Data Scientist Agent*](docs/hyperproject.md)

The main goal of this project is to **automatically and independently generate tools** for use by LLM agents. Rather than manually predefining tools for every possible use case, this project introduces a pipeline that can:

1. **Analyze** the task type  
2. **Ideate** potential solutions  
3. **Generate** appropriate Python tools  
4. **Validate** them against sample data

This approach enables more flexible, scalable, and intelligent agents that can adapt to diverse data analysis scenarios without requiring human experts in tool preparation.
There are some [examples](example/gen_tool_01.py) of generated tools avaliable.

> [!WARNING]
> **CLI tools are still under active development**, and functionality is currently limited.
> For full experience, consider using **LangGraph Studio** instead.
>
> 👉 Check how to get started with [LangGraph Studio](docs/how_to/use_langgraph_dev.md) for this project

# Quick Start

1. **Set up your environment**  
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your own API keys and configuration as needed.

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Use LangGraph Studio**  
   If you want to use LangGraph Studio for a better development experience:  
   ```bash
   pip install 'langgraph-cli[inmem]'
   ```
   >This step does not require creating account.
   >It run a local server and open a web browser to control the agent

View the [documntation](https://salmonsung.github.io/automatic-tool-generation/) for more details on features and configuration options best suited to your project.

# Table of Content 
- Usage Guideline:
   - [LangGraph Dev(recommand)](docs/how_to/use_langgraph_dev.md)
   - [Cli tool](docs/how_to/use_cli.md)
   - [Use in Your Project](docs/how_to/use_as_package.md)
