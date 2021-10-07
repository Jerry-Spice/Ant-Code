import pygame, sys, random, time
from pygame.locals import *

from AntClass import *
from FoodClass import *

pygame.init()

screen = pygame.display.set_mode((600,600))

background = pygame.Surface(screen.get_size())
background.fill((100,210,100))
background.convert()

ants = []

for i in range(1):
    ants.append(Ant())
    ants[-1].x = random.randint(200,400)
    ants[-1].y = random.randint(200,400)
    ants[-1].color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    ants[-1].body.fill(ants[-1].color)
    ants[-1].id = i

foods = []
for i in range(10):
    foods.append(Food(random.randint(0,600),random.randint(0,600),0,10))


while True:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            # for i in range(len(ants)):
            #     ants[i].logActions(ants[i].log)
            pygame.quit()
            sys.exit()
    for i in range(len(ants)):
        viewCircle = pygame.Surface((600,600), pygame.SRCALPHA)
        pygame.draw.circle(viewCircle,(255,255,255,100),(ants[i].x+5, ants[i].y+5),100)
        screen.blit(viewCircle, (0,0))
        ants[i].wander([screen.get_size()[0],screen.get_size()[1]], foods)
        ants[i].display(screen)
    for i in range(len(foods)):
        foods[i].display(screen)
    for ant in ants:
        for food in foods:
            if (ant.x-5 > food.x-2.5) and (ant.x+5 < food.x+2.5) and (ant.y-5 > food.y-2.5) and (ant.y+5 < food.y+2.5):
                del food
    pygame.display.flip()
