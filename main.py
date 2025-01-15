import streamlit as st

st.header("Welcome to the Reddit sentiment analyser!")

col1, col2 = st.columns([1, 1])

with col1:
    subreddit_name = st.text_input(
        'Subreddit name with no "r/" (Bad: "r/test", Good: "test"):'
    )

with col2:
    amount_to_scrape = st.number_input(
        "Amount to analyse:",
        min_value=1,
        max_value=50,
        value=1,
        step=1,
    )

if st.button("Analyse"):
    if subreddit_name.strip():

        st.write("Lorem ipsum")

    else:
        st.error("Please enter an existing subreddit name!a")
