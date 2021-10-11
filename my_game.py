# importing the modules that will be needed in the project
import pygame
import random

# initialising the pygame modules
pygame.init()

# creating and setting the size of the screen that is going to be used
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))

# Creating the player, the enemies and the prize objects with the chosen images
player = pygame.image.load("game/player.jpg")
enemy1 = pygame.image.load("game/enemy.png")
enemy2 = pygame.image.load("game/enemy.png")
enemy3 = pygame.image.load("game/enemy.png")
prize = pygame.image.load("game/prize.jpg")

# Getting the player, enemies and prize objects' widths and heights
# To be used to detect whenever any of them are off screen or where they are on the screen
player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

# Printing the height and width of the player object (i.e. the position)
print(f"This is the height of the player: {player_height}.")
print(f"This is the width of the player: {player_width}.")

# Storing the player's position in variables in order for them to be changeable
playerX = 100
playerY = 50

# Setting the enemy and prize objects start position off screen and with a random Y-position
enemy1X = screen_width
enemy1Y = random.randint(0, (screen_height - enemy1_height))

enemy2X = screen_width
enemy2Y = random.randint(0, (screen_height - enemy2_height))

enemy3X = screen_width
enemy3Y = random.randint(0, (screen_height - enemy3_height))

prizeX = screen_width
prizeY = random.randint(0, (screen_height - prize_height))

# Detecting whether arrow keys are being pressed or not
keyUp = False
keyDown = False

# Creating the while loop to continually have the game running
while 1:
    # Clearing the screen and drawing the player and enemy on the screen in the specified positions
    screen.fill(0)
    screen.blit(player, (playerX, playerY))
    screen.blit(enemy1, (enemy1X, enemy1Y))
    screen.blit(enemy2, (enemy2X, enemy2Y))
    screen.blit(enemy3, (enemy3X, enemy3Y))
    screen.blit(prize, (prizeX, prizeY))

    # Updates the screen to what is currently supposed to be on screen
    pygame.display.flip()

    # Looping through events that happen during the game
    for event in pygame.event.get():

        # Checking if the user want to quit and then quits the program if it is true
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Checking if a key has been pressed
        if event.type == pygame.KEYDOWN:

            # Testing if a key we want has been pressed
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

        # Checking if a key is not being pressed
        if event.type == pygame.KEYUP:

            # Testing if a key we want is no longer being pressed
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False

    # After the checks are completed in the for loop,
    # Checking if the keyUp or keyDown variables are true and will then move the layer object accordingly
    if keyUp:
        # Checks if the next movement will move the player off screen
        # If it doesn't the player object will move
        if playerY > 0:
            playerY -= 1

    if keyDown:
        # Checks if the next movement will move the player off screen
        # If it doesn't the player object will move
        if playerY < screen_height - player_height:
            playerY += 1

    # Adding a bounding box to the player to be used to check if the enemies collide with the player
    playerBox = pygame.Rect(player.get_rect())

    # Updating the bounding box to the player to ensure it is always around the player
    playerBox.top = playerY
    playerBox.left = playerX

    # Setting the bounding boxes for the first enemy object
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1Y
    enemy1Box.left = enemy1X

    # Setting the bounding boxes for the second enemy object
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2Y
    enemy2Box.left = enemy2X

    # Setting the bounding boxes for the third enemy object
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3Y
    enemy3Box.left = enemy3X

    # Setting the bounding boxes for the prize object
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeY
    prizeBox.left = prizeX

    # Testing for collisions between the player's box and the enemies' boxes
    if playerBox.colliderect(enemy1Box):

        # Printing losing status if a collision is detected
        print("You Lose!")

        # Quit the game and closing the window
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):

        # Printing losing status if a collision is detected
        print("You Lose!")

        # Quit the game and closing the window
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):

        # Printing losing status if a collision is detected
        print("You Lose!")

        # Quit the game and closing the window
        pygame.quit()
        exit(0)

    # Testing for a player collision
    if playerBox.colliderect(prizeBox):

        # Printing winning status if a collision is detected
        print("You Win!")

        # Quit the game and closing the window
        pygame.quit()
        exit(0)

    # Making the first enemy object move towards the player
    enemy1X -= 0.15

    # Once the first enemy object starts going off screen,
    # the second enemy object starts moving toward the player
    if enemy1X < 0:
        enemy2X -= 0.15

    # Once the second enemy object starts going off screen,
    # the third enemy object starts moving toward the player
    if enemy2X < 0:
        enemy3X -= 0.15

    # Once the third enemy object starts going off screen,
    # the prize object starts moving toward the player
    if enemy3X < 0:
        prizeX -= 0.15

    # If the prize object goes off screen the game is over and the player loses
    if prizeX < 0:
        # Printing losing status
        print("You lose!")

        # Quiting the game and closing the window
        pygame.quit()
        exit(0)
