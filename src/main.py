import pygame
import sys
from body import Body
from vector import Vector

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw a Circle")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)


body = Body(Vector([500, 0]), Vector([0, 0]), Vector([0, 9.8]))

# for _ in range(50):
#     body.timestep(0.1)
#     print(body.displacement)
#     body.try_bounce()
#     # print(body, end="\n\n")


# quit()
import time


def stamp():
    global elapsed
    old = stamp
    stamp = time.time()
    return stamp - old


stamp = time.time()
while True:
    print(stamp)
    time.sleep(1)
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    screen.fill(BLACK)

    # Draw a circle
    center = (width // 2, height // 2)  # Center of the screen
    radius = 50
    pygame.draw.circle(screen, RED, body.displacement.vector, radius)
    time.sleep(0.01)
    body.timestep(0.01)
    body.try_bounce()
    # Update the display
    pygame.display.flip()
