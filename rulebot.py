import time

# Rule-based logic
def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I assist you today?"

    elif user_input in ["how are you?", "how are you", "how r u"]:
        return "I'm functioning optimally. Thank you for asking!"

    elif user_input in ["what is your name?", "who are you?"]:
        return "I’m RuleBot 2.0 – your virtual assistant."

    elif user_input in ["it was nice chatting with you. bye!", "goodbye"]:
        return "Goodbye! Feel free to reach out again anytime."

    elif user_input in ["thanks!", "thank you", "thank you!"]:
        return "You're welcome!"

    elif user_input in ["what can you do?", "help", "how can you assist me?"]:
        return ("I can assist with greetings, share the current time and date, provide basic facts, "
                "respond to general queries, and more.")

    elif user_input in ["what's the time?", "what time is it?", "current time"]:
        return f"The current time is {time.strftime('%I:%M %p')}."

    elif user_input in ["what day is it?", "today's date", "current date"]:
        return f"Today is {time.strftime('%A, %B %d, %Y')}."

    elif user_input in ["what are you?", "what do you do?"]:
        return "I’m a digital assistant created to help with simple, rule-based queries."

    elif user_input in ["what is ai?", "explain ai", "define ai"]:
        return "Artificial Intelligence refers to the simulation of human intelligence by machines."

    elif user_input in ["tell me a fact", "share a fact", "give me a fact"]:
        return "Here’s a fact: The Eiffel Tower can be 15 cm taller during hot days due to thermal expansion."

    elif user_input in ["i'm bored! what should i do?"]:
        return "You could read something interesting or take a short walk!"

    elif user_input in ["can you tell a joke?", "tell me a joke", "make me laugh"]:
        return "Why don't scientists trust atoms? Because they make up everything."

    elif user_input in ["good morning"]:
        return "Good morning! I hope you have a productive day ahead."

    elif user_input in ["good night"]:
        return "Good night! Rest well and take care."

    elif user_input in ["i feel sad", "i'm sad"]:
        return "I'm sorry to hear that. Taking a break or speaking with a friend might help."

    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase your question?"

# Console conversation loop
print("Bot: 👋 Welcome! I'm RuleBot 2.0.")
while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot: ", response)
    if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
        break
