import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Target!")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Target (ball)
target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)
target_dx = 5
target_dy = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

def draw_target(x, y):
    pygame.draw.circle(screen, RED, (x, y), target_radius)

def show_score():
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= target_radius:
                score += 1
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)
                target_dx = random.choice([-5, 5])
                target_dy = random.choice([-5, 5])
    
    # Move the target
    target_x += target_dx
    target_y += target_dy
    
    # Bounce off edges
    if target_x <= target_radius or target_x >= WIDTH - target_radius:
        target_dx *= -1
    if target_y <= target_radius or target_y >= HEIGHT - target_radius:
        target_dy *= -1
    
    # Draw everything
    draw_target(target_x, target_y)
    show_score()
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()