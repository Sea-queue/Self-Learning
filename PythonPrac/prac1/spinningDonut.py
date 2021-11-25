#import os
#from math import sin, cos
import pygame
import math
import colorsys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH = 1000
HEIGHT =700

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH //x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0 #rotating animation

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
#display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Donut")
font = pygame.font.SysFont('Arial', 18, bold=True)


def hsv2rgb(h, s, v):
    return tuple(round(i*255) for i in colorsys.hsv_to_rgb(h, s, v))

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))


# def text_display(letter, x_start, y_start):
#     text = font.render(str(letter), True, white)
#     display_surface.blit(text, (x_start, y_start))

run = True
while run:
    screen.fill(black)

    z = [0] * screen_size # Donut. Fills donut space
    b = [' '] * screen_size # Backgrond. Fills empty space

    for j in range(0, 628, theta_spacing): #from 0 to 2pi
        for i in range(0, 628, phi_spacing): # from 0 to 2pi
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int (8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]
    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00002   # controls the speed
        B += 0.00001   # controls the speed

        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator


    pygame.display.update()
    hue += 0.005

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



"""
# for some reason, the following code prints a donut at each tick
def main():
    a = 0
    b = 0

    # for clearing console (windows and unix systems)
    clear = 'cls'
    if os.name == "posix":
        clear = "clear"

    os.system(clear)

    while True:
        z = [0 for _ in range(7040)]
        screen = [' ' for _ in range (1760)]

        j = 0
        while j < 6.28:
            j +=  0.07
            i = 0
            while i < 6.28:
                i += 0.02

                sinA = sin(a)
                cosA = cos(a)
                cosB = cos(b)
                sinB = sin(b)

                sini = sin(i)
                cosi = cos(i)
                cosj = cos(j)
                sinj = sin(j)

                cosj2 = cosj + 2
                mess = 1 / (sini * cosj2 * sinA + sinj * cosA + 5)
                t = sini * cosj2 * cosA - sinj * sinA

                # 40 is the left screen shift
                x = int(40 + 30 * mess * (cosi * cosj2 * cosB - t * sinB))

                #12 is the down screen shift
                y = int(12 + 15 * mess * (cosi * cosj2 * sinB + t * cosB))

                #all are casted to int, ie floored
                o = int(x + 80 * y)
                N = int(8 * ((sinj * sinA - sini * cosj * cosA) * cosB - sini * cosj * sinA - sinj * cosA - cosi * cosj * sinB))

                if 0 < y < 22 and 0 < x < 80 and z[o] < mess:
                    z[o] = mess
                    screen[o] = ".,*~:;=!*#$@"[N if N > 0 else 0]

        # print
        os.system(clear)
        for index, char in enumerate(screen):
            if index % 80 == 0:
                print()
            else:
                print(char, end = '')

        # increments
        a += 0.04
        b += 0.02

if __name__ == "__main__":
    main()
"""
