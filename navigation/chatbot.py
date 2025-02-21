import streamlit as st

# Function to generate bot responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I assist you today? 😊",
        "how are you": "I'm just a bot, but I'm doing great! Thanks for asking. What about you?",
        "what is your name": "I'm your friendly chatbot! 🤖",
        "bye": "Goodbye! Have a great day ahead! 👋",
        "what is python": "Python is a high-level programming language known for its simplicity and versatility. 🐍",
        "what is streamlit": "Streamlit is an open-source app framework for Machine Learning and Data Science projects. 🚀",
        "who is the founder of microsoft": "Microsoft was founded by Bill Gates and Paul Allen in 1975. 💻",
        "who is elon musk": "Elon Musk is a billionaire entrepreneur known for Tesla, SpaceX, Neuralink, and more. 🚀",
        "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence in machines. 🤖",
        "what is machine learning": "Machine Learning is a subset of AI that enables computers to learn from data. 📊",
        "who is the ceo of apple": "As of now, Tim Cook is the CEO of Apple. 🍏",
        "what is the capital of france": "The capital of France is Paris. 🗼",
        "what is the tallest mountain": "Mount Everest is the tallest mountain in the world, standing at 8,848 meters. ⛰️",
    }

    return responses.get(user_input, "Sorry, I didn't understand that. Can you rephrase?")

# Streamlit UI
st.title("💬 Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate bot response
    bot_reply = chatbot_response(user_input)
    
    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
