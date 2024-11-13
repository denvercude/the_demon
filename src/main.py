from chat_gpt import chat_with_gpt
from text_to_speech import speak_text
from get_speech import capture_speech
from chat_history import ChatHistory
from create_memory import generate_and_save_summary
 
def main():
    print("Starting the voice-based ChatGPT conversation. Press Ctrl+C to exit.")
    chat_history = ChatHistory()  # Initialize chat history

    while True:
        try:
            # Capture user's speech input
            user_input = capture_speech()
            if user_input:
                print(f"You: {user_input}")

                # Check for the exit phrase "Goodbye Demon"
                if user_input.strip().lower() == "goodbye demon":
                    print("Ending session and generating summary...")

                    # **Call the generate_and_save_summary function**
                    generate_and_save_summary(chat_history)
                    break  # Exit the loop after saving the summary

                # Send user input to ChatGPT and get a response
                gpt_response, chat_history = chat_with_gpt(user_input, chat_history)
                if gpt_response:
                    print(f"ChatGPT: {gpt_response}")
                    
                    # Use ElevenLabs TTS to speak out the response
                    speak_text(gpt_response, pitch_factor=0.77)  # Adjust pitch as needed

        except KeyboardInterrupt:
            print("\nConversation ended by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    main()
