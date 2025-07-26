# 🧠 Twitter Sentiment Analysis App

A simple web app built with **Python**, **Flask**, and **scikit-learn** to analyze the sentiment (Positive, Negative, Neutral) of tweets using machine learning.

![Sentiment Pie Chart](static/sentiment_plot.png)

---

## 📌 Features

- 🔍 Clean text preprocessing (emoji removal, lowercasing, etc.)
- 💬 Sentiment classification (Logistic Regression)
- 📊 Pie chart visualization of predictions
- 🌐 Simple, responsive frontend with HTML/CSS
- 🚀 Easy-to-run Flask backend

---

## 🖼️ Demo

Enter a tweet and get the sentiment prediction instantly:

![Demo Screenshot](static/demo_screenshot.png)

---

## 📂 Project Structure
sentiment-analysis-x/
│
├── app.py # Main Flask app
├── templates/
│ └── index.html # HTML frontend
├── static/
│ └── sentiment_plot.png # Auto-generated sentiment chart
├── model/
│ └── sentiment140.csv # [Not included: see below]
├── venv/ # Virtual environment (excluded via .gitignore)
└── requirements.txt # Python dependencies


#🔧 Tech Stack
Python

Flask

Pandas, NumPy

scikit-learn

Matplotlib

HTML/CSS

✍️ Author
Dhiraj Kumar
