import random
import json
import pickle
import numpy as np
import nltk
from datetime import datetime

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

l = WordNetLemmatizer()

with open(r'C:\Users\KUSUM\OneDrive\Desktop\Syntecxhub_Projects\AirtifiacialIntelligence_project\AI_Chatbot_GitHub\intents.json') as file:
    intents = json.load(file)

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [l.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)

    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)

    res = model.predict(np.array([bow]), verbose=0)[0]

    ERROR_THRESHOLD = 0.25

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []

    for r in results:
        return_list.append({
            'intent': classes[r[0]],
            'probability': str(r[1])
        })

    return return_list


def get_response(intents_list, intents_json):

    if len(intents_list) == 0:
        return "Sorry, I didn't understand that."

    tag = intents_list[0]['intent']

    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "Sorry, something went wrong."


print(" Bot is ready!")
print("Type 'exit' to quit.\n")

# Create/open chat history file

with open("chat_history.txt", "a", encoding="utf-8") as log_file:

    log_file.write(
        f"\n\n===== Chat Started: {datetime.now()} =====\n"
    )

    while True:

        message = input("You: ")

        if message.lower() == "exit":
            print("Bot: Goodbye!")
            log_file.write("You: exit\n")
            log_file.write("Bot: Goodbye!\n")
            break

        ints = predict_class(message)
        res = get_response(ints, intents)

        print("Bot:", res)

        # Save conversation
        log_file.write(f"You: {message}\n")
        log_file.write(f"Bot: {res}\n")

print("Chat history saved to chat_history.txt")