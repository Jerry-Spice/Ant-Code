import pygame, random, math

class Ant(object):
    def __init__(self):
        self.x, self.y = 300,300
        self.wanderAmount = 5
        # self.direction = [0,0]
        self.color = (255,255,255)
        self.body = pygame.Surface((10,10)) #10x10 pixel square
        self.body.fill(self.color)
        self.id = 0
        self.speed = 5
        self.angle = 180
        self.direction = [math.cos(self.angle*(math.pi/180)) / self.speed, math.sin(self.angle*(math.pi/180)) / self.speed]
        
        self.targetAngle = None

        self.foodId = None
        # self.body.convert()
    
    def move(self, spaceToExploreLimits):
        self.direction = [math.cos(self.angle*(math.pi/180)) / self.speed, math.sin(self.angle*(math.pi/180)) / self.speed]
        # print(self.direction)
        print(self.angle)
        if self.x + 10 + self.direction[0] < spaceToExploreLimits[0] and self.x + self.direction[0] > 0:
            self.x += self.direction[0]
        else:
            self.direction[0] *= -1
        if self.y + 10 + self.direction[1] < spaceToExploreLimits[1] and self.y + self.direction[1] > 0:
            self.y += self.direction[1]
        else:
            self.direction[1] *= -1
    

    def wander(self, spaceToExploreLimits, availableFood):
        if self.targetAngle == None:
            if random.randint(0,1) == 0:
                self.angle += self.wanderAmount
            else:
                self.angle += self.wanderAmount * -1
            self.move(spaceToExploreLimits)
        else:
            self.angle = self.targetAngle
            self.move(spaceToExploreLimits)
    
    def display(self, screen):
        screen.blit(self.body, (self.x, self.y))
        
    def findFood(self, availableFood):
        closestDistance = 10000000000
        closestId = -1
        for food in availableFood:
            closestDistance = math.sqrt((self.x - food.x)**2 + (self.y - food.y)**2) if math.sqrt((self.x - food.x)**2 + (self.y - food.y)**2) < closestDistance else closestDistance
            closestId = food.id if closestDistance == math.sqrt((self.x - food.x)**2 + (self.y - food.y)**2) else closestId
        if closestDistance != 0 or closestDistance != 10000000000 and closestId != -1:
            """Todo:
                add find food method by finding the x difference and then the cos (SohCahToa) for the target angle
            """
            self.targetAngle = math.cos()
        

