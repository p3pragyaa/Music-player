#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pygame


# In[2]:


import pygame
from pygame import mixer


# In[11]:


import pygame
from pygame import mixer

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
    r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\Tere Hawaale(PagalWorld.com.se).mp3",
    r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\Maan Meri Jaan(PagalWorld.com.se).mp3",
    r"C:\Users\KIIT\OneDrive\Documents\Web Development\PragyaPython-Project-1-Music\Jai Shri Ram(PagalWorld.com.se).mp3"
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
play_button = pygame.Rect(50, 100, 50, 50)
pause_button = pygame.Rect(120, 100, 50, 50)
stop_button = pygame.Rect(190, 100, 50, 50)
next_button = pygame.Rect(260, 100, 50, 50)

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
    pygame.draw.rect(window, (0, 255, 0), play_button)
    pygame.draw.rect(window, (255, 0, 0), pause_button)
    pygame.draw.rect(window, (0, 0, 255), stop_button)
    pygame.draw.rect(window, (255, 255, 0), next_button)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()


# In[ ]:




