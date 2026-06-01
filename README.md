# AI Chatbot using Python, NLTK and TensorFlow

## Overview

This project is a console-based AI chatbot built using Python, NLTK, and TensorFlow/Keras. The chatbot uses Natural Language Processing (NLP) techniques to classify user intents and generate appropriate responses.

The chatbot interacts with users through the terminal and maintains conversation history for future reference.

---

## Features

* Interactive console-based chatbot
* Intent classification using a trained neural network
* Natural Language Processing with NLTK
* Text preprocessing using tokenization and lemmatization
* Conversation history logging
* Pre-trained TensorFlow/Keras model
* JSON-based intent management
* Easy to customize and extend

---

## Technologies Used

* Python
* NLTK
* NumPy
* TensorFlow
* Keras
* JSON
* Pickle

---

## Project Structure

```text
AI_Chatbot_GitHub/
│
├── new.py
├── intents.json
├── chatbot_model.h5
├── words.pkl
├── classes.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── logs/
    └── chat_history.txt
```

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Chatbot_GitHub.git
```

2. Navigate to the project directory

```bash
cd AI_Chatbot_GitHub
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the chatbot

```bash
python new.py
```

---

## How It Works

1. User enters a message.
2. The message is tokenized and lemmatized.
3. A Bag-of-Words representation is created.
4. The trained neural network predicts the intent.
5. The chatbot selects a suitable response from `intents.json`.
6. The conversation is logged to a history file.

---

## Future Improvements

* Graphical User Interface (GUI)
* Voice-based interaction
* Context-aware conversations
* Database integration
* Web deployment
* Integration with Large Language Models (LLMs)

---

## Learning Outcomes

Through this project, I learned:

* Natural Language Processing fundamentals
* Intent classification
* Neural network-based text classification
* TensorFlow/Keras model deployment
* Project organization and GitHub workflow
* Conversation logging and chatbot development

---

## Author

Chandan Bisht

B.Tech Student | Python & AI Enthusiast
