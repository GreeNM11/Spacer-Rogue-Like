
import sys
sys.path.insert(1, 'IS 2022 Fall Rogue-like game\module1')

from module1.boss import *
from module1.globalVar import *
from module1.player import Player
from module1.money import *
from module1.startScreen import *
from module1.mouse import *
from module1.enemyBullet import *
from module1.teleporter import *

keys_pressed = pygame.key.get_pressed()
created_characters = False

def draw_gameWindow():
    # Start Menu Update #
    if not StartScreenButtons.returnPressed(start_button):
        # Map Update
        screen.blit(MAP_START_IMAGE, (0, 0))
        # Buttons Update
        startButton_group.update()
        startButton_group.draw(screen)
        # Mouse Update
        mouse_group.update()
        mouse_group.draw(screen)
        
    # Run & System Updates
    if StartScreenButtons.returnPressed(start_button) == True:
            
        if Player.getDeath(player) == False:
            # Map Update
            x = -(playerX[0])
            y = -(playerY[0]) 
            screen.blit(space_background, (0,0))
            screen.blit(MAP_GAME_IMAGE, (x, y))
            
            # Game Objects
            teleporter_group.update()
            teleporter_group.draw(screen)
            chest_group.update()
            chest_group.draw(screen)
            
            # Player Update
            player_group.update()
            player_group.draw(screen)

            # Enemy Update
            enemy_group.update()
            enemy_group.draw(screen)
            boss_group.update()
            boss_group.draw(screen)

            # Bullet Update
            bullet_group.update()
            bullet_group.draw(screen)
            enemyBullet_group.update()
            enemyBullet_group.draw(screen)

            # Healthbar Update
            healthbar_group.update()
            healthbar_group.draw(screen)
            playerHealthBar_group.update()
            playerHealthBar_group.draw(screen)

            # Game Stats Update
            timer_group.update()
            timer_group.draw(screen)
            money_group.update()
            money_group.draw(screen)

            # Director/Level Update
            game.update()

    if Player.getDeath(player) == True:
        print("dead")

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    run = True
    screen.blit(MAP_START_IMAGE, (0, 0))
    
    startButton_group.add(start_button, quit_button)
    
    # Runs the Program
    while run:
        clock.tick(FPS) # Runs FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If Window Is Closed
                run = False
            if StartScreenButtons.returnPressed(quit_button): # If Quit Button is Pressed
                run = False

        draw_gameWindow()   # SCREEN UPDATE

    pygame.quit()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
camera = pygame.math.Vector2((0, 0))
pygame.display.set_caption("Game")

start_button = StartScreenButtons(1)
quit_button = StartScreenButtons(2)
startButton_group.add(start_button, quit_button)

mouse = Mouse()
mouse_group.add(mouse)

main()





