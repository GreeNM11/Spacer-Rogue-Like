
from direct import *
from globalVar import *

class Timer(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.image = ZERO_IMAGE
        self.rect = self.image.get_rect()
        # Number Variables
        self.num = num
        self.display = 0
        self.x = 0
        self.y = 0

    def displayTimer(self):
        # Gets Each Digit of Time
        self.y = 30
        if self.num == 1: # Ones Place of Second
            sec = Directory.getTimeSeconds(game)
            oneSec = sec % 10
            self.x = 115
            self.display = oneSec

        if self.num == 2: # Tens Place of Second
            sec = Directory.getTimeSeconds(game)
            tenSec = sec // 10
            self.x = 90
            self.display = tenSec

        if self.num == 3: # Ones Place of Minute
            min =  Directory.getTimeMinutes(game)
            oneMin = min % 10
            self.x = 50
            self.display = oneMin

        if self.num == 4: # Tens Place of Minute
            min = Directory.getTimeMinutes(game)
            tenMin = min // 10
            self.x = 25
            self.display = tenMin
        # Sets Sprite Image to Corresponding Number
        Timer.changeNumber(self, self.display) # Updates Image

        if self.num == 5: # Colon
            self.image = COLON_IMAGE
            self.x = 70

    def changeNumber(self, n):
        # Sets Image Based on Number
        if n == 0:
            self.image = ZERO_IMAGE
        if n == 1:
            self.image = ONE_IMAGE
        if n == 2:
            self.image = TWO_IMAGE
        if n == 3:
            self.image = THREE_IMAGE
        if n == 4:
            self.image = FOUR_IMAGE
        if n == 5:
            self.image = FIVE_IMAGE
        if n == 6:
            self.image = SIX_IMAGE
        if n == 7:
            self.image = SEVEN_IMAGE
        if n == 8:
            self.image = EIGHT_IMAGE
        if n == 9:
            self.image = NINE_IMAGE

    def update(self):
        Timer.displayTimer(self)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # Makes Timer
onesSecond = Timer(1)
tensSecond = Timer(2)
onesMinute = Timer(3)
tensMinute = Timer(4)
colon = Timer(5)
timer_group.add(onesSecond, tensSecond, onesMinute, tensMinute, colon)
