import pygame
import math
import random
from tkinter import *
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
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)

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
        # somehow needs this for loop to trigger the window to pop up
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
        self.head = Cube(pos) # give a new head
        self.body = [] # clear the body
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        # moving to the right
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        # moving to the left
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


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
    cube1 = Cube(random_snack(width, snake), color = (0, 255, 0))
    cube1.draw(surface)
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(width, size, surface)
    pygame.display.update()


def random_snack(size, item):
    positions = item.body

    while True:
        x = random.randrange(size)
        y = random.randrange(size)
        if len(list(filter(lambda z:z.pos == (x, y), positions))) > 0:
            continue
        else:
            break
    return (x, y)


def message_box(subject, content):
    root = Tk()
    root.geometry("300x200")
    messagebox.showinfo(subject, content)


def main():
    global width, size, snake, snack
    width = 500
    size = 20
    window = pygame.display.set_mode((width, width))
    snake = Snake((255, 0, 0), (10, 10))
    snack = Cube(random_snack(size, snake), color = (0, 255, 0))
    snake.addCube()
    flag = True
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(70)
        clock.tick(10)
        snake.move()
        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(random_snack(size, snake), color = (0, 255, 0))

        # print the score reset the game when the snake hit itself
        for x in range(len(snake.body)):
            if snake.body[0].pos in list(map(lambda z:z.pos, snake.body[x+1:])):
                 print('Score: ', len(snake.body))
                 # might be a MAC problem
                 #message_box("You Lost!", 'play again...')
                 snake.reset((10, 10))
                 break
        redraw_window(window)

main()
