import pygame
from pygame import mixer
from pygame.locals import *
import os

# Initialize pygame and mixer
pygame.init()
mixer.init()

# Create window
window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Music Player")

# List of music files
music_files = [
    r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\Jai Shri Ram(PagalWorld.com.se).mp3",
    r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\Maan Meri Jaan(PagalWorld.com.se).mp3",
    r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\Tere Hawaale(PagalWorld.com.se).mp3"
]

# Index of current song
current_song_index = 0

# Load and play current song
def play_current_song():
    mixer.music.load(music_files[current_song_index])
    mixer.music.play()

# Play the current song
play_current_song()

# Button coordinates and dimensions
button_width = 50
button_height = 50
button_padding = 10

play_button = pygame.Rect(50, 100, button_width, button_height)
pause_button = pygame.Rect(120, 100, button_width, button_height)
stop_button = pygame.Rect(190, 100, button_width, button_height)
next_button = pygame.Rect(260, 100, button_width, button_height)

# Load button images
play_button_image = pygame.image.load(r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\play-button.png")
pause_button_image = pygame.image.load(r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\pause-button.png")
stop_button_image = pygame.image.load(r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\stop-button.png")
next_button_image = pygame.image.load(r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\next-button.png")

# Scale button images to fit the button dimensions
play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))
pause_button_image = pygame.transform.scale(pause_button_image, (button_width, button_height))
stop_button_image = pygame.transform.scale(stop_button_image, (button_width, button_height))
next_button_image = pygame.transform.scale(next_button_image, (button_width, button_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if buttons are clicked
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    mixer.music.unpause()
                elif pause_button.collidepoint(mouse_pos):
                    mixer.music.pause()
                elif stop_button.collidepoint(mouse_pos):
                    mixer.music.stop()
                elif next_button.collidepoint(mouse_pos):
                    # Play next song
                    current_song_index = (current_song_index + 1) % len(music_files)
                    play_current_song()

    # Clear the window
    window.fill((255, 255, 255))

    # Draw buttons
    window.blit(play_button_image, play_button)
    window.blit(pause_button_image, pause_button)
    window.blit(stop_button_image, stop_button)
    window.blit(next_button_image, next_button)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
