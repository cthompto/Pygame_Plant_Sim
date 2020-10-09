# import the pygame and time
import pygame
import time
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("sapling.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Lemon Tree Saga")

    # create a surface on screen that has the size of 320 x 480
    screen = pygame.display.set_mode((320,480))

    # load fonts
    dialogue_font = pygame.font.Font('PressStart2P.ttf', 10)
    button_font = pygame.font.Font('Fipps-Regular.ttf', 14)
    title_font = pygame.font.Font('Fipps-Regular.ttf', 18)

    # create title and button texts
    title_text = title_font.render("Lemon Tree Saga", True, (37, 161, 62))
    title_enter = button_font.render("Press Z to Continue", True,(37, 161, 62))
    title_enter2 = button_font.render("Press Z to Continue", True,(29, 63, 99))
    to_be_text = title_font.render("To Be Continued...", True, (37, 161, 62))
    to_be_restart = button_font.render("Press Z to Restart", True, (37, 161, 62))
    to_be_restart2 = button_font.render("Press Z to Restart", True, (29, 63, 99))
    to_be_credits = button_font.render("Press X for Credits", True, (37, 161, 62))
    wait1_text = button_font.render("Wait 1 Day", True, (37, 161, 62))
    wait1_text2 = button_font.render("Wait 1 Day", True, (29, 63, 99))
    z_text = button_font.render("( Z )", True, (37, 161, 62))
    z_text2 = button_font.render("( Z )", True, (29, 63, 99))
    wait7_text = button_font.render("Wait 7 Days", True, (37, 161, 62))
    wait7_text2 = button_font.render("Wait 7 Days", True, (29, 63, 99))
    x_text = button_font.render("( X )", True, (37, 161, 62))
    x_text2 = button_font.render("( X )", True, (29, 63, 99))
    water_text = button_font.render("Water Tree", True, (37, 161, 62))
    water_text2 = button_font.render("Water Tree", True, (29, 63, 99))
    c_text = button_font.render("( C )", True, (37, 161, 62))
    c_text2 = button_font.render("( C )", True, (29, 63, 99))
    win1 = title_font.render("Zoey Survived", True, (37, 161, 62))
    lose1 = title_font.render("Zoey Has Died", True, (37, 161, 62))

    # create intro screen splash text
    splash1 = dialogue_font.render("FOR ZOEY", True, (37, 161, 62))
    splash2 = dialogue_font.render("OUR LEMON TREE", True, (37, 161, 62))
    
    # create intro text block 1
    story1 = dialogue_font.render("IN AUGUST, MY WIFE AND I", True, (37, 161, 62))
    story2 = dialogue_font.render("MOVED INTO A NEW HOME IN", True, (37, 161, 62))
    story3 = dialogue_font.render("SAN JOSE. KNOWING WE WOULD", True, (37, 161, 62))
    story4 = dialogue_font.render("BE HERE FOR SOMETIME, WE", True, (37, 161, 62))
    story5 = dialogue_font.render("WANTED TO FEEL SETTLED. SO,", True, (37, 161, 62))
    story6 = dialogue_font.render("WE BOUGHT A LEMON TREE FOR", True, (37, 161, 62))
    story7 = dialogue_font.render("OUR BALCONY. HER NAME IS ZOEY.", True, (37, 161, 62))
    
    # create intro text block 2
    story8 = dialogue_font.render("WE QUICKLY REALIZED HOW", True, (37, 161, 62))
    story9 = dialogue_font.render("CHALLENGING IT IS TO CARE", True, (37, 161, 62))
    story10 = dialogue_font.render("FOR SOMETHING THAT CAN'T", True, (37, 161, 62))
    story11 = dialogue_font.render("VERBALIZE ITS NEEDS. CARING", True, (37, 161, 62))
    story12 = dialogue_font.render("BECAME A OF PROCESS OF", True, (37, 161, 62))
    story13 = dialogue_font.render("WATERING OR WAITING.", True, (37, 161, 62))
    
    # create intro text block 3
    story14 = dialogue_font.render("THIS GAME IS A REFLECTION", True, (37, 161, 62))
    story15 = dialogue_font.render("OF THE PROCESS. THE ONLY", True, (37, 161, 62))
    story16 = dialogue_font.render("OPTIONS ARE TO EITHER WATER", True, (37, 161, 62))
    story17 = dialogue_font.render("OR WAIT...", True, (37, 161, 62))

    # define variables for the game
    water = 0
    days = 0
    health = 0

    # define variable for game the screens
    Game_Stage = 0

    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # keybroad controls
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_z:
                        # title screen
                        if Game_Stage == 0:
                            Game_Stage = 1
                            screen.blit(title_enter2, (45,425))
                            pygame.display.flip()
                            time.sleep(.5)
                            # intro splash
                            screen.fill((227, 207, 54))
                            screen.blit(splash1, (125, 160))
                            screen.blit(splash2, (95, 180))
                            pygame.display.flip()
                            time.sleep(4)
                        # story screen
                        elif Game_Stage == 1:
                            Game_Stage = 2
                            days = 0
                            water = 0
                            health = 0
                            screen.blit(title_enter2, (45,425))
                            pygame.display.flip()
                            time.sleep(.5)
                        # main game screen
                        elif Game_Stage == 2:
                            days += 1
                            water -= 1
                            if water < 0:
                                health -= 1
                            if water > 7:
                                health += 1
                            print("days = ", days)
                            print("water = ", water)
                            print("health = ", health)
                            print("Game_Stage = ", Game_Stage)
                            screen.blit(wait1_text2, (25,360))
                            screen.blit(z_text2, (55,380))
                            pygame.display.flip()
                            time.sleep(.5)
                            
                        # win screen
                        elif Game_Stage == 3:
                            Game_Stage = 5
                            screen.blit(title_enter2, (45,425))
                            pygame.display.flip()
                            time.sleep(.5)

                        # lose screen
                        elif Game_Stage == 4:
                            Game_Stage = 5
                            screen.blit(title_enter2, (45,425))
                            pygame.display.flip()
                            time.sleep(.5)

                        # to be continued screen
                        elif Game_Stage == 5:
                            Game_Stage = 0
                            screen.blit(to_be_restart2, (45,280))
                            pygame.display.flip()
                            time.sleep(.5)
                        
                        # credits screen
                        #elif Game_Stage ==6:

                    if event.key == pygame.K_x:
                        if Game_Stage == 2:
                            days += 7
                            if water < 0:
                                health -= 7
                            elif water == 1:
                                health -= 6
                            elif water == 2:
                                health -= 5
                            elif water == 3:
                                health -= 4
                            elif water == 4:
                                health -= 3
                            elif water == 5:
                                health -= 2
                            elif water == 6:
                                health -= 1
                            elif water == 8:
                                health += 1
                            elif water == 9:
                                health += 2
                            elif water == 10:
                                health += 3
                            elif water == 11:
                                health += 4
                            elif water == 12:
                                health += 5
                            elif water == 13:
                                health += 6
                            elif water > 14: 
                                health += 7
                            water -= 7
                            print("days = ", days)
                            print("water = ", water)
                            print("health = ", health)
                            print("Game_Stage = ", Game_Stage)
                            screen.blit(wait7_text2, (180,360))
                            screen.blit(x_text2, (220,380))
                            pygame.display.flip()
                            time.sleep(.5)
               
                    if event.key == pygame.K_c:
                        if Game_Stage == 2:
                            water += 7
                            print("water = ", water)
                            screen.blit(water_text2, (100, 415))
                            screen.blit(c_text2, (140, 435))
                            pygame.display.flip()
                            time.sleep(.5)

            # title screen
            if Game_Stage == 0:
                screen.fill((227, 207, 54))
                title_imagine = pygame.image.load("sapling.png")
                title_imagine = pygame.transform.scale(title_imagine, (90, 185))
                screen.blit(title_imagine, (105,148))
                screen.blit(title_text, (35,40))
                screen.blit(title_enter, (45,425))
                
            # intro screen
            if Game_Stage == 1:
                # intro main
                screen.fill((227, 207, 54))
                # text block 1
                screen.blit(story1, (25, 40))
                screen.blit(story2, (25, 60))
                screen.blit(story3, (25, 80))
                screen.blit(story4, (25, 100))
                screen.blit(story5, (25, 120))
                screen.blit(story6, (25, 140))
                screen.blit(story7, (25, 160))
                # text block 2
                screen.blit(story8, (25, 200))
                screen.blit(story9, (25, 220))
                screen.blit(story10, (25, 240))
                screen.blit(story11, (25, 260))
                screen.blit(story12, (25, 280))
                screen.blit(story13, (25, 300))
                # text block 3
                screen.blit(story14, (25, 340))
                screen.blit(story15, (25, 360))
                screen.blit(story16, (25, 380))
                screen.blit(story17, (25, 400))
                # advance button
                screen.blit(title_enter, (45, 425))

            # main game screen
            if Game_Stage == 2:
                screen.fill((227, 207, 54))
                title_imagine = pygame.image.load("sapling.png")
                title_imagine = pygame.transform.scale(title_imagine, (90, 185))
                screen.blit(title_imagine, (105,148))
                screen.blit(wait1_text, (25,360))
                screen.blit(z_text, (55,380))
                screen.blit(wait7_text, (180,360))
                screen.blit(x_text, (220,380))
                screen.blit(water_text, (100, 415))
                screen.blit(c_text, (140, 435))
                # win condition
                if (days > 60): 
                    Game_Stage = 3
                #lose condition
                if (health < -14 or health > 21):
                    Game_Stage = 4

            # win screen
            if Game_Stage == 3:
                screen.fill((227, 207, 54))
                screen.blit(win1, (35,40))
                print("Game_Stage = ", Game_Stage)
                screen.blit(title_enter, (45, 425))

            # lose screen
            if Game_Stage == 4:
                screen.fill((227, 207, 54))
                screen.blit(lose1, (35,40))
                print("Game_Stage = ", Game_Stage)
                screen.blit(title_enter, (45, 425))

            # to be continued screen
            if Game_Stage == 5:
                screen.fill((227, 207, 54))
                screen.blit(to_be_text, (45, 220))
                screen.blit(to_be_restart, (45,280))
                screen.blit(to_be_credits, (45,320))

            # credits screen
            if Game_Stage == 6:
                screen.fill((227, 207, 54))

            pygame.display.flip()
 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()