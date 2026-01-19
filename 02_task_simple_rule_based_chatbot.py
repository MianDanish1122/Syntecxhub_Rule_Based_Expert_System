import re
import datetime

# Define intents with patterns and responses
intents = {
    'greeting': {
        'patterns': [r'hello', r'hi', r'hey', r'good morning', r'good afternoon', r'good evening'],
        'responses': ['Hello! How can I help you today?', 'Hi there!', 'Hey! What\'s up?']
    },
    'help': {
        'patterns': [r'help', r'assist', r'support', r'what can you do'],
        'responses': ['I can answer questions about our company, provide help, or just chat. Ask me anything!', 'I\'m here to help. What do you need?']
    },
    'small_talk': {
        'patterns': [r'how are you', r'what\'s up', r'how is your day', r'tell me a joke'],
        'responses': ['I\'m doing well, thanks! How about you?', 'Just processing data, as usual. What about you?', 'Why did the computer go to the doctor? Because it had a virus!']
    },
    'goodbye': {
        'patterns': [r'bye', r'goodbye', r'see you', r'exit', r'quit'],
        'responses': ['Goodbye! Have a great day!', 'See you later!', 'Take care!']
    }
}

# Small knowledge base
knowledge_base = {
    'what is your name': 'I am a simple rule-based chatbot.',
    'what is python': 'Python is a high-level programming language known for its simplicity and readability.',
    'what is ai': 'AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.',
    'how does this chatbot work': 'This chatbot uses pattern matching to identify intents and respond with predefined rules.',
    'what is machine learning': 'Machine learning is a subset of AI that allows systems to learn from data without being explicitly programmed.'
}

def match_intent(user_input):
    user_input = user_input.lower()
    for intent, data in intents.items():
        for pattern in data['patterns']:
            if re.search(pattern, user_input):
                return intent, data['responses']
    return None, None

def get_knowledge_response(user_input):
    user_input = user_input.lower()
    for question, answer in knowledge_base.items():
        if question in user_input:
            return answer
    return None

def log_conversation(user_input, bot_response):
    with open('conversation_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f'[{timestamp}] User: {user_input}\n')
        log_file.write(f'[{timestamp}] Bot: {bot_response}\n\n')

def main():
    print("Chatbot: Hello! I'm a simple rule-based chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        # Check for goodbye
        intent, responses = match_intent(user_input)
        if intent == 'goodbye':
            bot_response = responses[0]  # Pick first response
            print(f"Chatbot: {bot_response}")
            log_conversation(user_input, bot_response)
            break

        # Check other intents
        if intent:
            import random
            bot_response = random.choice(responses)
        else:
            # Check knowledge base
            bot_response = get_knowledge_response(user_input)
            if not bot_response:
                bot_response = "I'm sorry, I don't understand that. Can you rephrase?"

        print(f"Chatbot: {bot_response}")
        log_conversation(user_input, bot_response)

if __name__ == "__main__":
    main()