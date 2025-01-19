import pygame, sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Congratulations!")
clock = pygame.time.Clock()

# Colors and fonts
WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
font = pygame.font.Font(None, 74)

# Stickman dance variables
x, y, angle = WIDTH // 2, HEIGHT // 2, 0

# Draw stickman
def draw_stickman(x, y, angle):
    # Head
    pygame.draw.circle(screen, BLACK, (x, y - 50), 30, 2)
    # Eyes
    pygame.draw.circle(screen, BLACK, (x - 10, y - 60), 5)
    pygame.draw.circle(screen, BLACK, (x + 10, y - 60), 5)
    # Smile
    pygame.draw.arc(screen, BLACK, (x - 15, y - 65, 30, 20), 3.14, 6.28, 2)
    # Body
    pygame.draw.line(screen, BLACK, (x, y - 20), (x, y + 60), 4)
    # Arms
    pygame.draw.line(screen, BLACK, (x, y - 20), (x - 50, y - 20 + angle), 4)
    pygame.draw.line(screen, BLACK, (x, y - 20), (x + 50, y - 20 - angle), 4)
    # Legs
    pygame.draw.line(screen, BLACK, (x, y + 60), (x - 30, y + 120 - angle), 4)
    pygame.draw.line(screen, BLACK, (x, y + 60), (x + 30, y + 120 + angle), 4)

# Main loop
while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    angle = (angle + 1) % 20 - 10
    draw_stickman(x, y, angle)
    text = font.render("Congratulations!!!", True, RED)
    screen.blit(text, text.get_rect(center=(WIDTH // 2, 100)))

    pygame.display.flip()
    clock.tick(30)
