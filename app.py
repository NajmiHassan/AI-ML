import streamlit as st
from openai import OpenAI

# Initialize client with your own API key and endpoint if different from default OpenAI settings
client = OpenAI(
    api_key="e677189f43f0498abbd2b5f4a4b7a596",
    base_url="https://api.aimlapi.com"
)

# Function to get response from OpenAI
def get_response(question, chat_history):
    # Add previous chat history to the messages
    messages = [{"role": "system", "content": "You are an AI assistant who knows everything."}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": question})
    
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=messages,
    )
    return response.choices[0].message.content

# Initialize session state variables for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Set up the main structure of Streamlit app
st.title('AI/ML Chatbot')
st.write("Chat with the AI assistant:")

# Display chat history
for chat in st.session_state.chat_history:
    if chat['role'] == 'user':
        st.write(f"**You:** {chat['content']}")
    else:
        st.write(f"**Assistant:** {chat['content']}")

# User input text box
user_input = st.text_input("Type your question here...")

if st.button('Send'):
    if user_input:
        # Get response from AI based on input query
        answer = get_response(user_input, st.session_state.chat_history)
        
        # Update chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        
        # Clear the input box for the next question
        st.experimental_rerun()
    else:
        st.write("Please enter a question.")
