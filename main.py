import streamlit as st

st.header("Welcome to the Reddit sentiment analyser!")

post = st.text_input("Enter Reddit post link:")

if st.button("Analyse"):
    if post.strip():

        st.write("Lorem ipsum")

    else:

        st.error("Please enter a valid Reddit post link before analysing.")
