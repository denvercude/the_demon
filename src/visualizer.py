import pygame
import numpy as np
import wave
import threading
import sys

def play_and_display(audio_file, screen, screen_height, screen_width):
    # Set up colors
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    # Initialize Pygame mixer and screen
    pygame.mixer.init()

    # Load the audio file
    try:
        pygame.mixer.music.load(audio_file)
    except pygame.error as e:
        print(f"Error loading audio file: {e}")
        sys.exit()

    # Function to process audio and return frequency data
    def analyze_audio():
        wf = wave.open(audio_file, 'rb')
        framerate = wf.getframerate()
        chunk_size = 1024

        while True:
            data = wf.readframes(chunk_size)
            if len(data) == 0:
                break
            # Convert to numpy array
            audio_data = np.frombuffer(data, dtype=np.int16)
            fft_data = np.abs(np.fft.fft(audio_data)[:len(audio_data)//2])
            yield fft_data

        wf.close()

    # Create a generator for audio analysis
    audio_generator = analyze_audio()

    # Function to update visualizer
    def update_visualizer():
        try:
            fft_data = next(audio_generator)
            screen.fill(BLACK)

            # Draw bars based on FFT data
            num_bars = 50
            bar_width = screen_width // num_bars
            max_bar_height = screen_height // 2

            # Mirror the data for symmetry
            half_bars = num_bars // 2
            for i in range(half_bars):
                bar_height = min(int(fft_data[i] / 1000), max_bar_height)
                # Left side
                x_pos_left = screen_width // 2 - (i + 1) * bar_width
                pygame.draw.rect(screen, GREEN, (x_pos_left, screen_height // 2 - bar_height, bar_width - 2, bar_height * 2))
                # Right side
                x_pos_right = screen_width // 2 + i * bar_width
                pygame.draw.rect(screen, GREEN, (x_pos_right, screen_height // 2 - bar_height, bar_width - 2, bar_height * 2))

            pygame.display.flip()
        except StopIteration:
            pass

    # Play audio in a separate thread
    def play_audio():
        pygame.mixer.music.play()

    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

    # Main Pygame loop
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.music.stop()

        # Check if music is still playing
        if pygame.mixer.music.get_busy():
            # Update visualizer
            update_visualizer()
        else:
            # Draw static green line when audio ends
            screen.fill(BLACK)
            line_y = screen_height // 2
            pygame.draw.line(screen, GREEN, (0, line_y), (screen_width, line_y), 2)
            pygame.display.flip()
            running = False  # Exit the loop when audio finishes

        clock.tick(30)  # 30 frames per second

    # Ensure audio thread finishes before returning
    audio_thread.join()

# When the function exits, it will return control to the main program loop
