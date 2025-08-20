from enemy import Enemy
from enemyBullet import *
from globalVar import *

BOSS_IMAGE1 = pygame.image.load(os.path.join(sprites_folder, 'Boss1.png')) # BOSS1 Model

class Boss(Enemy):
    def __init__(self, x, y, multiplier, type):
        super().__init__(x, y, multiplier, type)
        # If Boss can Shoot
        self.shoot = False
        self.bullet_speed = 0
        self.bullet_type = ""

        self.bossDead = False

        Boss.setBossType(self)
        Enemy.enemyHealthbar(self)

    def setBossType(self):
        if self.type == 1:
            Boss.boss1(self)

    def boss1(self):
        # Defines Boss 1 Stats
        self.image = BOSS_IMAGE1
        self.size = 50
        self.moveSpeed = 0.2
        self.health = 40 + (0.5 * self.multiplier)
        self.totalHealth = self.health
        self.money = 20 * self.multiplier
        self.damage = 50
        # Shooting
        self.shoot = True
        self.bullet_speed = 4
        self.bullet_type = 1
        self.bulletReload = 2 * (60) # Seconds
        self.bulletReloadCooldown = self.bulletReload

    def bossShoot(self):
        # Boss Shoots Bullets On a Cooldown
        if self.shoot == True:
            self.bulletReloadCooldown += 1
            if self.bulletReload <= self.bulletReloadCooldown:
                Boss.shootBullet(self)
                self.bulletReloadCooldown = 0

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
            self.bossDead = True
            self.healthbar.kill()

    def getBossDead(self):
        return self.bossDead

    def update(self):
        Enemy.displayPosition(self)
        Enemy.handleEnemy(self)
        Enemy.enemyCollide(self)
        Boss.enemyHit(self)
        Enemy.setHealthBar(self)
        Enemy.hitPlayer(self)
        Boss.bossShoot(self)
        Enemy.displayPosition(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))
