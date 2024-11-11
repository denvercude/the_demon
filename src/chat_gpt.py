import openai
from chat_history import ChatHistory
from config import OPENAI_API_KEY, DEFAULT_MODEL

# Load API KEY
openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt, chat_history=None):
    try:
        # Initialize ChatHistory if not provided
        if chat_history is None:
            chat_history = ChatHistory()

        # Add the user's message to the chat history
        chat_history.add_message("user", prompt)

        # Call OpenAI's API with the chat history
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=chat_history.get_history()
        )

        # Extract and add the assistant's reply to the chat history
        reply = response['choices'][0]['message']['content']
        chat_history.add_message("assistant", reply)

        return reply, chat_history
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return None, chat_history