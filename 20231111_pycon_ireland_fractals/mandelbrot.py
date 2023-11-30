import pygame


WIDTH = HEIGHT = 900


screen = pygame.display.set_mode((WIDTH, HEIGHT))


def f(z, c):
    return z**2 + c


MAX_ITER = 50


colours = []
for i in range(MAX_ITER + 1):
    c = pygame.Color(0, 0, 0)
    c.hsla = (
        180 * (i / MAX_ITER) ** 0.8,
        100,
        50,
        100,
    )
    colours.append(c)


for x in range(WIDTH):
    for y in range(HEIGHT):
        re = 3 * x / WIDTH - 2.3
        im = 3 * y / HEIGHT - 1.5
        c = z = complex(re, im)
        iter = 0
        while iter < MAX_ITER and abs(z) < 2:
            z = f(z, c)
            iter += 1

        screen.set_at((x, y), colours[iter])

pygame.display.flip()


while True:
    for ev in pygame.event.get():
        pass
