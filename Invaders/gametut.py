import pygame
import random
import math

#Initialize 
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#title
pygame.display.set_caption("Invaders")
icon = pygame.image.load('startup(1).png')
pygame.display.set_icon(icon)

#about the player
playerImg = pygame.image.load('alien.png')
playerX = 370
playerY = 480

enemyImg = []
enemyX = []
enemyY = []
enemyChangeX = []
EnemyNum = 2

for i in range(EnemyNum):
    enemyImg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyChangeX.append(0.2)
    
bulletImg = pygame.image.load('bullet.png')
bulletX = 480
bulletY = 480
bulletChangeX = 0
bulletChangeY = 0.80
bullet_state = "ready"

score = 0

def player(playerX,playerY):
    screen.blit(playerImg,(playerX,playerY))

def enemy(enemyX,enemyY,i):
    screen.blit(enemyImg[i],(enemyX,enemyY))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    P = [enemyX,enemyY]
    Q = [bulletX,bulletY]
    dist = math.dist(P,Q)
    if dist < 27:
        return True
    return False

playerChangeX = 0
#game loop
running = True
while running:
    #print(pygame.event.get())
    screen.fill((200,200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX = -0.3
            if event.key == pygame.K_RIGHT:
                playerChangeX = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                

        if event.type == pygame.KEYUP:
            playerChangeX = 0 
            
    for i in range(EnemyNum):
        enemyX[i] += enemyChangeX[i]
        if enemyX[i] <= 0:
            enemyChangeX[i] = 0.3
        if enemyX[i] >= 736:
            enemyChangeX[i] = -0.3
            enemyY[i] += 25
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score += 3
            print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    playerX += playerChangeX

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletChangeY
    #change the color
    #screen.fill((0,255,0))
    #pygame.display.update() it kept changing lol

    player(playerX,playerY)
    pygame.display.update()
    
