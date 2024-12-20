# Customer Sentiment Analysis and Detection

## Overview: 
This project is a comprehensive solution for analyzing customer sentiment using machine learning. It includes:

- A Jupyter Notebook for preprocessing, training, and evaluating a sentiment analysis model.
- A Streamlit web application for user-friendly sentiment prediction.
## Features:

- Sentiment Analysis Model trained on customer reviews.
- Interactive Streamlit app for real-time predictions.
- Clear visualizations and insights (available in the notebook).
## Project Structure:

- __Customer_Review.ipynb__: A notebook to preprocess data, train a Naive Bayes model, and evaluate its performance on customer reviews.
- __app.py__: A Streamlit-based web app to provide a user-friendly interface for predicting sentiment.
## Setup Instructions:

```
pip install -r requirements.txt
```

## Run the Jupyter Notebook: 
Use Customer_Review.ipynb to preprocess and train the model. Save the trained model in the path specified in the app.py file.

```
streamlit run app.py
```

- Train the model using the notebook if needed.
- Use the Streamlit app to input customer reviews and get sentiment predictions.
# Dependencies:

- Python libraries: pandas, nltk, matplotlib, seaborn, streamlit, joblib, and more.
CSV file containing customer reviews (used in the notebook).

# Acknowledgments:

__Dataset__  : https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products/data
