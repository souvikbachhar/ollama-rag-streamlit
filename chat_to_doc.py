import glob
import math
import os
import shutil

import streamlit as st
import time

from populate_database import clear_database, load_documents_to_database, load_documents
from query_data import query_rag
from util import log_with_toast

#CACHE_DATA_FULL_PATH = os.getcwd()+"\cache" #windows
CACHE_DATA_FULL_PATH = os.getcwd()+"/cache" #linux

# Streamed response emulator
def response_generator(prompt):
    start_time = time.time()
    with st.spinner('Generating...⏳'):
        response = query_rag(prompt, selected_llm_model, selected_embed_model)
        #time.sleep(1)
        #response = 'ok'
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
    log_with_toast(start_time)


st.set_page_config(page_title="Chat with Docs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='expanded')
st.title("Hello Human...!!!")
with st.sidebar:
    selected_embed_model = st.sidebar.selectbox('Choose embedding model', ['nomic-embed-text'],
                                                key='selected_embed_model')
    selected_llm_model = st.sidebar.selectbox('Choose LLM model', [ 'llama3','mistral', 'gemma:2b'],
                                              key='selected_llm_model')
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)

    col1, col2 = st.columns([5, 5])
    with col1:
        if st.button("Upload and Train", type="secondary"):
            with st.spinner('Training...⏳'):
                start_time = time.time()
                for uploaded_file in uploaded_files:
                    path = os.path.join(CACHE_DATA_FULL_PATH, uploaded_file.name)
                    with open(path, "wb") as f:
                        f.write(uploaded_file.getvalue())

                load_documents_to_database()

                for filename in os.listdir(CACHE_DATA_FULL_PATH):
                    os.remove(os.path.join(CACHE_DATA_FULL_PATH, filename))
                log_with_toast(start_time)
    with col2:
        if st.button("Reset DB", type="primary"):
            with st.spinner('Cleaning...⏳'):
                start_time = time.time()
                clear_database()
                log_with_toast(start_time)

    st.markdown("""---""")
    "[Available Embedding models](https://python.langchain.com/docs/integrations/text_embedding/)"
    "[Available LLM models](https://ollama.com/library)"
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
