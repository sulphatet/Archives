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
        self.movex = .2
        self.movey = .2

    def draw(self):
        color = (0,255,0)
        return pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y,self.width,self.height))

    def move(self):
        self.x += self.movex
        self.y += self.movey

p1 = Player(0,300)
p2 = Player(790,250)
ball = Ball()


#Main
running = True
GameStop = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    p1.draw()
    p2.draw()
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
        p2.y -= .5
    if key_input[pygame.K_DOWN]:
        p2.y += .5
    if key_input[pygame.K_w]:
        p1.y -= .5
    if key_input[pygame.K_s]:
        p1.y += .5

    #WALL STUFF
    vallBottom = pygame.draw.rect(screen,(0,0,255),pygame.Rect(0,550,800,50))
    vallTop = pygame.draw.rect(screen,(0,0,255),pygame.Rect(0,0,800,50))
    if vallBottom.collidepoint((ball.x,ball.y))or vallTop.collidepoint((ball.x,ball.y)):
        ball.movey = - ball.movey

    if player1data.collidepoint((ball.x,ball.y)) or player2data.collidepoint((ball.x,ball.y)):
        ball.movex= -ball.movex

    pygame.display.update()

#closing
pygame.quit()
