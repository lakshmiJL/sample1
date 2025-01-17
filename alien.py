import pgzrun
import random
WIDTH = 600
HEIGHT = 500
alien = Actor('alien')
alien.x = WIDTH/2
alien.y = HEIGHT/2

msg = "Click on the Alien"
def draw():
    screen.fill("sky blue")
    alien.draw()
    screen.draw.text(msg,(50,50))

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        alien.x = random.randint(50,550)
        alien.y = random.randint(50,450)




pgzrun.go()