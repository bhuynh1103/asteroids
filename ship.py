import pygame
from math import sin, cos, pi
from constants import *


def deg(degrees):
    radian = degrees * (pi/180)
    return radian


def rotate(x, y, angle):
    X = x * cos(angle) - y * sin(angle)
    Y = y * cos(angle) + x * sin(angle)
    return [X, Y]


def translate(x, y, shiftX, shiftY):
    X = x + shiftX
    Y = y + shiftY
    return [X, Y]


class Ship:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.r = 20
        self.heading = 0
        self.rotation = 0
        self.velocity = [0, 0]
        self.isBoosting = False
        self.color = color

    def boosting(self, boolean):
        self.isBoosting = boolean

    def update(self):
        if self.isBoosting:
            self.boost()
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        friction = 0.97
        self.velocity[0] *= friction
        self.velocity[1] *= friction

    def boost(self):
        force = [cos(self.heading) * 0.25, sin(self.heading) * 0.25]
        self.velocity[0] += force[0]
        self.velocity[1] += force[1]

    def wrap(self):
    # Wraps x
        if self.x > screenSize + self.r:
            self.x = -self.r
        elif self.x < -self.r:
            self.x = screenSize + self.r

    # Wraps y
        if self.y > screenSize + self.r:
            self.y = -self.r
        elif self.y < -self.r:
            self.y = screenSize + self.r

    def draw(self, window):
    # Assigns points based on radius of triangle
        port = [(- self.r), self.r]
        starboard = [self.r, self.r]
        forward = [0, (- self.r)]

    #  Rotates points according to heading in degrees
        port = rotate(port[0], port[1], self.heading + deg(90))
        starboard = rotate(starboard[0], starboard[1], self.heading + deg(90))
        forward = rotate(forward[0], forward[1], self.heading + deg(90))

    # Translates points according to x and y
        port = translate(port[0], port[1], self.x, self.y)
        starboard = translate(starboard[0], starboard[1], self.x, self.y)
        forward = translate(forward[0], forward[1], self.x, self.y)

    # Draws triangle
        pygame.draw.polygon(window, self.color, (port, starboard, forward), 1)

    # DEBUG
    # Draws points on vertices of triangle
    #     pygame.draw.ellipse(window, red, (port[0], port[1], 5, 5))
    #     pygame.draw.ellipse(window, green, (starboard[0], starboard[1], 5, 5))
    #     pygame.draw.ellipse(window, blue, (forward[0], forward[1], 5, 5))


    def setRotation(self, angle):
        self.rotation = angle

    def turn(self):
        self.heading += self.rotation