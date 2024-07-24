import pgzrun
import random



WIDTH = 1200
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,255)

#creating actors

soldier = Actor("soldier")


soldier.pos = (WIDTH//2,HEIGHT-60)

speed = 5 

#creating a list for bullets
bullets = []

#creating the list of opponents
opponents = []

score=0
direction=1
soldier.dead=False
soldier.countdown=90

#creating opponents - 8 coloms and 4 rows

for x in range (8):
    for y in range (4):
        enemy=Actor("opponent")
        opponents.append(enemy)
        opponents[-1].x = 100 + 50 * x
        opponents[-1].y = 80 + 50 * y

#updating score
def display_score():
    screen.draw.text(str(score),(30,50))

def gameover():
    screen.draw.text("Game over!!!",(250,300))
    

#pressing spacebar key to shoot bulets
def on_key_down(key):
    if soldier.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullets.append(bullet)
            bullets[-1].x=soldier.x
            bullets[-1].y=soldier.y-50

def update():
    global score ,direction
    movedown = False
    #move the soldier left # or right with arrow keys
    if soldier.dead == False:
        if keyboard.left:
            soldier.x-=speed
            if soldier.x <= 0:
                soldier.x = 0
        elif keyboard.right:
            soldier.x+=speed
            if soldier.x >=WIDTH:
                soldier.x = WIDTH
    if keyboard.space:
        bullet = Actor("bullet")
        bullets.append(bullet)
        bullets[-1].x=soldier.x
        bullets[-1].y=soldier.y-50
    #moving bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)

        else :
            bullet.y-=10
    if len(opponents) == 0:
        gameover()
    #checking the position of the last enemy to move left and right
    if len(opponents) > 0 and (opponents[0].x  < 80 or opponents[-1].x > WIDTH-80):
        movedown = True
        direction = direction*-1
    for enemy in opponents:
        enemy.x += 5*direction
        if movedown == True:
            enemy.y += 100

        if enemy.y> HEIGHT:
            opponents.remove(enemy)
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                opponents.remove(enemy)
                bullets.remove(bullet)
                if len(opponents) == 0:
                    gameover()

        if enemy.colliderect(soldier):
            soldier.dead = True
    if soldier.dead == True:
        soldier.countdown -= 1

    if soldier.countdown == 0:
        soldier.dead = False
        soldier.countdown = 90                  






def draw():
    screen.clear()
    screen.fill(BLUE)
    if soldier.dead==False:
        soldier.draw()
    for enemy in opponents:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    if len(opponents) == 0:
        gameover()



pgzrun.go()






        
