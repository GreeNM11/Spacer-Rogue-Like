
from bullet import Bullet
from globalVar import *
from chest import Chest
from playerHealthbar import PlayerHealth


  # Images

PLAYER_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'Player.png')) #  Player Model

PLAYERINVINCIBLE_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'Player_Invincible.png')) #  Player Model Invincible

  # PLAYER CLASS

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER_IMAGE
        self.rect = self.image.get_rect()
            # Center
        self.displayX = WIDTH / 2
        self.displayY = HEIGHT / 2
        self.x = self.displayX
        self.y = self.displayY

            # Speed
        self.VEL = 1.5
        self.direction = ""
            # Shoot
        self.shootCooldown = 60 / (0.7) # Per Second
        self.reload = self.shootCooldown
        self.bullet_damage = 2
        self.bullet_speed = 6
            # Dash
        self.dashDistance = 80
        self.dashCooldown = (2) * 60  # In Seconds
        self.dashTimer = self.dashCooldown
        self.dashFrame = 15 # Frames per dash
        self.dashFrameCounter = self.dashFrame # Keeps Track of Timer
            # Money
        self.playerMoney = 35
            # Health
        self.totalHealth = 100
        self.health = self.totalHealth
            # Difficulty
        self.difficulty = 1
        self.iframes = 1 * (60) # Seconds
        self.iframesTimer = self.iframes # Keeps Track of Timer
            # Player Misc
        self.thornDamage = 0
            # Player Actions
        self.death = False
        self.touchingObject = False
        self.selectedObject = None

        Player.createHealthbar(self)

    def playerMove(self): # Player Movement
        # WASD Movement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and (self.x >= borderX_left):  # LEFT
            self.x -= self.VEL
        if keys_pressed[pygame.K_d] and (self.x <= borderX_right):  # RIGHT
            self.x += self.VEL
        if keys_pressed[pygame.K_w] and (self.y >= borderY_top):  # UP
            self.y -= self.VEL
        if keys_pressed[pygame.K_s] and (self.y <= borderY_bottom):  # DOWN
            self.y += self.VEL

    def playerDirection(self):
        # Gets Player Direction
        keys_pressed = pygame.key.get_pressed()
        pressed = ""
        # UP , UP Right and Left
        if keys_pressed[pygame.K_w]:
            if keys_pressed[pygame.K_w] and keys_pressed[pygame.K_a]:
                pressed = "UPL"
            elif keys_pressed[pygame.K_w] and keys_pressed[pygame.K_d]:
                pressed = "UPR"
            elif keys_pressed[pygame.K_w] and not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                pressed = "UP"
        # DOWN, Down Right and Left
        elif keys_pressed[pygame.K_s]:
            if keys_pressed[pygame.K_s] and keys_pressed[pygame.K_a]:
                pressed = "DOWNL"
            elif keys_pressed[pygame.K_s] and keys_pressed[pygame.K_d]:
                pressed = "DOWNR"
            elif keys_pressed[pygame.K_s] and not keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_d]:
                pressed = "DOWN"
        # RIGHT
        elif keys_pressed[pygame.K_d] and not keys_pressed[pygame.K_w] and not keys_pressed[pygame.K_s]:
            pressed = "RIGHT"
        # LEFT
        elif keys_pressed[pygame.K_a] and not keys_pressed[pygame.K_w] and not keys_pressed[pygame.K_s]:
            pressed = "LEFT"

        self.direction = pressed

    def playerDash(self):
        # Dash Action
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            if Player.dashCooldown(self):
                Player.playerDirection(self)
                self.dashFrameCounter = 0

    def dashAnimation(self):
        # Dash Movement and Animation
        distance = self.dashDistance / self.dashFrame
        diagnol = (math.sqrt(2) / 2) * distance
        # Dash Cooldown/If Available
        if self.dashFrameCounter < self.dashFrame:
            self.dashFrameCounter += 1
            # Direction of Dash
            if self.direction == "UP":
                if self.y - diagnol > borderY_top:
                    self.y -= distance
                    self.dashTimer = 0
                elif self.y > borderY_top:
                    self.y -= self.y - borderY_top
                    self.dashTimer = 0

            if self.direction == "UPR":
                if self.y - diagnol > borderY_top:
                    self.y -= diagnol
                    self.dashTimer = 0
                elif self.y > borderY_top:
                    self.y -= self.y - borderY_top
                    self.dashTimer = 0

                if self.x + diagnol < borderX_right:
                    self.x += diagnol
                    self.dashTimer = 0
                elif self.x < borderX_right:
                    self.x += self.x - borderX_right
                    self.dashTimer = 0

            if self.direction == "UPL":
                if self.y - diagnol > borderY_top:
                    self.y -= diagnol
                    self.dashTimer = 0
                elif self.y > borderY_top:
                    self.y -= self.y - borderY_top
                    self.dashTimer = 0

                if self.x - diagnol > borderX_left:
                    self.x -= diagnol
                    self.dashTimer = 0
                elif self.x > borderX_left:
                    self.x -= self.x - borderX_left
                    self.dashTimer = 0

            if self.direction == "DOWN":
                if self.y + distance < borderY_bottom:
                    self.y += distance
                    self.dashTimer = 0
                elif self.y < borderY_bottom:
                    self.y += borderY_bottom - self.y
                    self.dashTimer = 0

            if self.direction == "DOWNR":
                if self.y + diagnol < borderY_bottom:
                    self.y += diagnol
                    self.dashTimer = 0
                elif self.y < borderY_bottom:
                    self.y += borderY_bottom - self.y
                    self.dashTimer = 0

                if self.x + diagnol < borderX_right:
                    self.x += diagnol
                    self.dashTimer = 0
                elif self.x < borderX_right:
                    self.x += self.x - borderX_right
                    self.dashTimer = 0

            if self.direction == "DOWNL":
                if self.y + diagnol < borderY_bottom:
                    self.y += diagnol
                    self.dashTimer = 0
                elif self.y < borderY_bottom:
                    self.y += borderY_bottom - self.y
                    self.dashTimer = 0

                if self.x - diagnol > borderX_left:
                    self.x -= diagnol
                    self.dashTimer = 0
                elif self.x > borderX_left:
                    self.x -= self.x - borderX_left
                    self.dashTimer = 0

            if self.direction == "LEFT":
                if self.x - distance > borderX_left:
                    self.x -= distance
                    self.dashTimer = 0
                elif self.x > borderX_left:
                    self.x -= self.x - borderX_left
                    self.dashTimer = 0

            if self.direction == "RIGHT":
                if self.x + distance < borderX_right:
                    self.x += distance
                    self.dashTimer = 0
                elif self.x < borderX_right:
                    self.x += self.x - borderX_right
                    self.dashTimer = 0

    def dashCooldown(self):
        # Manages Cooldown of Dash
        dash = False
        if self.dashTimer <= self.dashCooldown:
            self.dashTimer += 1
            dash = False
        if self.dashTimer >= self.dashCooldown:
            dash = True
        return dash

    def playerShoot(self):
        # Enables Player Shoot
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_LEFT]:
            Player.create_bullet(self)

    def create_bullet(self):
        # Creates Bullet Object When Shoot Action
        if Player.playerReload(self):
            self.reload = 0
            direction = Player.bulletDirection(self)
            b = Bullet(self.x + self.displayX, self.y + self.displayY, direction, self.bullet_damage, self.bullet_speed)
            bullet_group.add(b)
            nonPlayer_group.add(b)
    def playerReload(self):
        # Shoot Cooldown
        shoot = False
        if self.reload <= self.shootCooldown:
            self.reload += 1
            shoot = False
        if self.reload >= self.shootCooldown:
            shoot = True
        return shoot

    def bulletDirection(self):
        # Determines Direction of Bullet
        keys_pressed = pygame.key.get_pressed()
        pressed = ""

        if keys_pressed[pygame.K_UP]:
            if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_LEFT]:
                pressed = "UPL"
            elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_RIGHT]:
                pressed = "UPR"
            elif keys_pressed[pygame.K_UP] and not keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_RIGHT]:
                pressed = "UP"

        elif keys_pressed[pygame.K_DOWN]:
            if keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_LEFT]:
                pressed = "DOWNL"
            elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_RIGHT]:
                pressed = "DOWNR"
            elif keys_pressed[pygame.K_DOWN] and not keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_RIGHT]:
                pressed = "DOWN"

        elif keys_pressed[pygame.K_RIGHT] and not keys_pressed[pygame.K_UP] and not keys_pressed[pygame.K_DOWN]:
            pressed = "RIGHT"

        elif keys_pressed[pygame.K_LEFT] and not keys_pressed[pygame.K_UP] and not keys_pressed[pygame.K_DOWN]:
            pressed = "LEFT"

        return pressed

    def playerHit(self, damage):
        if self.iframesTimer >= self.iframes:
            self.iframesTimer = 0
            self.health -= damage
        # Determines if Player Dies
        if self.health <= 0:
            self.death = True

    def createHealthbar(self):
        self.healthbarGreen = PlayerHealth(1)
        self.healthbarRed = PlayerHealth(2)
        playerHealthBar_group.add(self.healthbarGreen, self.healthbarRed)

    def playerHealthBar(self):
        # Updates Each Healthbar
        PlayerHealth.setHealthbar(self.healthbarGreen, self.health, self.totalHealth)
        PlayerHealth.setHealthbar(self.healthbarRed, self.health, self.totalHealth)

    def playerIframe(self):
        # I Frames Manager
        if self.iframesTimer < self.iframes:
            self.iframesTimer += 1
            self.image = PLAYERINVINCIBLE_IMAGE

        if self.iframes <= self.iframesTimer:
            self.image = PLAYER_IMAGE

    def playerMoney(self, n):
        self.playerMoney += n

    def playerInteractChest(self):
        # If Player Not Touching Teleporter
        if not pygame.sprite.spritecollideany(self, teleporter_group):
            if pygame.sprite.spritecollideany(self, chest_group):
                chest = pygame.sprite.spritecollideany(self, chest_group)
                # Chest that is touching player is taken
                if chest and Chest.getOpened(chest) == False and self.touchingObject == False:
                    # Tells That It is touching a chest so no two chest can be selected
                    self.touchingChest = True
                    self.selectedObject = chest
                    Chest.setSelected(chest, True)
                # If E is pressed to Open, checks parameters and if passes, opens chest
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_e]:
                    if Chest.getOpened(chest) == False and Player.getMoney(playerList[0]) >= Chest.getCost(chest):
                        Chest.setOpened(chest)
                        self.shootCooldown *= 0.9
                        self.playerMoney -= Chest.getCost(chest)
                        self.touchingObject = False

        if not pygame.sprite.spritecollideany(self, chest_group) and not pygame.sprite.spritecollideany(self, teleporter_group):
            self.touchingObject = False

        # Get Functions
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getDisplayX(self):
        return self.displayX
    def getDisplayY(self):
        return self.displayY
    def getMoney(self):
        return self.playerMoney
    def getDeath(self):
        return self.death
    def getThorn(self):
        return self.thornDamage
    def setTouchingTeleporter(self, touching):
        self.touchingObject = touching

        # Health Get
    def getHealth(self):
        return self.health
    def getTotalHealth(self):
        return self.totalHealth

        # Manage Other Sprites

    def update(self):
        Player.playerMove(self)
        Player.playerShoot(self)
        Player.playerReload(self)

        Player.playerDash(self)
        Player.dashCooldown(self)
        Player.dashAnimation(self)

        Player.playerIframe(self)

        Player.playerHealthBar(self)
        Player.playerInteractChest(self)

        playerX[0] = self.x
        playerY[0] = self.y

        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))
