from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st

model = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)


prompt_template = PromptTemplate.from_template(
    """You are a helpful AI assistant.
Please answer the user's query clearly, using a structured format such as bullet points or sections.
If the user asks for summarization, generate a concise and informative summary for the given input.

Query: {user_input}

Structured Answer:"""
)

st.title("🤖 Intelligent Assistant")
st.markdown("Ask me anything — from summaries to explanations!")


user_prompt = st.text_input("Enter your request:")


if st.button("Generate Response"):
    if user_prompt.strip():
        with st.spinner("Thinking..."):
            formatted_prompt = prompt_template.format(user_input=user_prompt)
            result = model.invoke(formatted_prompt)
            st.success("Response:")
            st.write(result)
    else:
        st.warning("Please enter something.")

