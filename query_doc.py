import math

import streamlit as st
import time

from query_data import query_rag

st.set_page_config(page_title="Chat with Docs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Chat with Docs 🤖")

input_text = st.text_input("Ask Assistant")

submit = st.button("Search")

## Final response
if submit:
    start_time = time.time()
    st.write(query_rag(input_text,'mistral','nomic-embed-text'))
    st.success('Responded in '+str(math.ceil(time.time() - start_time)) + ' seconds')