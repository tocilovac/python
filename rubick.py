import pygame
import numpy as np
from pygame.locals import *

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rubik's Cube Solver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Cube geometry (3x3x3)
cube = np.array([
    [[RED, RED, RED], [RED, RED, RED], [RED, RED, RED]],    # Front face
    [[GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN], [GREEN, GREEN, GREEN]],  # Back face
    [[BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE], [BLUE, BLUE, BLUE]],         # Left face
    [[ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE], [ORANGE, ORANGE, ORANGE]],  # Right face
    [[YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW], [YELLOW, YELLOW, YELLOW]], # Top face
    [[WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE], [WHITE, WHITE, WHITE]]  # Bottom face
])

# Draw the cube
def draw_cube():
    face_positions = [
        (300, 200),  # Front
        (500, 200),  # Back
        (100, 200),  # Left
        (700, 200),  # Right
        (300, 50),   # Top
        (300, 350)   # Bottom
    ]
    
    for i, (x, y) in enumerate(face_positions):
        for row in range(3):
            for col in range(3):
                pygame.draw.rect(screen, cube[i][row][col], 
                                (x + col * 30, y + row * 30, 28, 28))

# Rotate a face (simplified)
def rotate_face(face_idx, clockwise=True):
    cube[face_idx] = np.rot90(cube[face_idx], -1 if clockwise else 1)

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    draw_cube()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_1: rotate_face(0)  # Front
            elif event.key == K_2: rotate_face(1)  # Back
            elif event.key == K_3: rotate_face(2)  # Left
            elif event.key == K_4: rotate_face(3)  # Right
            elif event.key == K_5: rotate_face(4)  # Top
            elif event.key == K_6: rotate_face(5)  # Bottom
    
    pygame.display.flip()

pygame.quit()