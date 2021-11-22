import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox


class Cube:
    size = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.size
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle = (i * dis + dis - radius*2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)

class Snake:
    body = []
    turns  = {} # when head changes direction, stores pos(key), direction(value)


    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny =1


    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # index, cube
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                # after last cube hit the turning position, remove it
                if i == len(self.body) - 1:
                    self.turns.pop(p)

            else: # when hitting the edge
                # moving left, hit the left edge
                # $$ x is colum, y is row
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.size - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.size - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.size - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == - 1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.size - 1)
                else:
                    c.move(c.dirnx, c.dirny)


    def reset(self, pos):
        pass


    def addCube(self):
        pass


    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def draw_grid(w, size, surface):

    size_btwn = w // size
    x = 0
    y = 0
    for i in range(size):
        x += size_btwn
        y += size_btwn
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    surface.fill((0, 0, 0))
    s.draw(surface)
    draw_grid(width, size, surface)
    pygame.display.update()


def random_snack(size, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, size, s
    width = 500
    size = 20
    window = pygame.display.set_mode((width, width))
    s = Snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(70)
        clock.tick(10)
        s.move()
        # somehow needs this for loop to trigger the window pop up
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         flag = False
        redraw_window(window)

main()
