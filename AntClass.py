import pygame, random, math

class Ant(object):
    def __init__(self):
        self.x, self.y = 300,300
        self.wanderAmount = 0.1
        # self.direction = [0,0]
        self.color = (255,255,255)
        self.body = pygame.Surface((10,10)) #10x10 pixel square
        self.body.fill(self.color)
        self.id = 0
        self.speed = 1
        self.angle = 0
        self.direction = [math.cos(self.angle)*self.speed, math.sin(self.angle)*self.speed]
        self.targetAngle = None

        self.foodId = None
        # f = open("C:/Users/joshl/OneDrive/Desktop/pygame/AntsCrawling/AntData/Ant#"+str(self.id)+".txt","w+")
        # f.close()
        self.log = ""
        # self.body.convert()
    
    def logActions(self, message):
        f = open("C:/Users/joshl/OneDrive/Desktop/pygame/AntsCrawling/AntData/Ant#"+str(self.id)+".txt","a+")
        f.write(message+"\n")
        f.close()

    def move(self, spaceToExploreLimits):
        self.direction = [math.cos(self.angle)*self.speed, math.sin(self.angle)*self.speed]
        # print(self.angle)
        if self.x + 10 + self.direction[0] < spaceToExploreLimits[0] and self.x + self.direction[0] > 0:
            self.x += self.direction[0] * 0.5
            self.log += "X -> "+str(self.x)
        else:
            self.direction[0] *= -1
            self.log += "X -> "+str(self.x)
        if self.y + 10 + self.direction[1] < spaceToExploreLimits[1] and self.y + self.direction[1] > 0:
            self.y += self.direction[1] * 0.5
            self.log += "X -> "+str(self.x)
        else:
            self.direction[1] *= -1
            self.log += "X -> "+str(self.x)
    def wander(self, spaceToExploreLimits, availableFood):
        # while self.angle > 360:
        #     self.angle = self.angle-360
        # while self.angle < 0:
        #     self.angle = self.angle+360
        self.findFood(availableFood)
        if self.targetAngle == None:
            if random.randint(0,1) == 0:
                self.angle += self.wanderAmount
            else:
                self.angle += self.wanderAmount * -1
            self.move(spaceToExploreLimits)
        else:
            self.angle = self.targetAngle
            # self.direction = [round(math.cos(self.angle)*self.speed), round(math.sin(self.angle)*self.speed)]
            print(str(round(self.angle))+":"+str(round(self.targetAngle)))
            self.move(spaceToExploreLimits)
    
    def display(self, screen):
        screen.blit(self.body, (self.x, self.y))
        
    def findFood(self, foodArray):
        closestDistance = 10000000
        for i in range(len(foodArray)):
            distanceToFood = math.sqrt((foodArray[i].y - self.y)**2 + (foodArray[i].x - self.x)**2)
            if distanceToFood < closestDistance:
                closestDistance = distanceToFood
        if closestDistance != 10000000 and (distanceToFood <= 100 and distanceToFood != 0):
            changeInY = (foodArray[i].y - self.y)
            self.targetAngle = math.asin((changeInY/distanceToFood)) + self.angle
            self.foodId = foodArray[i].id
        elif distanceToFood == 0:
            pass
        else:
            self.targetAngle = None
        

