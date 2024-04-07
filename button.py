import pygame
import config

class Button():
    def __init__(self, image, x_pos, y_pos, text_input, font):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(topleft=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.font = pygame.font.SysFont(font['name'],font['size'])
        self.text = self.font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos+self.rect.width/2, self.y_pos+self.rect.height/2))

    def update(self, win):
        win.blit(self.image, self.rect)
        win.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, "green")
        else:
            self.text = self.font.render(self.text_input, True, "white")