from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import random


# Create a chatbot instance
chatbot = ChatBot("My Chatbot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train("chatterbot.corpus.english")

# Function to generate a random greeting
def greet():
    greetings = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
    return random.choice(greetings)

# Function to provide a response
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Main program loop
def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() in ["bye", "goodbye", "see you", "take care"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
