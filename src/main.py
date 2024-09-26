import pygame
import sys
from body import Body
from vector import Vector
from math import radians, degrees, sin, cos

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Draw a Circle")

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pixels_per_meter = 500
print(f"the window width is {width/pixels_per_meter:.0f} meters")
PIXEL_SIZE = 1 / pixels_per_meter  # in meters


gravity = 9.8
Body(Vector([1, 0.5, 0]), Vector([-2, 1, 10]), Vector([0, 0, 0]))
Body(Vector([1, 0.5, 0]), Vector([2, 2, 10]), Vector([0, 0, 0]))
Body(Vector([1, 0.5, 0]), Vector([-2, 3, -10]), Vector([0, 0, 0]))
Body(Vector([1, 0.5, 0]), Vector([2, 4, -10]), Vector([0, 0, 0]))

from random import random

for _ in range(12):
    a = (random() - 1) * 2
    b = (random() - 1) * 2
    c = (random() - 1) * 2
    Body(Vector([1, 0.5, 0]), Vector([a**2, b**2, c**2]), Vector([0, 0, 0]))

# for _ in range(50):
#     body.timestep(0.1)
#     print(body.displacement)
#     body.try_bounce()
#     # print(body, end="\n\n")


# quit()
import time


def colorize(x):
    if x < 0:
        x = 0
    if x > 1:
        x = 1
    return int(x * 255)


def stamp():
    global stamp_
    old = stamp_
    stamp_ = time.time()
    elapsed = stamp_ - old
    print(f"fps: {1/elapsed:.0f}")
    return elapsed


stamp_ = time.time()

speed = 0.5  # rotation speed
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    screen.fill(BLACK)

    step = stamp()

    Body.registry = sorted(Body.registry, key=lambda x: x.depth, reverse=True)
    for _body in Body.registry:
        _body.timestep(step)
        _body.try_bounce()

        a = cos(time.time() * speed) * gravity
        b = sin(time.time() * speed) * gravity
        _body.acceleration = Vector([0, a, b])

        depth = _body.displacement.z
        brightness = 1 / (depth + 0.5)
        brightness = colorize(brightness)
        color = (brightness, brightness, brightness)
        pygame.draw.circle(
            screen,
            color,
            (_body.displacement * pixels_per_meter).vector[:2],
            _body.screen_size * pixels_per_meter,
        )

    # time.sleep(1e-1)

    # Update the display
    pygame.display.flip()
