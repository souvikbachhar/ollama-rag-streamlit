import math
import streamlit as st
import time

from query_data import query_rag


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
    st.toast('Execution time : '+str(math.ceil(time.time() - start_time)) + ' seconds')

st.set_page_config(page_title="Chat with Docs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='expanded')
st.title("Hello Human...!!!")
with st.sidebar:
    selected_embed_model = st.sidebar.selectbox('Choose embedding model', ['nomic-embed-text'], key='selected_embed_model')
    selected_llm_model = st.sidebar.selectbox('Choose LLM model', ['mistral','gemma:2b'], key='selected_llm_model')
    uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
    st.markdown("""---""")
    "[Available Embedding models](https://python.langchain.com/docs/integrations/text_embedding/)"
    "[Available LLM models](https://github.com/ollama/ollama?tab=readme-ov-file#quickstart)"
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