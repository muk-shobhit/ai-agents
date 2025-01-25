# AI Agents with Phi Data

This repository demonstrates simple steps to create and work with AI agents using the [Phi Data](https://www.phidata.com/) framework. It showcases how to build basic agents, integrate tools, and develop teams of agents leveraging multiple LLMs and tools.

---

[![Agentic AI](https://img.youtube.com/vi/K9H7O7jPcZg/0.jpg)](https://www.youtube.com/watch?v=K9H7O7jPcZg)

## What Are AI Agents?

AI agents are software entities designed to perform tasks autonomously or semi-autonomously. They utilize Artificial Intelligence (AI) models and frameworks to:

- Analyze data
- Execute predefined actions
- Solve complex problems by leveraging multiple tools

Agents can be simple (focused on a single task) or complex (capable of coordinating with other agents).

---

## Frameworks and Models Used

### Phi Data Framework
- **Phi Data**: A robust agent creation framework that supports multiple large language models (LLMs) and tools for advanced AI capabilities.

### Models Used
1. **OLama ([Groq](https://groq.com/))**
   - An open-source model offering versatility and scalability.
   - Utilized via Groq for efficient deployment and execution.

2. **[Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) GPT**
   - Integrated to provide state-of-the-art conversational capabilities.

---

## Features of This Repository

### 1. **Basic Agents**
- Build and understand foundational agents.

### 2. **Agents with Multiple Tools**
- Extend agent functionality with tools for:
  - **Web search**: Gather information dynamically.
  - **Finance analysis**: Analyze financial data and trends.

### 3. **Team of Agents**
- Demonstrates how multiple agents can collaborate to solve complex problems.

---

## Installation Steps

Follow these steps to set up the project:

### Step 1: Set Up Python Virtual Environment
1. Open a terminal or command prompt.
2. Create a virtual environment:
   ```bash
   python -m venv ai_agents_env
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```bash
     ai_agents_env\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source ai_agents_env/bin/activate
     ```

### Step 2: Install Required Packages
1. Install the Phi Data package:
   ```bash
   pip install phidata
   ```

2. Install additional dependencies as needed:
   ```bash
   pip install -r requirements.txt
   ```

---

## Step-by-Step Video Guide

For a detailed walkthrough of the repository, watch the [YouTube video](https://www.youtube.com/watch?v=K9H7O7jPcZg). This video covers:
- Setting up the environment.
- Installing dependencies.
- Running the agents and understanding their outputs.
- Extending functionality with custom tools.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to:
- **Phi Data** for the powerful agent creation framework.
- **Groq** and **Azure OpenAI** for their robust AI models.
