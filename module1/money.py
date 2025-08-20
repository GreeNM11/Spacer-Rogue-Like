
from timer import *

class Money(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.image = ZERO_IMAGE
        self.rect = self.image.get_rect()
        # Money Variables
        self.num = num
        self.display = 0
        self.x = 0
        self.y = 0

    def displayMoney(self):
        # Gets Each Digit of Money
        self.y = 30
        if self.num == 1: # Ones Place of Second
            money = Player.getMoney(player)
            ones = money % 10
            self.x = WIDTH - 25
            self.display = ones

        if self.num == 2: # Tens Place of Second
            money = Player.getMoney(player)
            tens = (money // 10) % 10
            self.x = WIDTH - 50
            self.display = tens

        if self.num == 3: # Ones Place of Minute
            money = Player.getMoney(player)
            hundreds = ((money // 100) % 10)
            self.x = WIDTH - 75
            self.display = hundreds

        if self.num == 4: # Tens Place of Minute
            money = Player.getMoney(player)
            thousands = ((money // 1000) % 10)
            self.x = WIDTH - 100
            self.display = thousands
        # Changes Money Image to Corresponding Number
        Timer.changeNumber(self, self.display) # Updates Image

    def update(self):
        Money.displayMoney(self)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # Makes Money Counter
ones = Money(1)
tens = Money(2)
hundreds = Money(3)
thousands = Money(4)
money_group.add(ones, tens, hundreds, thousands)