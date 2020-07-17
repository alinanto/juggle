import pygame
import sys
from pygame.locals import *
pygame.init()

#define Classes

class Ball :
    def __init__(self,image_file,x,y,dx,dy) :
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.iBall = pygame.image.load(image_file).convert_alpha()
        self.rBall = self.iBall.get_rect()
        screen.blit(self.iBall,self.rBall.move(self.x,self.y))
        pygame.display.update(self.rBall.move(self.x,self.y))
        self.height = self.iBall.get_height()
        self.width = self.iBall.get_width()
        self.sideCollide = 0
        self.faceCollide = 1
    def update(self) :
        screen.blit(iBackground,self.rBall.move(self.x,self.y),self.rBall.move(self.x,self.y))
        pygame.display.update(self.rBall.move(self.x,self.y))
        self.x += self.dx
        self.y += self.dy
        if (self.x <= 0 and self.dx<0) or (self.x >= WIDTH-self.width and self.dx>0):
            self.dx *= -1 
        if (self.y <= 0 and self.dy<0) or (self.y >= HEIGHT-self.height and self.dy>0):
            self.dy *= -1
        playerCollide = self.rBall.move(self.x,self.y).colliderect(player.rPlayer.move(player.x,player.y))
        boundaryCollide = self.rBall.move(self.x,self.y).colliderect(boundary)
        if boundaryCollide and not playerCollide : self.sideCollide = 1
        if not boundaryCollide :
            self.sideCollide = 0
            self.faceCollide = 1 
        if self.sideCollide and playerCollide :        
            self.dx *= -1
            self.x += self.dx
            self.sideCollide = 0
            self.faceCollide = 0
        elif self.faceCollide and playerCollide :
            self.dy *= -1
            self.y += self.dy
            self.faceCollide = 0;
        screen.blit(self.iBall,self.rBall.move(self.x,self.y))
        pygame.display.update(self.rBall.move(self.x,self.y))

class Player :
    def __init__(self,image_file) :
        self.x = PLAYER_XINT 
        self.y = PLAYER_YINT
        self.dx = 0
        self.iPlayer = pygame.image.load(image_file).convert_alpha()
        self.rPlayer = self.iPlayer.get_rect()
        screen.blit(self.iPlayer,self.rPlayer.move(self.x,self.y))
        pygame.display.update(self.rPlayer.move(self.x,self.y))
        self.width = self.iPlayer.get_width()
        self.height = self.iPlayer.get_height()
    def update(self) :
        screen.blit(iBackground,self.rPlayer.move(self.x,self.y),self.rPlayer.move(self.x,self.y))
        pygame.display.update(self.rPlayer.move(self.x,self.y))
        self.x += self.dx
        if self.x<0 :
            self.x = 0
            self.dx = 0
        if self.x>WIDTH-self.width :
            self.x = WIDTH-self.width
            self.dx = 0        
        screen.blit(self.iPlayer,self.rPlayer.move(self.x,self.y))
        pygame.display.update(self.rPlayer.move(self.x,self.y))

# initialisation of constants

FBACKGROUND = 'bg1.png'
FBALL = 'ball.png'
FPLAYER = 'player.png'
iBackground = pygame.image.load(FBACKGROUND)
WIDTH = iBackground.get_width()
HEIGHT = iBackground.get_height()
BALL1_XINT = int(WIDTH*0.5)
BALL1_YINT = int(HEIGHT*0.1)
BALL2_XINT = int(WIDTH*0.5)
BALL2_YINT = int(HEIGHT*0.7)
BALL_XSPEED = 10
BALL_YSPEED = 10
PLAYER_XINT = WIDTH//2
PLAYER_YINT = int(HEIGHT*0.9) 
PLAYER_SPEED = 15
ANIMATOR = pygame.USEREVENT+1
FPS = 40
screen = pygame.display.set_mode((WIDTH,HEIGHT))
iBackground = iBackground.convert_alpha()
        
#initialising display and event loop and creating objects
        
screen.blit(iBackground,(0,0))
pygame.display.update()
print('Display resolution set as',str(WIDTH)+'x'+str(HEIGHT))
ball1 = Ball(FBALL,  
            BALL1_XINT,
            BALL1_YINT,
            BALL_XSPEED,
            BALL_YSPEED)
ball2 = Ball(FBALL,  
            BALL2_XINT,
            BALL2_YINT,
            -BALL_XSPEED,
            BALL_YSPEED)

player = Player(FPLAYER)
boundary = pygame.Rect(0,PLAYER_YINT,WIDTH,player.height)
pygame.time.set_timer(ANIMATOR,1000//FPS)

while 1:
    for event  in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if(event.key == K_LEFT) : player.dx = -PLAYER_SPEED
            if(event.key == K_RIGHT) : player.dx = +PLAYER_SPEED
        if event.type == pygame.KEYUP:
            if(event.key == K_LEFT and player.dx<0) : player.dx = 0
            if(event.key == K_RIGHT and player.dx>0) : player.dx = 0
        if event.type == ANIMATOR :
            ball1.update()
            ball2.update()
            player.update()
                    
    
