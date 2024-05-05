import math
import time
import logging
import streamlit as st
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_with_toast(start_time):
    logger.info('Execution time : ' + str(math.ceil(time.time() - start_time)) + ' seconds')
    st.toast('Execution time : ' + str(math.ceil(time.time() - start_time)) + ' seconds')