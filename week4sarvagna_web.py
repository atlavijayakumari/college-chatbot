# week4sarvagna_chat.py
# Conversational College FAQ Bot - Offline, No API Key Needed

import streamlit as st

# FAQ database
faq_data = {
    "what are your college timings": "Our college operates from 9:00 AM to 4:00 PM, Monday to Saturday.",
    "how to apply for admission": "You can apply via our official website under the Admissions section.",
    "what courses do you offer": "We offer B.Tech, M.Tech, MBA, and Diploma courses in various specializations.",
    "what is the fee structure": "The fee structure depends on the course. Please visit our official website for details.",
    "how to contact the college": "You can contact us at +91-9876543210 or email at info@college.com."
}

# Greeting keywords
greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]

# Exit keywords
goodbyes = ["bye", "goodbye", "exit", "quit", "thank you", "thanks"]

# Function to generate bot responses
def generate_response(user_query):
    query_lower = user_query.lower().strip()

    # Greeting check
    if query_lower in greetings:
        return "Hello! 👋 How can I help you with college-related questions today?"

    # Goodbye check
    if query_lower in goodbyes:
        return "Thank you for chatting with me! 😊 Have a great day. 👋"

    # Check FAQs
    for question, answer in faq_data.items():
        if question in query_lower:
            return answer

    return "Sorry, I don't have an answer for that. Please contact the college for more info."

# Streamlit page setup
st.set_page_config(page_title="🎓 College FAQ Chatbot", page_icon="🤖")
st.title("🎓 College FAQ Chatbot")
st.write("Ask me anything about the college! Type 'bye' to end the conversation.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input box
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot reply
    bot_reply = generate_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_reply})

    # If user says goodbye → stop accepting new inputs
    if user_input.lower().strip() in goodbyes:
        st.session_state.chat_ended = True

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")

# Disable input after goodbye
if st.session_state.get("chat_ended", False):
    st.warning("🔒 Conversation ended. Refresh the page to start again.")
