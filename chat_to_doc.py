import math
import streamlit as st
import time

from query_data import query_rag


# Streamed response emulator
def response_generator(prompt):
    start_time = time.time()
    with st.spinner():
        #response = query_rag(prompt)
        time.sleep(1)
        response = 'ok'
    for word in response.split():
        yield word + " "
        time.sleep(0.05)
    st.toast('Execution time : '+str(math.ceil(time.time() - start_time)) + ' seconds')

st.set_page_config(page_title="Chat with Docs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.title("Hello Human...!!!")


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