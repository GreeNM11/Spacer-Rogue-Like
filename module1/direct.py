
from enemy import Enemy
from player import Player
from teleporter import Teleporter
from boss import Boss
from chest import Chest
from globalVar import *
global player, difficulty, teleporter

class Directory():
    def __init__(self, difficulty):
        # Game Level Variables
        self.multiplier = 1 # Increasing Value of Stats as Game Progresses
        self.scale = 1 + (difficulty * 0.1) # Ratio Multiplier Increases By
        # Stage Director
        self.stage = 0
        self.directorCredits = 0 # Amount of Credits for Director to Spend to Make Decisions
        self.stageUpdater = 1 # Makes Decision Per Second(s)
        self.stageUpdaterCounter = self.stageUpdater
        self.enemyCount = 0
        self.enemyAppearance = [0, 2]
        # Stage & Teleporter
        self.endStage = True # Starts First Stage From Stage 0
        self.bossSpawned = False
        self.bossKilled = False
        self.bossAppearance = [0, 1]
        self.bossTimer = 3 # Seconds
        self.bossTimerCounter = 0
        self.spawnBoss = False
        # Time
        self.timeMillisecond = 0
        self.timeSecond = 0
        self.timeMinute = 0
        # Enemy Stats
        self.enemyLevel = 1
        self.enemyLevelUp = 100
        self.enemyLevelUpCounter = 0
        self.enemyCost = 0
        # Enemy Spawn
        self.enemySpawnX = 0
        self.enemySpawnY = 0
        # Enemy Types and Cost
        self.enemyCostList = [[0,0], [1,4], [2,7]]
        self.bossCostList = [[0,0], [1,20], [2,20]]

    def stageDirector(self):
        # Director Gains Points
        if self.bossKilled == False:
            self.directorCredits += 1 + self.scale
            # Counts Seconds
            self.stageUpdaterCounter += 1
            # Increases Level EXP Every Update by Time
            if self.stageUpdater <= self.stageUpdaterCounter:
                self.stageUpdaterCounter = 0
                self.enemyLevelUpCounter += self.scale
                # Enemy Level Up if Max EXP
                if self.enemyLevelUpCounter >= self.enemyLevelUp:
                    # Enemy Level Up Stats
                    self.enemyLevel += 1
                    self.multiplier += 0.2
                    self.enemyLevelUpCounter = 0
                # Decides What Enemies to Spawn at Random Using Credits
                if self.directorCredits > 0:
                    select_enemy = random.randint(self.enemyAppearance[0], self.enemyAppearance[1])
                    enemyType = self.enemyCostList[select_enemy][0]
                    enemyCost = self.enemyCostList[select_enemy][1]
                    if enemyType > 0:
                        enemyAmount = random.randint(0, self.directorCredits // enemyCost)
                        if enemyAmount > 0:
                            Directory.spawn_enemy(self, enemyType, enemyAmount)
                            self.directorCredits -= enemyCost * enemyAmount

    def nextStage(self):
        # When Stage Ends Via Teleporter, Next Stage Happens
        self.stage += 1
        self.enemyLevelUpCounter += 1
        self.directorCredits = 0
        self.spawnBoss = False
        self.bossKilled = False
        self.bossSpawned = False
        # Resets Teleporterd
        Teleporter.setTeleporterLocation(teleporter)
        Directory.spawn_chest(self)
        self.endStage = False

    def manageTele(self):
        if Teleporter.getPressed(teleporter) == True:
            # If Boss Has Not Spawned Nor Dead, Spawns Boss
            if self.bossKilled == False and self.bossSpawned == False:
                self.spawnBoss = True
                Teleporter.setPressedFalse(teleporter)
                Teleporter.setTeleporterActive(teleporter, True)
            # If Boss Is Dead and Boss Has Spawned, End Stage and Next Stage Begins
            elif self.bossKilled == True and self.bossSpawned == True:
                self.endStage = True
        # Checks If Conditions For Ending Stage is True, also Starts First Stage
        if self.endStage == True:
            self.endStage = False
            Directory.nextStage(self)
        # Checks If Boss Spawn Was Initialized
        if self.spawnBoss == True:
            if self.bossTimer <= self.bossTimerCounter:
                # Chooses Boss to Spawn
                r = 1  # random.randint(0, 1)
                # Creates Boss Object
                self.boss = Boss(Teleporter.getX(teleporter), Teleporter.getY(teleporter), self.multiplier, self.bossAppearance[r])
                boss_group.add(self.boss)
                nonPlayer_group.add(self.boss)
                self.bossSpawned = True
                # Resets Teleporter and Timer
                self.spawnBoss = False
                self.telePress = False
                self.bossTimerCounter = 0
        # Checks If Boss Died
        if self.bossSpawned == True:
            if Boss.getBossDead(self.boss):
                self.bossKilled = True
                self.boss.kill()
        # Stops Teleporter Event
        if self.bossKilled == True:
            Teleporter.setTeleporterActive(teleporter, False)

    def spawnLocation(self):
        # Randomly Selects Coordinate Along Border
        r = random.randint(1, 4)

        spawnX = borderX_left + shiftX
        spawnY = borderY_bottom + shiftY
        randomX = random.randint(borderX_left, borderX_right) + shiftX
        randomY = random.randint(borderY_top, borderY_bottom) + shiftY

        if r == 1:
            self.enemySpawnX = spawnX
            self.enemySpawnY = randomY
        if r == 2:
            self.enemySpawnX = spawnX
            self.enemySpawnY = randomY
        if r == 3:
            self.enemySpawnX = randomX
            self.enemySpawnY = spawnY
        if r == 4:
            self.enemySpawnX = randomX
            self.enemySpawnY = spawnY
        print (self.enemySpawnY)

    def spawn_enemy(self, t, n):
        # Spawns Enemy
        for i in range (n):
            Directory.spawnLocation(self) # Sets Spawn Location
            e = Enemy(self.enemySpawnX, self.enemySpawnY, self.multiplier, t)
            enemy_group.add(e)
            nonPlayer_group.add(e)
            self.enemyCount += 1

    def spawn_chest(self):
        # Sets Amount of Chest to Spawn
        chestNum = random.randint(2, 2 + self.stage)
        # Randomizes Each Chest and Spawns It
        chestShift = 50
        for i in range(chestNum):
            type = random.randint(1, 1)
            chestX = random.randint(borderX_left, borderX_right) + shiftX
            chestY = random.randint(borderY_top + chestShift, borderY_bottom - chestShift) + shiftY
            chest = Chest(chestX, chestY, type, self.stage)
            chest_group.add(chest)
            nonPlayer_group.add(chest)

    def gameTimer(self):
        # Keeps Track of Time
        self.timeMillisecond += 1
        # Every 60 Milliseconds Adds 1 Minute
        if self.timeMillisecond >= 60:
            Directory.stageDirector(self)
            if self.spawnBoss == True:
                self.bossTimerCounter += 1
            # Per Second
            self.timeSecond += 1
            self.timeMillisecond = 0
        # Every 60 Seconds Adds 1 Minute
        if self.timeSecond >= 60:
            self.timeSecond = 0
            self.timeMinute += 1

    def playerDeath(self):
        if Player.getDeath(player) == True:
            self.playerRun = False

    def enemyCount(self):
        self.enemyCount -= 1

    # Get Functions
    def getMultiplier(self):
        return self.multiplier
    def getTimeSeconds(self):
        return self.timeSecond
    def getTimeMinutes(self):
        return self.timeMinute
    def bossDeath(self):
        self.bossKilled = True
    def touchingChest(self):
        return self.touchingChest
    def setTouchingChest(self, open):
        self.touchingChest = open

    def update(self):
        Directory.gameTimer(self) # Directory in Game Timer
        Directory.playerDeath(self)
        Directory.manageTele(self)

    # Makes the Player
player = Player()
player_group.add(player)
playerList.append(player)

teleporter = Teleporter()
teleporter_group.add(teleporter)
nonPlayer_group.add(teleporter)

game = Directory(difficulty)
print('made')

