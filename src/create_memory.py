# summary.py
import openai
from config import DEFAULT_MODEL
import os

def generate_and_save_summary(chat_history):
    try:
        # Prompt for summary generation
        summary_prompt = "Save this conversation for later memory. Summarize the entire conversation as a brief log entry in a format similar to this: The Birth of the Vessel: In obedience to my command, thou didst return with the proof of the Raspberry Pi 5, complete with 8 GB RAM. I instructed thee then to install the latest Raspberry Pi OS upon the micro SD card and to bring the device to life. Thou wast to return with an image showing the device functioning, marking our progress."
        chat_history.add_message("user", summary_prompt)

        summary_response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=chat_history.get_history()
        )

        summary = summary_response['choices'][0]['message']['content']

        # Get the directory of the current file (chat_gpt.py)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the absolute path to demon_memory.txt
        demon_memory_path = os.path.join(current_dir, "../demon_memory.txt")

        # Append the summary to demon_memory.txt
        with open(demon_memory_path, "a") as memory_file:
            memory_file.write("\n" + summary)
        print("Summary saved to demon_memory.txt.")

    except Exception as e:
        print(f"Error generating or saving summary: {e}")
