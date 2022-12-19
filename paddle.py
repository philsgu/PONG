import pygame
#create the paddle sprite OOP
BLACK = (0,0,0)
FUNK = (255, 204, 0)
class Paddle(pygame.sprite.Sprite):
    #inherits from the "Sprite" class in pygame
    #constructor for new objects
    def __init__(self, color, width, height):
        #call the parent class (Sprite) constructor to be used
        super().__init__()

        #PASS IN THE COLOR OF THE PADDLE, ITS WIDTH AND HEIGHT
        #set BACKGROUD COLOR AND SET IT TO BE TRANSPARENT
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #DRAW THE PADDLE (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #fetch the rectangle object (x,y) method, where are you going to put the paddle object 
        self.rect = self.image.get_rect()
    #add methods to move the paddle
    def moveUp(self, pixels):
        self.rect.y -= pixels
        #check that you are NOT going too far off (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0 #bound 

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400 
