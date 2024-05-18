# ollama-rag-streamlit
This is an opensource playground for people who want to test out different LLM and embedding models to choose which works best for them <br/>

Complete e2e opensource solution . You do not need any account in any tools like huggingface,openai etc to use this.

# Tech stack used
ollama,langchain,pluggable opensource llm and embedding models,chroma DB,streamlit as wrapper

# Pre req
Download and install Ollama from https://ollama.com/ <br/>
Download the models you want to use in your app: <br/>
Ex : ollama pull llama3 <br/>
     ollama pull nomic-embed-text <br/>
     <br/>

# How to use
pip install -r requirements.txt  <br/>

streamlit run chat_to_doc.py

From the Dopdown on the left, you can choose which model to embed and which model to use for LLM

# Screenshots
Uploading Docs
![Alt text](images/1.png?raw=true "Query")

Querying Docs
![Alt text](images/2.png?raw=true "Result")
