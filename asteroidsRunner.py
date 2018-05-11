import pygame, sys
from pygame.locals import *
from constants import *
from ship import *
from asteroids import *

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))

ship = Ship(screenSize // 2, screenSize // 2, white)
asteroids = []

for num in range(5):
    asteroids.append(Asteroid(white))

def keyPressed(left, right, forward):
    if event.type == KEYDOWN and event.key == left:
        ship.setRotation(-0.1)
    elif event.type == KEYDOWN and event.key == right:
        ship.setRotation(0.1)
    elif event.type == KEYDOWN and event.key == forward:
        ship.isBoosting = True

    # DEBUG
    # Resets ship to center, changes velocity to 0, and points ship to right
    elif event.type == KEYDOWN and event.key == K_SPACE:
        ship.x = width // 2
        ship.y = height // 2
        ship.velocity = [0, 0]
        ship.heading = 0


def keyReleased(left, right, forward):
    if event.type == KEYUP and (event.key == left or event.key == right):
        ship.setRotation(0)
    elif event.type == KEYUP and event.key == forward:
        ship.isBoosting = False


while True:
    FPS = 60
    pygame.time.wait(1000//FPS)

    screen.fill(black)

    ship.draw(screen)
    ship.turn()
    ship.update()
    ship.wrap()
    
    for asteroid in asteroids:
        asteroid.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        keyPressed(K_a, K_d, K_w)
        keyReleased(K_a, K_d, K_w)
