import streamlit as st
from textblob import TextBlob
import pandas as pd
import joblib

# Function to analyze sentiment
def analyze_sentiment(text):
   
   model = joblib.load(r"C:\Users\Sparsh Mahajan\OneDrive\Documents\c progams\.vscode\.vscode\backend\Customer Sentiment Predictor\model\naive_bayes.pkl")
   prediction = model.predict([text])
   if prediction==0:
       return "Negative"
   else:
       return "Positive"

# Streamlit UI

st.title("Customer Sentiment Detector")

# Text Input
st.subheader("Analyze Single Feedback")
user_input = st.text_area("Enter customer feedback here:", placeholder="Type your feedback...")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        sentiment = analyze_sentiment(user_input)
        st.write(f"**Sentiment:** {sentiment}")
    else:
        st.warning("Please enter some feedback to analyze.")



