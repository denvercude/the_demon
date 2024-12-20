from chat_gpt import chat_with_gpt
from chat_history import ChatHistory
from get_speech import capture_speech
from text_to_speech import speak_text
from visualizer import play_and_display
import pygame

# Initialize screen dimensions and colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Demon Visualizer")

# Set screen to fullscreen
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

# Function to draw the initial green line
def draw_initial_line():
    screen.fill(BLACK)
    line_y = screen_height // 2
    pygame.draw.line(screen, GREEN, (0, line_y), (screen_width, line_y), 2)
    pygame.display.flip()

def main():
    running = True
    chat_history = ChatHistory()

    # Draw the initial line
    draw_initial_line()

    while running:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # Allow ESC to exit fullscreen
                running = False

        # Capture user input
        user_input = capture_speech()

        if user_input:
            # Check for termination phrase
            if user_input.strip().lower() == 'goodbye demon':
                running = False
                continue

            print(f"You: {user_input}")

            # Get response from GPT
            response, chat_history = chat_with_gpt(user_input, chat_history)

            if response:
                print(f"Demon: {response}")

                # Generate and play response audio
                audio_file = speak_text(response, pitch_factor=0.77)
                play_and_display(audio_file, screen, screen_height, screen_width)

        # Ensure the screen updates continue
        pygame.display.flip()
        clock.tick(30)  # Limit to 30 FPS

    # Quit Pygame when done
    pygame.quit()

if __name__ == "__main__":
    main()
