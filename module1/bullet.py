from globalVar import *

import player

BULLET_IMAGE1 = pygame.image.load(os.path.join(sprites_folder, 'Bullet.png'))

        # BULLET CLASS

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, damage, speed):
        super().__init__()
        # Bullet Sprite
        self.image = BULLET_IMAGE1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.displayX = self.x
        self.displayY = self.y
        self.direction = direction
        # Bullet Variables
        self.damage = damage
        self.BULLET_SPEED = speed

    def handleBullets(self):
        # Moves Bullet According to Direction
        diagnol = math.sqrt(2) / 2
        if self.direction == "UP":
            self.y -= self.BULLET_SPEED
        if self.direction == "UPR":
            self.y -= self.BULLET_SPEED * diagnol
            self.x += self.BULLET_SPEED * diagnol
        if self.direction == "UPL":
            self.y -= self.BULLET_SPEED * diagnol
            self.x -= self.BULLET_SPEED * diagnol

        if self.direction == "DOWN":
            self.y += self.BULLET_SPEED
        if self.direction == "DOWNR":
            self.y += self.BULLET_SPEED * diagnol
            self.x += self.BULLET_SPEED * diagnol
        if self.direction == "DOWNL":
            self.y += self.BULLET_SPEED * diagnol
            self.x -= self.BULLET_SPEED * diagnol

        if self.direction == "LEFT":
            self.x -= self.BULLET_SPEED
        if self.direction == "RIGHT":
            self.x += self.BULLET_SPEED

    def destroy(self):
        # Bullet Dies if Out of Boundry
        if borderX_left + shiftX> self.x:
            self.kill()
        elif self.x > borderX_right + shiftX:
            self.kill()
        elif borderY_top + shiftY > self.y:
            self.kill()
        elif self.y > borderY_bottom + shiftY:
            self.kill()

    def getDamage(self):
        return self.damage

    def displayPosition(self):
        self.displayX = self.x - playerX[0]
        self.displayY = self.y - playerY[0]

    def update(self):
        Bullet.displayPosition(self)
        Bullet.handleBullets(self)
        Bullet.destroy(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))
