from itertools import count, product
from math import sin, cos, pi
import pygame


SIDE = 600

screen = pygame.display.set_mode((SIDE, SIDE))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_pixel(screen, x, y, colour):
    x, y = round(x), round(y)
    for dx, dy in product(range(-1, 2), repeat=2):
        screen.set_at((x + dx, y + dy), colour)


def circle(percentage):
    """Accepts a percentage and returns a position.
    “Parametrisation” of the circle.
    """
    return (
        SIDE // 2 + SIDE // 3 * cos(2 * pi * percentage),
        SIDE // 2 + SIDE // 3 * sin(2 * pi * percentage),
    )


def eight(percentage):
    return (
        SIDE // 2 + SIDE // 3 * sin(4 * pi * percentage),
        SIDE // 2 + SIDE // 3 * cos(2 * pi * percentage),
    )


def spiral(percentage):
    return (
        SIDE // 2 + percentage * SIDE // 3 * cos(10 * pi * percentage),
        SIDE // 2 + percentage * SIDE // 3 * sin(10 * pi * percentage),
    )


def morph(p1, p2, alpha):
    def parametrisation(percentage):
        x1, y1 = p1(percentage)
        x2, y2 = p2(percentage)
        return (
            x1 + (x2 - x1) * alpha,
            y1 + (y2 - y1) * alpha,
        )

    return parametrisation


def rotating_spiral(percentage, time):
    return (
        SIDE // 2
        + (1 + sin(time) / 10)
        * percentage
        * SIDE
        // 3
        * cos(10 * pi * percentage + time),
        SIDE // 2
        + (1 + sin(time) / 10)
        * percentage
        * SIDE
        // 3
        * sin(10 * pi * percentage + time),
    )


screen.fill(WHITE)


def bg(time):
    return (
        40 + 30 * abs(sin(0.1 * time)),
        40 + 30 * abs(sin(0.1 * time)),
        40 + 30 * abs(sin(0.1 * time)),
    )


def fg(time):
    return (
        255 - abs(15 * sin(0.05 * time)),
        85 + abs(160 * sin(0.05 * time)),
        85 + abs(60 * sin(0.05 * time)),
    )


BLENDING_STEPS = 100
for tick in count(step=0.1):
    screen.fill(bg(tick))

    STEPS = 3000
    clr = fg(tick)
    for step in range(STEPS + 1):
        percentage = step / STEPS
        x, y = rotating_spiral(percentage, tick)
        draw_pixel(screen, x, y, clr)
    pygame.display.flip()
input()


"""
BLENDING_STEPS = 100
for tick in count():
    screen.fill(WHITE)
    alpha = blending_step / BLENDING_STEPS
    p = morph(circle, spiral, alpha)

    STEPS = 3000
    for step in range(STEPS + 1):
        percentage = step / STEPS
        x, y = p(percentage)
        draw_pixel(screen, x, y, BLACK)
    pygame.display.flip()
input()
"""
