import pygame
from constants import *
from random import randint
from math import cos, sin


class Asteroid:
    def __init__(self, color):
        self.x = randint(0, screenSize)
        self.y = randint(0, screenSize)
        self.r = randint(25, 50)
        self.color = color
        
    def draw(self, window):
        pygame.draw.ellipse(window, self.color, (self.x, self.y, self.r * 2, self.r * 2), 1)
