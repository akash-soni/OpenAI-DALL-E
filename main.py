import streamlit as st
from src.page1 import page1
from src.page2 import page2
from src.page3 import page3
from src.page4 import page4
import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")



Pages = {
"Entry page": page1,
"Text to Image": page2,
"Image Variation": page3,
"Image Edit": page4
}

page = st.sidebar.selectbox("Select a page", list(Pages.keys()))

Pages[page]()
