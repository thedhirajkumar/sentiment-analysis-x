# 🧠 Twitter Sentiment Analysis App

Sentiment Analyzer
A Python-based web application that performs sentiment analysis on text input using VADER (Valence Aware Dictionary and sEntiment Reasoner). Built with Flask, it allows users to input text and view sentiment (Positive, Negative, or Neutral) while displaying a pie chart of sentiment distribution from the Sentiment140 dataset or sample texts. Developed by Dhiraj Kumar, CSE student at NIT Silchar.
Features

Analyze sentiment of user-input text in real-time.
Visualize sentiment distribution of sample tweets from the Sentiment140 dataset using a pie chart.
Simple and intuitive web interface.

#Tech Stack

-Python: Backend logic and sentiment analysis.

-Flask: Web framework for the user interface.
-VADER (via NLTK): Sentiment analysis library.
-Pandas & Matplotlib: Data handling and visualization.

Installation

Clone the repository:git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer


Set up a virtual environment:python -m venv venv
.\venv\Scripts\activate  # On Windows


Install dependencies:pip install -r requirements.txt


Download the Sentiment140 dataset from Kaggle and place training.1600000.processed.noemoticon.csv as sentiment140.csv in the project folder.
Run the application:python app.py


Open http://127.0.0.1:5000 in your browser.

Usage

Enter text in the input field and click "Analyze" to see the sentiment result.
View the pie chart below, which shows the sentiment distribution of the first 10 tweets from the Sentiment140 dataset (or hardcoded sample texts if the dataset is missing).

Future Improvements

Integrate real-time X post fetching via the X API.
Add support for multilingual sentiment analysis (e.g., Hindi).
Deploy to a cloud platform like Heroku or Render for a live demo.
Enhance the UI with Bootstrap or a modern framework.

License
MIT License


