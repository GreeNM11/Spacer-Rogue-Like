
#import direct
from player import *
from enemyHealthbar import *
from enemyBullet import *

ENEMY_IMAGE1 = pygame.image.load(os.path.join(sprites_folder, 'enemy1.png')) # ENEMY1 Model
ENEMY_IMAGE2 = pygame.image.load(os.path.join(sprites_folder, 'enemy2.png')) # ENEMY2 Model

global enemy_group, enemyList, bullet_group, player

# Enemy Class

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, multiplier, type):
        super().__init__()
        # Enemy Sprite
        self.image = ENEMY_IMAGE1
        self.rect = self.image.get_rect()
        self.type = type
        self.size = 0
        # Center
        self.x = x
        self.y = y
        self.displayX = self.x
        self.displayY = self.y
        self.direction = ""
        # Move FPS
        self.frame = 8
        self.frameCounter = self.frame
        # Enemy Stats
        self.multiplier = multiplier
        self.playerD = 0
        self.moveSpeed = 0
        self.totalHealth = 0
        self.health = 0
        self.money = 0
        self.damage = 0
        # Enemy Dash
        self.dashTimer = 4 * (60) # Second
        self.dashCounter = 0
        self.dashDistance = 0 # Pixel
        self.dashSpeed = 0 # Pixels Per Second
        self.dashDistanceCounter = 0
        # Dash Tracker
        self.dashX = 0
        self.dashY = 0
        # Enemy Action Tracker
        self.dash = False
        self.collide = False
        self.face_player = False
        # Sets Enemy Type
        Enemy.setType(self)
        Enemy.enemyHealthbar(self)

    def setType(self):
        if self.type == 1:
            Enemy.enemy1(self)
        if self.type == 2:
            Enemy.enemy2(self)

    def enemy1(self): # Basic Enemy
        # Sets Stats
        self.image = ENEMY_IMAGE1
        self.size = 20
        self.moveSpeed = 1
        self.health = 5 + (0.2 * self.multiplier)
        self.totalHealth = self.health
        self.money = 1 * self.multiplier
        self.damage = 20

    def enemy2(self): # Dash Enemy
        # Sets Stats
        self.image = ENEMY_IMAGE2
        self.size = 24
        self.moveSpeed = 0.5
        self.health = 9 + (0.2 * self.multiplier)
        self.totalHealth = self.health
        self.money = 3 * self.multiplier
        # Sets Dash Stats
        self.dash = True
        self.dashTimer = 1.2 * (60) # Second
        self.dashDistance = 70
        self.dashSpeed = 3
        self.damage = 30
        # Misc
        self.face_player = True

    def handleEnemy(self):
        # Gets Player Location
        playerX = Player.getX(playerList[0]) + Player.getDisplayX(playerList[0])
        playerY = Player.getY(playerList[0]) + Player.getDisplayY(playerList[0])
        # Gets Distance from Player
        self.playerD = math.sqrt((playerX - self.x) ** 2 + abs(playerY - self.y) ** 2)
        self.frameCounter += 1
        # Updates Moveset
        if self.frameCounter >= self.frame:
            self.frameCounter = 0
            self.xy = abs(playerX - self.x) >= abs(playerY - self.y)
        # Moves Enemy Toward Player without Collision of Another Enemy
        if self.collide == False:
            if self.xy:
                if playerX - self.x > 0:
                    self.x += self.moveSpeed
                elif playerX - self.x < 0:
                    self.x -= self.moveSpeed
            else:
                if playerY - self.y > 0:
                    self.y += self.moveSpeed
                elif playerY - self.y < 0:
                    self.y -= self.moveSpeed

        self.collide = False
        # Manages Dash
        if self.dash == True:
            self.dashCounter += 1
            # Dashes If Dash Timer is Available
            if self.dashTimer <= self.dashCounter:
                self.dashCounter = 0
                self.dashDistanceCounter = 0
                # Enemy Position from Player
                x = (playerX - self.x)
                y = (playerY - self.y)
                if x == 0:
                    x += 1
                if y == 0:
                    y += 1
                # Calculates Angle to Dash Toward Player
                angle = math.atan(y / x)
                self.dashX = math.cos(angle) * (self.dashSpeed)
                self.dashY = math.sin(angle) * (self.dashSpeed)

                if x < 0:
                    self.dashX = -1 * abs(self.dashX)
                if y < 0:
                    self.dashY = -1 * abs(self.dashY)
                if x > 0:
                    self.dashX = 1 * abs(self.dashX)
                if y > 0:
                    self.dashY = 1 * abs(self.dashY)
                # Rotates Sprite
                '''
                if self.face_player == True:
                    self.image = pygame.transform.rotate(self.image, 30)
                    self.rect = self.image.get_rect()
                '''
                
        # Keeps Track of Dash Distance
        if self.dashDistanceCounter < self.dashDistance:
            if self.collide == False:
                self.x += self.dashX
                self.y += self.dashY
                self.dashDistanceCounter += math.sqrt(self.dashX ** 2 + self.dashY ** 2)

    def enemyCollide(self):
        # Calculates Collision of Enemies and Stops the Further Enemy
        if pygame.sprite.spritecollideany(self, enemy_group):
            i = pygame.sprite.spritecollideany(self, enemy_group)
            if self.playerD > i.getPlayerD():
                self.collide = True

    def hitPlayer(self):
        # Determines if Enemy Collided With Player
        if pygame.sprite.spritecollideany(self, player_group):
            Player.playerHit(playerList[0], self.damage)
            self.health -= Player.getThorn(playerList[0])

    def shootBullet(self):
        # Enemy Position from Player
        x = (playerX[0] - self.x + shiftX)
        y = (playerY[0] - self.y + shiftY)
        if x == 0:
            x += 1
        if y == 0:
            y += 1
        # Calculates Angle to Shoot At Player
        angle = math.atan(y / x)
        bulletX = math.cos(angle) * (self.bullet_speed)
        bulletY = math.sin(angle) * (self.bullet_speed)

        if x < 0:
            bulletX = -1 * abs(bulletX)
        if y < 0:
            bulletY = -1 * abs(bulletY)
        if x > 0:
            bulletX = 1 * abs(bulletX)
        if y > 0:
            bulletY = 1 * abs(bulletY)
        # Creates Enemy Bullet
        bullet = EnemyBullet(self.x, self.y, bulletX, bulletY, self.type)
        enemyBullet_group.add(bullet)
        nonPlayer_group.add(bullet)

    def enemyHit(self):
        # If Enemy and Bullet Collide, Bullet Dies, Enemy Loses Health
        if pygame.sprite.spritecollideany(self, bullet_group):
            bullet = pygame.sprite.spritecollideany(self, bullet_group)
            damage = Bullet.getDamage(bullet)
            self.health -= damage
            bullet.kill()
        # Enemy Dies and Drops Money if Health is > 0
        if self.health <= 0:
            Player.playerMoney(playerList[0], self.money)
            self.healthbar.kill()
            self.kill()

    def enemyHealthbar(self):
        # Creates the Healthbar
        self.healthbar = HealthBar(self.size, self.x, self.y, self.totalHealth)
        healthbar_group.add(self.healthbar)
        nonPlayer_group.add(self.healthbar)

    def setHealthBar(self):
        # Updates Healthbar Position and Health
        HealthBar.setHealthBar(self.healthbar, self.x, self.y, self.health)

    def getPlayerD(self):
        return self.playerD
    def getMoney(self):
        return self.money
    def getDamage(self):
        return self.damage

    def displayPosition(self):
        self.displayX = self.x - playerX[0]
        self.displayY = self.y - playerY[0]

    def update(self):
        Enemy.handleEnemy(self)
        Enemy.enemyCollide(self)
        Enemy.setHealthBar(self)
        Enemy.enemyHit(self)
        Enemy.hitPlayer(self)
        Enemy.displayPosition(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))
