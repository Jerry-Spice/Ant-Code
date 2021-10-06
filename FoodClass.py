import pygame, random, math


class Food(object):
    def __init__(self, x, y, id, value):
        self.x = x
        self.y = y
        self.id=id
        self.value=value
        self.body = pygame.Surface((5,5))
        self.body.fill((255,255,0))
        self.body.convert()
    
    def display(self, screen):
        screen.blit(self.body, (self.x, self.y))