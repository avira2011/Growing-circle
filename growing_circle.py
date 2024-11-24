import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill('black')
pygame.display.update()

class Grow_Circle():
    
    def __init__(self,color, pos, radius):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.surface = screen

    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface,self.color, self.pos, self.radius)

    def grow(self,radius):
        self.radius = self.radius+radius
        self.draw_circle = pygame.draw.circle(self.surface,self.color, self.pos, self.radius)
    

white_circle = Grow_Circle('white',(300,300), 25)

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill('black')
            white_circle.draw() 
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            screen.fill('black')
            white_circle.grow(20) 
            pygame.display.update()

