import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

TITLE = "Space Journey"
FPS = 30

# Variable
mode = "menu"

# Enemy Function
def new_enemy():
    enemy = Actor('enemy', (random.randint(0, WIDTH), random.randint(-450, -50)))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

def enemy_ship():    
    for enemy in enemies:
        if enemy.y < HEIGHT:
            enemy.y += enemy.speed
        else:
            enemies.remove(enemy)
            new_enemy()

# Planet Function
def planet():
    if planets[0].y < HEIGHT + 100:
        planets[0].y += 1
    else:
        p = planets.pop(0)
        planets.append(p)

def meteorites():
    for meteor in meteors:
        if meteor.y < HEIGHT:
            meteor.y += meteor.speed
        else:
            meteor.x = random.randint(0, WIDTH)
            meteor.y = random.randint(-450, -50)
            meteor.speed = random.randint(4, 11)

#Bullet Function
def bullet_move():
    for bullet in bullets:
        if bullet.y >= 0:
            bullet.y -= 12
        else:
            bullets.remove(bullet)

# Collision Function
def collision():
    global mode
    global count
    
    for enemy in enemies:
        if ship.colliderect(enemy):
            mode = "end"
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                count += 1
                new_enemy()
                break

background = Actor('space')
ship = Actor('ship', (WIDTH / 2, HEIGHT - 50))

type1 = Actor('ship1', (WIDTH / 4, HEIGHT / 2))
type2 = Actor('ship2', (WIDTH / 2, HEIGHT / 2))
type3 = Actor('ship3', (WIDTH / 4 * 3, HEIGHT / 2))

planets = [Actor('plan1', (random.randint(0, WIDTH), -100)), Actor('plan2', (random.randint(0, WIDTH), -100)), Actor('plan3', (random.randint(0, WIDTH), -100)), ]

enemies = []
meteors = []
bullets = []

count = 0

for i in range(5):
    new_enemy()
    
    meteor = Actor('meteor', (random.randint(0, WIDTH), random.randint(-450, -50)))
    meteor.speed = random.randint(4, 11)
    meteors.append(meteor)
    
def draw():
    background.draw()
    
    if mode == "game":
        planets[0].draw()
        
        for meteor in meteors:
            meteor.draw()
        for bullet in bullets:
            bullet.draw()
        ship.draw()
        
        for enemy in enemies:
            enemy.draw()
        
        screen.draw.text(str(count), pos=(20, 20), color="white", fontsize = 60)
            
    elif mode == "menu":
        screen.draw.text("Select Your Ship", center=(WIDTH / 2, HEIGHT / 2 - 150), color="white", fontsize = 80)
        
        type1.draw()
        type2.draw()
        type3.draw()
        
        
    else:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2 - 50), color="white", fontsize = 111)
        screen.draw.text("Your Score: " + str(count), center=(WIDTH / 2, HEIGHT / 2 + 25), color="white", fontsize = 65)
        screen.draw.text("Press Space to Restart", center=(WIDTH / 2, HEIGHT / 2 + 185), color="white", fontsize = 70)

def on_mouse_move(pos):
    ship.pos = pos

def on_mouse_down(button, pos):
    global mode
    
    if mode == "menu" and type1.collidepoint(pos):
        ship.image = "ship1"
        mode = "game"
    elif mode == "menu" and type2.collidepoint(pos):
        ship.image = "ship2"
        mode = "game"
    elif mode == "menu" and type3.collidepoint(pos):
        ship.image = "ship3"
        mode = "game"
    
    if mode == "game" and button == mouse.LEFT:
        bullet = Actor('missiles', ship.pos)
        bullets.append(bullet)
# Update Function
def update(dt):
    global mode
        
    if mode == "game":
        enemy_ship()
        collision()
        planet()
        meteorites()
        bullet_move()
        
    elif mode == "end" and keyboard.space:
        enemies.clear()
                
        for n in range(5):
            new_enemy()
                        
        mode = "game"

pgzrun.go()

