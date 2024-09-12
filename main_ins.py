import streamlit as st
from utils_ins import generate_instagram

st.header("Viral Instagram AI Writing Assistant ✏️")

with st.sidebar:
    openai_api_key = st.text_input("Please enter your Open AI API key:",type = "password")
    st.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")

theme = st.text_input("Topic")
submit = st.button("Start writing")

if submit and not openai_api_key:
    st.info("Please enter your Open AI API key")
    st.stop()
if submit and not theme:
    st.info("Please enter the topic of the generated content")
    st.stop()
if submit:
    with st.spinner("AI is working hard to create, please wait..."):
        result = generate_instagram(theme, openai_api_key)
    st.divider()

    left_column, right_column = st.columns(2)  # 设置左右行页面布局
    with left_column:
        st.markdown("##### Instagram Header 1")
        st.write(result.titles[0])
    with left_column:
        st.markdown("##### Instagram Header 2")
        st.write(result.titles[1])
    with left_column:
        st.markdown("##### Instagram Header 3")
        st.write(result.titles[2])
    with left_column:
        st.markdown("##### Instagram Header 4")
        st.write(result.titles[3])
    with left_column:
        st.markdown("##### Instagram Header 5")
        st.write(result.titles[4])

    with right_column:
        st.markdown("##### Instagram Post")
        st.write(result.content)
