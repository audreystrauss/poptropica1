import pygame
from sys import exit
import os

pygame.init()

screen_width = 1401
screen_height = 522
screen = pygame.display.set_mode((screen_width, screen_height))

# set up bg
image_path = os.path.join("poptropica1", "PoptropicaTowerz.png")
background_image = pygame.image.load(image_path).convert_alpha()

# set up jack
player_image_path = os.path.join("poptropica1", "Jack.webp")
player_image = pygame.image.load(player_image_path).convert_alpha()
player_image = pygame.transform.scale(player_image, (50, 50))
# set up obstacle 1
voteguy_image_path = os.path.join("poptropica1", "voteguy.jpg")
voteguy_image = pygame.image.load(voteguy_image_path).convert_alpha()
voteguy_image = pygame.transform.scale(voteguy_image, (50, 50))
#set up end point
professor_image_path = os.path.join("poptropica1", "prof.webp")
professor_image = pygame.image.load(professor_image_path).convert_alpha()
professor_image = pygame.transform.scale(professor_image, (50, 50))


player_x = 0
player_y = screen_height - player_image.get_height()  
player_speed = 5
voteguy_x = 400
voteguy_y = screen_height - voteguy_image.get_height()
voteguy_prompted = False
can_move_past_voteguy = False
professor_x = 1100
professor_y = screen_height - professor_image.get_height()
professor_prompted = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if can_move_past_voteguy or player_x > voteguy_x + voteguy_image.get_width():
                player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0, min(player_x, screen_width - player_image.get_width()))

    if player_x + player_image.get_width() >= voteguy_x and not voteguy_prompted:
        response = input("Would you like to sign up to vote today? (Type 'y' for Yes please! or 'n' for No way! I have a final exam!): ")
        if response.lower() == "y":
            confirm_response = input("Are you sure? (Type 'y' for Yes or 'n' for No): ")
            if confirm_response.lower() == "y":
                print("No problem! You cannot pass Voter Guy.")
                voteguy_prompted = True
            elif confirm_response.lower() == "n":
                print("Okay! You can still sign up to vote.")
                voteguy_prompted = False
        elif response.lower() == "n":
            print("No problem! You can pass me.")
            voteguy_prompted = True
            can_move_past_voteguy = True

    if player_x >= professor_x and not professor_prompted:
        print("Jack, why did you rush to class today? You don't need to take the final! You had the #1 final project!")
        professor_prompted = True
   

    
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(voteguy_image, (voteguy_x, voteguy_y))
    screen.blit(professor_image, (professor_x, professor_y))
    pygame.display.update()

