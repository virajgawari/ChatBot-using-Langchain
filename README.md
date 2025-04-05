# 🤖 Intelligent Assistant using Mistral-7B and Streamlit

This is a simple yet powerful AI assistant web app built using **Streamlit**, **LangChain**, and **HuggingFace's Mistral-7B** model. It takes user queries and provides clear, structured answers — including summaries and explanations.

## 🚀 Features

- Uses **Mistral-7B-Instruct-v0.2** for intelligent text generation.
- Structured and helpful responses via **LangChain PromptTemplates**.
- Clean and responsive **Streamlit UI**.
- Supports tasks like:
  - Summarization
  - General question answering
  - Clear, bullet-point or section-based explanations

## 📦 Requirements

Make sure you have the following installed:

```bash
pip install streamlit langchain langchain_huggingface python-dotenv
```

## Example Prompt Template

You are a helpful AI assistant.
Please answer the user's query clearly, using a structured format such as bullet points or sections.
If the user asks for summarization, generate a concise and informative summary for the given input.

Query: {user_input}

Structured Answer:

## Set Up Environment Variables

Create a .env file in the root directory with your Hugging Face API key:
```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key
```

## Project Structure
```bash
intelligent-assistant/
│
├── app.py             # Main Streamlit application
├── .env               # Environment variables (not committed)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```
