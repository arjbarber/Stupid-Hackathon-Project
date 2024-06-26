import pygame
import config
import os
import sys
from button import Button
from random import randint
from time import time
from webbrowser import open
from requests import get
pygame.init()

WIN = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
HALF_WIDTH = config.WIDTH/2
BUTTON_ANSWER_FONT = pygame.font.SysFont(config.BUTTON_SCREEN_FONT["name"],config.BUTTON_SCREEN_FONT["size"])
BUTTON_PERIOD_FONT = pygame.font.SysFont(config.BUTTON_PERIOD_FONT["name"],config.BUTTON_PERIOD_FONT["size"])
L_BUTTON_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ButtonBackground.png')), (HALF_WIDTH - (2*config.BUTTON_MARGIN), config.HEIGHT - (2*config.BUTTON_MARGIN))
)
R_BUTTON_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ButtonBackground.png')), ((config.WIDTH - config.BUTTON_MARGIN) - (HALF_WIDTH + config.BUTTON_MARGIN), config.HEIGHT - (2*config.BUTTON_MARGIN))
)

def draw_button_screen(answer_text,periods):
    WIN.fill(config.COLOR)

    answer_text_font = BUTTON_ANSWER_FONT.render(answer_text,1,config.BUTTON_SCREEN_FONT["color"])
    periods_font = BUTTON_PERIOD_FONT.render(periods,1,config.BUTTON_PERIOD_FONT["color"])
    WIN.blit(answer_text_font,(HALF_WIDTH - (answer_text_font.get_width()/2),(config.HEIGHT/2) - answer_text_font.get_height()))
    WIN.blit(periods_font,(HALF_WIDTH - (periods_font.get_width()/2),(config.HEIGHT/2) + periods_font.get_height()))

    pygame.display.update()


def Button_Pressed(answer, correct):
    clock = pygame.time.Clock()
    run = True
    WIN.fill(config.COLOR)
    pygame.display.update()
    answer_text = ""
    second_line = ""
    init_time = time()
    while run:
        time_elapsed = int(time() - init_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if answer == correct:
            answer_text = "You clicked the right answer! Here is your reward."
            second_line = time_elapsed * "."
            if time_elapsed >= 5:
                open("https://youtu.be/dQw4w9WgXcQ?si=VG6kFpMeenJuBazA")
                main()
        else:
            answer_text = "You clicked the wrong answer! Here is your IP address:"
            second_line = str(get('https://api.ipify.org').content.decode('utf8')) + time_elapsed * "."
            if time_elapsed >= 5:
                main()        
        
        draw_button_screen(answer_text,second_line)

    pygame.quit()
    sys.exit()

def R_Button_Pressed():
    print("Right Pressed")

def draw_screen(Lbutton,Rbutton):
    WIN.fill(config.COLOR)
    Lbutton.update(WIN)
    Rbutton.update(WIN)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    pygame.display.set_caption("50/50")
    Lbutton = Button(L_BUTTON_IMAGE,config.BUTTON_MARGIN,config.BUTTON_MARGIN,config.LEFT_BUTTON_TEXT,config.BUTTON_FONT)
    Rbutton = Button(R_BUTTON_IMAGE,config.WIDTH/2 + config.BUTTON_MARGIN, config.BUTTON_MARGIN,config.RIGHT_BUTTON_TEXT,config.BUTTON_FONT)
    correct_ans = randint(0,1) # Left = 0, Right = 1
    # print(correct_ans) Will Tell you the correct side in the console
    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        mouse = {"position": pygame.mouse.get_pos(), "buttons": pygame.mouse.get_pressed()}
        
        if Lbutton.checkForInput(mouse["position"]) and mouse["buttons"][0]:
            Button_Pressed(0,correct_ans)
        elif Rbutton.checkForInput(mouse["position"]) and mouse["buttons"][0]:
            Button_Pressed(1,correct_ans)
        
        Lbutton.changeColor(mouse["position"])
        Rbutton.changeColor(mouse["position"])
        draw_screen(Lbutton,Rbutton)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()