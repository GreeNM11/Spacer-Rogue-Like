
from globalVar import *

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, size, x, y, totalHP):
        super().__init__()
        # Creating Image
        self.enemySize = size
        self.sizeX = self.enemySize
        self.sizeY = 3 + self.enemySize / 20
        self.image = pygame.Surface([self.sizeX, self.sizeY])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # Position of HealthBar Above Enemy
        self.originalX = x
        self.x = x
        self.y = y - (3 + self.enemySize * 0.6)
        self.totalHP = totalHP

    def setHealthBar(self, x, y, HP):
        # Updates Position
        self.x = x
        self.y = y - (3 + self.enemySize * 0.6)
        # Makes Sure HP Is Not Below 0
        if HP < 0:
            HP = 0
        # Updates the Size of Healthbar According to HP Percent Left
        self.percentHP = (HP / self.totalHP)
        self.sizeX = self.percentHP * self.enemySize
        self.x -= ((self.enemySize - self.sizeX) / 2)
        # Updates Image
        if self.sizeX and self.sizeY > 0:
            self.image = pygame.Surface([self.sizeX, self.sizeY])
            self.image.fill(GREEN)

    def displayPosition(self):
        self.displayX = self.x - playerX[0]
        self.displayY = self.y - playerY[0]

    def update(self):
        HealthBar.displayPosition(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))