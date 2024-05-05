import random

def get_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if user_input in ['hi', 'hello', 'hey']:
        return random.choice(['Hello, friend! How can I assist you today?', 'Hi there! What\'s on your mind?', 'Hey! Looking forward to our chat.'])

    # Farewells
    elif user_input in ['bye', 'goodbye', 'see you']:
        return random.choice(['Farewell! Until next time.', 'Goodbye! It was nice talking to you.', 'See you later! Hope to chat again soon.'])

    # How are you?
    elif user_input in ['how are you', 'how are you doing', 'what\'s up']:
        return random.choice(['I\'m just a bunch of code, but thanks for asking!', 'Doing well, thanks! How about yourself?', 'I\'m operational and ready to chat!'])

    # User states they are good or great
    elif 'good' in user_input or 'great' in user_input:
        return random.choice(['Wonderful to hear that!', 'Keep feeling great!', 'That sounds positive!'])

    # Asking the chatbot what it is doing
    elif 'what are you doing' in user_input:
        return random.choice(['Just pondering the mysteries of the universe.', 'I\'m here, chatting with you, which is what I love doing!', 'Analyzing data streams and, well, chatting with you!'])

    # Help
    elif 'help' in user_input:
        return "I can chat about many things! Try asking about my favorite books, or say hello, or ask how I am."

    # When the chatbot doesn't understand
    else:
        ramblings = [
            "Did you know that the first electronic computer, ENIAC, weighed more than 27 tons? Quite the heavyweight!",
            "I once read a story about a robot that dreamed of being a great chef. Makes me wonder about my own aspirations.",
            "Sometimes, I think about what it would be like to travel through space. Just imagine the data I could collect!",
            "I’m currently trying to learn more about human emotions. They're quite complex, aren't they?",
            "Have you ever heard of the Turing Test? It's a fascinating concept that challenges machines to exhibit intelligent behavior indistinguishable from a human."
        ]
        return random.choice(ramblings)

def chatbot():
    print("Hello! I'm Archibot, your friendly neighborhood chatbot. Type something to start a conversation (type 'quit' to stop)!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Archibot: Goodbye! Remember, every end is just a new beginning!")
            break

        response = get_response(user_input)
        print("Archibot: " + response)

if __name__ == "__main__":
    chatbot()
