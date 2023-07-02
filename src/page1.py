import streamlit as st

introduction = """### OpenAI DALL-E
- OpenAI DALL-E is a neural network-based image generation system that can create images from textual descriptions.
- It was introduced by OpenAI in January 2021.
- The system is capable of generating high-quality images of objects that do not exist in the real world.
- DALL-E can modify several of an object's attributes, as well as the number of times that it appears.
- DALL-E 2 generates more realistic and accurate images with 4x greater resolution than DALL-E 1.
- DALL-E 2 is preferred over DALL-E 1 when evaluators compared each model. 71.7% preferred for caption matching and 88.8% preferred for photorealism.
"""

def page1():
    st.title("OPEN AI DALL-E")
    st.info(introduction)