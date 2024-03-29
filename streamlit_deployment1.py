import streamlit as st

st.set_page_config(layout="wide")
st.title("OpenAI Demo")
st.sidebar.title("AI Apps")

ai_app = st.sidebar.radio("Choose an ai app",("Blog generator","Image generator","Movie Recommendor"))

if ai_app == "Blog generator":
  st.header("Blog Generator")
  st.write("Input a topic to generate a blog about it using OpenAI")

  topic = st.text_area("Topic", height=20)
  additional_text = st.text_area("Additional Text", height=20)

  if st.button("Generate Blog"):
    st.write("Blog Generated")

elif ai_app == "Image generator":
  st.header("Image Generator")
  st.write("Input a prompt to generate a image about it using OpenAI")

  prompt = st.text_area("Prompt", height=20)

  if st.button("Generate Image"):
    st.write("Image Generated")

elif ai_app == "Movie Recommendor":
  st.header("Movie Recommendor")
  st.write("Input a description to generate related movie recommendations")

  movie_description = st.text_area("Movie Description", height=20)

  if st.button("Recommend Movies"):
    st.write("Movies recommended")


