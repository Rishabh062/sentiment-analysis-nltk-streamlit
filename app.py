import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
st.title("🤗Real Time Sentiment Analysis project.")
st.header("This streamlit webapp will try to classify sentiment on a real time using NLTK and streamlit🚀🚀")
st.header("👩🏻‍💻 Please provide us your feedback.")
user_input = st.text_input("Enter value:")
nltk.download("vader_lexicon")
s = SentimentIntensityAnalyzer()
score = s.polarity_scores(user_input)

if score == 0:
    st.write(" ")
elif score["neg"] != 0:
    st.write("# Negative")
elif score["pos"] != 0:
    st.write("# Positive")
