
from globalVar import *
from player import *

ENEMY_BULLET_IMAGE1 = pygame.image.load(os.path.join(sprites_folder, 'enemy_bullet1.png'))

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, X, Y, type):
        super().__init__()
        # Bullet Sprite
        self.image = ENEMY_BULLET_IMAGE1
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # Bullet Variables
        self.type = type
        self.moveX = X
        self.moveY = Y
        self.BULLET_SPEED = 0
        self.damage = 0

        EnemyBullet.setType(self)

    def setType(self):
        # Determines Inputted Boss Type
        if self.type == 1:
            EnemyBullet.bossBullet1(self)

    def bossBullet1(self):
        # Defines Boss 1
        self.BULLET_SPEED = 1
        self.damage = 15

    def manageBullet(self):
        self.x += self.moveX * self.BULLET_SPEED
        self.y += self.moveY * self.BULLET_SPEED

    def destroy(self):
        # Bullet Dies if Out of Boundry
        if borderX_left + shiftX > self.x:
            self.kill()
        elif self.x > borderX_right + shiftX:
            self.kill()
        elif borderY_top + shiftY > self.y:
            self.kill()
        elif self.y > borderY_bottom + shiftY:
            self.kill()
        # Dies When Hits Player
        if pygame.sprite.spritecollideany(self, player_group):
            Player.playerHit(playerList[0], self.damage)
            self.kill()

    def getDamage(self):
        return self.damage

    def displayPosition(self):
        self.displayX = self.x - playerX[0]
        self.displayY = self.y - playerY[0]

    def update(self):
        EnemyBullet.displayPosition(self)
        EnemyBullet.manageBullet(self)
        EnemyBullet.destroy(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))
