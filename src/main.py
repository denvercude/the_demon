import pygame
import numpy as np 
import time
from get_speech import capture_speech
from chat_gpt import chat_with_gpt
from text_to_speech import speak_text
from chat_history import ChatHistory
from pydub.utils import make_chunks
from pydub import AudioSegment
from pydub.playback import play
import threading

# Initial display of the waveform line on a black background.
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("ChatGPT Visualizer")
screen.fill((0, 0, 0))
pygame.display.flip()

line_y = screen.get_height() // 2
line_color = (0, 255, 0)

pygame.draw.line(screen, line_color, (0, line_y), (screen.get_width(), line_y), 2)
pygame.display.flip()

pygame.mixer.init(frequency=44100, size=-16, channels=1)

running = True
chat_history = ChatHistory()
is_playing_audio = False

def play_audio_with_visual(audio_file, screen, line_y, line_color):
    global is_playing_audio
    is_playing_audio = True
    audio = AudioSegment.from_file(audio_file)
    pygame.mixer.Sound(audio_file).play()
    samples = np.array(audio.get_array_of_samples())
    sample_rate = audio.frame_rate
    chunk_size = sample_rate // 30  # Approximate 30 FPS visualization
    chunks = [samples[i:i + chunk_size] for i in range(0, len(samples), chunk_size)]

    for i, chunk in enumerate(chunks):
        amplitude = np.abs(chunk).mean()
        amplitude_normalized = amplitude / (2 ** 15)
        bar_height = int(amplitude_normalized * (screen.get_height() // 2))  # Scale bar height
        
        screen.fill((0, 0, 0))  # Clear the screen
        for x in range(0, screen.get_width(), 10):  # Draw bars with spacing
            bar_y_top = line_y - bar_height // 2
            bar_y_bottom = line_y + bar_height // 2
            pygame.draw.line(screen, line_color, (x, bar_y_top), (x, bar_y_bottom), 5)  # Draw vertical bars
        pygame.display.flip()
        time.sleep(1 / 30)

    is_playing_audio = False
    
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, line_color, (0, line_y), (screen.get_width(), line_y), 2)
    pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    user_input = capture_speech()

    if user_input and user_input.strip().lower() == "goodbye demon":
        running = False
    
    if user_input:
        print(f"You: {user_input}")

        response, chat_history = chat_with_gpt(user_input, chat_history)

        # Generate the audio and save it to the file
        audio_file = speak_text(response, pitch_factor=0.77)

        threading.Thread(target=play_audio_with_visual, args=(audio_file, screen, line_y, line_color), daemon=True).start()

        if not is_playing_audio:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, line_color, (0, line_y), (screen.get_width(), line_y), 2)
            pygame.display.flip()