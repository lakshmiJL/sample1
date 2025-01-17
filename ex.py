import pgzrun
from random import randint

TITLE = "Collect Flowers"
WIDTH = 500
HEIGHT = 400

score = 0
game_over = False
score_displayed = False

bee = Actor("bee.png")
bee.pos = (100, 50)
flower = Actor("flower.png")
flower.pos = (100, 200)

def draw():
    screen.blit("background.png", (0, 0))
    bee.draw()
    flower.draw()
    
    if game_over:
        screen.fill("red")
        screen.draw.text("Time's Up!, your final score is " + str(score),
                         midtop=(WIDTH / 2, 10),
                         fontsize=15,
                         color="yellow")
    elif score_displayed:
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

def place_flower():
    flower.x = randint(55, WIDTH - 55)
    flower.y = randint(55, HEIGHT - 55)

def time_up():
    global game_over
    game_over = True

def show_score():
    global score_displayed
    score_displayed = True

def update():
    global score, game_over, score_displayed
    
    if not game_over:
        if keyboard.a:
            bee.x -= 5
        if keyboard.d:
            bee.x += 5
        if keyboard.w:
            bee.y -= 5
        if keyboard.s:
            bee.y += 5

        if bee.colliderect(flower):
            score += 1
            place_flower()
    
    if score > 1 and not score_displayed:
        clock.schedule_unique(show_score, 5.0)

clock.schedule(time_up, 60.0)
pgzrun.go()
