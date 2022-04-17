#generl setup
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])

class Player(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 80

    def draw(self):
        color = (255,182,193)
        return pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y,self.width,self.height))

class Ball(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.width = 25
        self.height = 25
        self.movex = .5
        self.movey = .5

    def draw(self):
        color = (0,255,0)
        return pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y,self.width,self.height))

    def move(self):
        self.x += self.movex
        self.y += self.movey

p1 = Player(0,300)
p2 = Player(790,250)
ball = Ball()
pygame.display.set_caption('PONG')
score1 = 0
score2 = 0

#Main
running = True
GameStop = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    player1data = p1.draw()
    player2data = p2.draw()
    ball.draw()

    
    if GameStop:
        ball.move()
    #ball.move()
    #color = (100,255,255)
    #x = 0
    #y = 0
    #wid = 20
    #hei = 100
    #pygame.draw.rect(screen,color,pygame.Rect(x,y,wid,hei))

    #keyboard stuff
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE]:
        GameStop = True
    if key_input[pygame.K_UP]:
        p2.y -= .75
    if key_input[pygame.K_DOWN]:
        p2.y += .75
    if key_input[pygame.K_w]:
        p1.y -= .75
    if key_input[pygame.K_s]:
        p1.y += .75

#WALL Code ----v
    vallBottom = pygame.draw.rect(screen,(0,0,255),pygame.Rect(0,590,800,5))
    vallTop = pygame.draw.rect(screen,(0,0,255),pygame.Rect(0,0,800,5))
    if vallBottom.collidepoint((ball.x,ball.y))or vallTop.collidepoint((ball.x,ball.y)):
        ball.movey = - ball.movey

    if player1data.collidepoint((ball.x,ball.y)) or player2data.collidepoint((ball.x,ball.y)):
        ball.movex= -ball.movex

    if ball.x > p2.x+5:
        score2 += 1
        ball.x = 400
        ball.y = 300
        GameStop = False
    elif ball.x < p1.x:
        score1 += 1
        ball.x = 400
        ball.y = 300
        GameStop = False

    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render('Player 1: ' + str(score1),True,(255,0,0),(100,255,0))
    textRect = text.get_rect()
    textRect.center = (500,590)
    screen.blit(text,textRect)

    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render('Player 2: ' + str(score2),True,(255,0,0),(100,255,0))
    textRect = text.get_rect()
    textRect.center = (200,590)
    screen.blit(text,textRect)
    pygame.display.update()

#closing
pygame.quit()
