import random

# Function to greet the user
def greet():
    responses = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
    return random.choice(responses)

# Function to provide a response
def get_response(user_input):
    greetings = ["hello", "hi", "hey", "greetings"]
    farewells = ["bye", "goodbye", "see you", "take care"]
    
    if user_input.lower() in greetings:
        return greet()
    elif user_input.lower() in farewells:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand. Can you please rephrase your statement?"

# Main program loop
def main():
    
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        
        if user_input.lower() in farewells:
            break

if __name__ == "__main__":
    main()
