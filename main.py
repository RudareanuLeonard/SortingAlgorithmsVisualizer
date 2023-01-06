import pygame
import random

pygame.init() #init the pygame

class UIInfo: #class that has UI info...like window height width colors ...
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    GRADIENT = [
                GREY,
                (160, 160, 160),
                (192, 192, 192)
                ] #colors to use to differentiate the blocks that represents the numbers

    SIDE_PAD = 100 #number of pixels from the start/end of the window (num/2 to the left and num/2 to the right)

    def __init__(self, width, height, list_to_be_sorted):
        self.width = width
        self.height = height

        #now init the pygame window
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithms Visualisator") #title
        self.set_list(list_to_be_sorted)

    def set_list(self, list_to_be_sorted): #attributes of the list..the bars with their colors, width, height
        self.list_to_be_sorted = list_to_be_sorted
        self.max_value = max(self.list_to_be_sorted) #max value of the list
        self.min_value = min(self.list_to_be_sorted) #min value of the list
        #now we calculate the width of each bar...depending of how many bars we have
        self.bar_width = (self.width - self.SIDE_PAD) // len(list_to_be_sorted) #formula to determine how many pixels we give to each bar
        self.bar_height = 50
        self.start_x = self.SIDE_PAD // 2 #start drawing from left side Ox axis


def draw(draw_ui):
    draw_ui.window.fill(draw_ui.BACKGROUND_COLOR)
    pygame.display.update


def draw_list(draw_list):
    list_to_be_sorted = draw_list.list_to_be_sorted
    
    #start drawing from the top left corner(where pixel 0,0 is), so we figure out the height of the bar and then substract it from the height of the screen
    for i, val in enumerate(list_to_be_sorted):
        x = draw_list.start_x + i * draw_list.bar_width
        y = draw_list.height - (val - draw_list.min_value) * draw_list.bar_height 


def generate_list_to_be_sorted(n, min_value, max_value):
    list_to_be_sorted = []
    for i in range(n):
        value = random.randint(min_value, max_value)
        list_to_be_sorted.append(value)
    return list_to_be_sorted

def main(): #the main piece of code where all the things happen
    running_program = True
    n = 50
    min_value = 0
    max_value = 100

    list_to_be_sorted = generate_list_to_be_sorted(n, min_value, max_value)
    ui_info = UIInfo(800, 600, list_to_be_sorted)
    while running_program == True:
        pygame.display.update()
        draw(ui_info)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_program = False

    pygame.quit()


if __name__ == "__main__":
    main()