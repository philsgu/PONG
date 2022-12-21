import pygame
import pygame_menu
from paddle import Paddle
from ball import Ball
#always initialize
pygame.init()

#define some colors
#use clasic ATAIRI like
BLACK = (0, 0, 0)
TEAL = (3, 240, 252)
RED = (252, 3, 3)
WHITE = (255, 255, 255)

#create tone for ball
pong_sound = pygame.mixer.Sound('pong_blip.wav')
#score point
score_sound = pygame.mixer.Sound('Funk.wav')
#open new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Phil Pong")

paddleA = Paddle(TEAL, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(RED, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#Create a list of spirte into Group using this Sprite class method
all_sprite_list = pygame.sprite.Group()

#Add the paddle and ball to the list of sprites
all_sprite_list.add(paddleA)
all_sprite_list.add(paddleB)
all_sprite_list.add(ball)

#pause game
# def pause():
#     loop = 1

#     write("PAUSED", 500, 150)
#     write("Press Space to continue", 500, 250)
#     while loop:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 loop = 0
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     loop = 0
#                 if event.key == pygame.K_SPACE:
#                     screen.fill((0, 0, 0))
#                     loop = 0
#         pygame.display.update()
#         # screen.fill((0, 0, 0))
#         clock.tick(60)

def play_game():
    #the loop will carry on for refresh screen
    carryOn = True

    #clock is import to control how fast the screen updates
    clock = pygame.time.Clock()

    #Initialize player score
    scoreA = 0
    scoreB = 0
    #------Main Program Loop-------
    while carryOn:
        #--- Main event loop ----
        for event in pygame.event.get(): #user did something
            if event.type == pygame.QUIT: #if user clicked close/QUIT window
                carryOn = False

        #Moving the paddles when the user uses the arrow keys (player A) or W/S keys (player B)
        keys= pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(10)
        if keys[pygame.K_s]:
            paddleA.moveDown(10)
        if keys[pygame.K_UP]:
            paddleB.moveUp (10)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown (10) 
            

        #---- Game logic should go in here ---
        all_sprite_list.update() #put the defined sprite in here 
        #Check if the ballis bouncing against any of the 4 walls
        if ball.rect.x>=690:
            scoreA +=1
            pygame.mixer.Sound.play(score_sound)
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB +=1
            pygame.mixer.Sound.play(score_sound)
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]
        
        #Detect collection between ball and paddle and random bounce if off either positive or negative direction points
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
            pygame.mixer.Sound.play(pong_sound)
            ball.bounce()


        #--- Drawing code should go here ----
        #clear the screen -----black 
        screen.fill(BLACK)
        #draw the net in the middle
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 8) #[Start X, Start point y], [End X, End Y point]

        #Draw all sprites in one go from the group sprite variable
        all_sprite_list.draw(screen)

        #Draw scorecard on top
        font = pygame.font.Font(None, 74)
        text_a = font.render(str(scoreA), 1, WHITE)
        screen.blit(text_a, (250,10))
        text_b = font.render(str(scoreB), 1, WHITE)
        screen.blit(text_b, (420, 10))


        #---- UPDATE the screen with what we've drawn up
        pygame.display.flip()


        #--- Limit to 60 frames per second
        clock.tick(60)

#play_game()
#create a menu prior to entry to play game mode
menu = pygame_menu.Menu("Phil's Pong", 400, 300)
menu.add.button('Play', play_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.add.label("Player Left Keys: W/S", font_size=14)
menu.add.label("Player Right Keys: UP/DOWN", font_size=14)
menu.mainloop(screen)
#Once we have wcited the main program loop, we can stop the game engine:
pygame.quit()
