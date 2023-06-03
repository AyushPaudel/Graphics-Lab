import math
import sys, pygame
from pygame import event, gfxdraw
from pygame.locals import *
pygame.init()

display_info = pygame.display.Info()
width = display_info.current_w
height = display_info.current_h

screen_resultuion = "The screen resolution is {}p X {}p.".format(width, height)

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("Lab 2 --DDA")

window.fill((0,0,0))
pygame.display.flip()
RED = Color("#C8102E")

def bresenham(x1,y1, x2,y2):
	
    dx = x2-x1
    dy = y2-y1
    m = dy / dx
    if m < 1:
        D = 2 * dy - dx
        gfxdraw.pixel(window, x1, y1, RED)
        y = y1
        for x in range(x1+1, x2+1):
            if D>0: 
                y+=1
                gfxdraw.pixel(window,x,y,RED)
                D -= 2*(dy-dx)
            else:
                gfxdraw.pixel(window, x,y,RED)
                D += 2*dy

    else:
        D = 2 *dx
        gfxdraw.pixel(window, x1, y1, RED)
        x = x1
        for y in range(y1, y2+1):
             gfxdraw.pixel(window,x,y, RED)

             D += dx
             if D >=0:
                  x +=1
                  D -= 2 * (y2-y1)
    
    pygame.display.flip()

bresenham(10,10,500,500)



while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

# WHITE = Color("#FFFFFF")

# window.fill(WHITE)
# pygame.display.flip()

# white=(255,255,255)

# def ROUND(n):
# 	return int(n+0.5)

# def dda(x1,y1,x2,y2):
# 	x,y = x1,y1
# 	length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
# 	dx = (x2-x1)/float(length)
# 	dy = (y2-y1)/float(length)
# 	gfxdraw.pixel(window,ROUND(x),ROUND(y),(0,0,0))

# 	for i in range(length):
# 		x+= dx
# 		y+= dy
# 		gfxdraw.pixel(window,ROUND(x),ROUND(y),(0,0,0))
# 	pygame.display.flip()

# dda(10,10,500,500)

# ------------------------------------------------------
