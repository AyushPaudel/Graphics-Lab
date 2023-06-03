import math
import pygame
from pygame import event
from pygame.locals import *

pygame.init()

display_info = pygame.display.Info()
width = display_info.current_w
height = display_info.current_h

screen_resultuion = "The screen resolution is {}p X {}p.".format(width, height)


window = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Lab 1 - Flag")

RED = Color("#C8102E")
CRIMSON = Color("#DC143C")
DARK_BLUE = Color("#003893")
BLUE = Color("#003087")
WHITE = Color("#FFFFFF")
BLACK = Color("#000000")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        # close when [X] is pressed
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    window.fill(WHITE)

    border = 12

    # upper outer triangle
    pygame.draw.polygon(
        window,
        DARK_BLUE,
        [
            (100 - border, 100 - 2 * border),
            (100 - border, 300 + border),
            (400 + 3 * border, 300 + border),
        ],
    )

    # # lower outer triangle
    pygame.draw.polygon(
        window,
        DARK_BLUE,
        [
            (100 - border, 200- 2 * border - 5),
            (100 - border, 500 + border),
            (400 + 2 * border + 5, 500 + border),
        ],
    )

    # # upper inner triangle
    pygame.draw.polygon(window, CRIMSON, [(100, 100), (100, 300), (400, 300)])

    # # lower inner triangle
    pygame.draw.polygon(window, CRIMSON, [(100, 200), (100, 500), (400, 500)])

    # # drawing the sun
    number_of_points = 12
    point_list = []
    center_x = 175
    center_y = 400
    for i in range(number_of_points * 2):
        radius = 60
        if i % 2 != 0:
            radius = radius // 1.5
            pass
        angle = i * math.pi / number_of_points
        x = center_x + int(math.cos(angle) * radius)
        y = center_y + int(math.sin(angle) * radius)
        point_list.append((x, y))

    pygame.draw.polygon(window, WHITE, point_list)

    # # drawing the moon
    pygame.draw.circle(window, WHITE, (175, 234), 60)
    pygame.draw.circle(window, CRIMSON, (175, 220), 58)
    number_of_points = 16
    point_list = []
    center_x = 175
    center_y = 260
    for i in range(number_of_points * 2):
        radius = 40
        if i % 2 == 0:
            radius = radius // 1.3
        angle = i * math.pi / number_of_points
        x = center_x + int(math.cos(angle) * radius)
        y = center_y + int(math.sin(angle) * radius)
        point_list.append((x, y))
    del point_list[5:13]
    pygame.draw.polygon(window, WHITE, point_list)

    # font = pygame.font.SysFont("arial", 28)
    # font_2 = pygame.font.SysFont("helvetiva", 18)
    # text = font.render("National Flag of Nepal", True, BLACK)
    # resolution = font_2.render(screen_resultuion, True, BLACK)
    # window.blit(text, (97, 530))
    # window.blit(resolution, (200, 580))
    
    pygame.display.flip()
    clock.tick()
pygame.quit()
