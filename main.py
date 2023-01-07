import math
import pygame
import random
import time

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
    TOP_PAD = 150

    FONT = pygame.font.SysFont("times new roman", 12)

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
        self.bar_height = math.floor((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2 #start drawing from left side Ox axis


def draw(draw_ui):
    draw_ui.window.fill(draw_ui.BACKGROUND_COLOR)

    controls = draw_ui.FONT.render("R - create a new list | SPACE - start sorting | A - sort in ascending oreder | D - sort in descending order", 1, draw_ui.BLACK) # the text of the screen
    draw_ui.window.blit(controls, (10,5))

    draw_list(draw_ui)
    pygame.display.update()


def draw_list(draw_list, color_positions={}, clear_background=False):
    list_to_be_sorted = draw_list.list_to_be_sorted

    if clear_background:
        clear_rect = (draw_list.SIDE_PAD//2, draw_list.TOP_PAD, 
						draw_list.width - draw_list.SIDE_PAD, draw_list.height - draw_list.TOP_PAD)
        pygame.draw.rect(draw_list.window, draw_list.BACKGROUND_COLOR, clear_rect)

    color_num = 0
    #start drawing from the top left corner(where pixel 0,0 is), so we figure out the height of the bar and then substract it from the height of the screen
    for i, val in enumerate(list_to_be_sorted):
        x = draw_list.start_x + i * draw_list.bar_width
        y = draw_list.height - (val - draw_list.min_value) * draw_list.bar_height
        color = draw_list.GRADIENT[color_num % 3] #first, second or third color
        color_num = color_num + 1 
        
        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_list.window, color, (x, y, draw_list.bar_width, draw_list.height)) #draw the block
    
    if clear_background:
        pygame.display.update()



def generate_list_to_be_sorted(n, min_value, max_value):
    list_to_be_sorted = []
    for i in range(n):
        value = random.randint(min_value, max_value)
        list_to_be_sorted.append(value)
    return list_to_be_sorted


def some_sort(draw_info, ascending=True):
    list_to_be_sorted = draw_info.list_to_be_sorted

    for i in range(0, len(list_to_be_sorted) - 1):
        for j in range(i + 1, len(list_to_be_sorted)):
            if ascending == True:
                if list_to_be_sorted[i] > list_to_be_sorted[j]:
                    aux = list_to_be_sorted[i]
                    list_to_be_sorted[i] = list_to_be_sorted[j]
                    list_to_be_sorted[j] = aux
                    draw_list(draw_info, {j: draw_info.GREEN, j+1:draw_info.RED}, True)
                    yield True #stop the function at the point it is and can resume it later from the same point
                    
            else:
                if list_to_be_sorted[i] < list_to_be_sorted[j]:
                    aux = list_to_be_sorted[i]
                    list_to_be_sorted[i] = list_to_be_sorted[j]
                    list_to_be_sorted[j] = aux
                    draw_list(draw_info, {j: draw_info.GREEN, j+1:draw_info.RED}, True)
                    yield True #stop the function at the point it is and can resume it later from the same point


    return list_to_be_sorted




def heapify(arr, n, i, ascending):
    
    if ascending == True:
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
    
    # See if left child of root exists and is
    # greater than root
    
        if l < n and arr[i] < arr[l]:
            largest = l
    
    # See if right child of root exists and is
    # greater than root
    
        if r < n and arr[largest] < arr[r]:
            largest = r
    
    # Change root, if needed
    
        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
    
    # Heapify the root.
    
            heapify(arr, n, largest, ascending)
    else:#descending
        smallest = i # Initialize smallest as root
        l = 2 * i + 1 # left = 2*i + 1
        r = 2 * i + 2 # right = 2*i + 2
    
        # If left child is smaller than root
        if l < n and arr[l] < arr[smallest]:
            smallest = l
    
        # If right child is smaller than
        # smallest so far
        if r < n and arr[r] < arr[smallest]:
            smallest = r
    
        # If smallest is not root
        if smallest != i:
            (arr[i],
            arr[smallest]) = (arr[smallest],
                            arr[i])
    
            # Recursively heapify the affected
            # sub-tree
            heapify(arr, n, smallest, ascending)
 
# The main function to sort an array of given size
 
def heap_sort(draw_info, ascending=True):
    arr = draw_info.list_to_be_sorted
    n = len(arr)

 
 # Build a heap.
 # Since last parent will be at ((n//2)-1) we can start at that location.

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ascending)
        # draw_list(draw_info, {i: draw_info.GREEN, i-1:draw_info.RED}, True)
        # yield True #stop the function at the point it is and can resume it later from the same point

 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        draw_list(draw_info, {i: draw_info.GREEN, i-1:draw_info.RED}, True)
        time.sleep(0.5)
        heapify(arr, i, 0, ascending)
 


def main(): #the main piece of code where all the things happen
    running_program = True
    n = 15
    min_value = 0
    max_value = 100

    list_to_be_sorted = generate_list_to_be_sorted(n, min_value, max_value)

    ui_info = UIInfo(800, 600, list_to_be_sorted)

    sorting = False #var that know if we are sorting the list or not
    ascending = True # ascending sort ----- if false => descending sort

    sorting_algorithm = heap_sort
    sorting_algorithm_name = "Heap Sort"
    # sorting_algorithm_generator = None

    cnt = 0

    while running_program == True:
        pygame.display.update()    
        if cnt == 1:
            time.sleep(0.4)

        cnt = 1

        # if sorting: #if we are sorting, we try to call the 'next' method => next step in the generator
        #     try:
        #         next(sorting_algorithm_generator)
        #     except StopIteration: #it means the generator is finished
        #         sorting = False
        # else:
        draw(ui_info)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_program = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r: #letter R
                sorting = False
                list_to_be_sorted = generate_list_to_be_sorted(n, min_value, max_value)
                ui_info.set_list(list_to_be_sorted)#now we display the new list
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True #we are sorting
                sorting_algorithm_generator = sorting_algorithm(ui_info, ascending)
            elif event.key == pygame.K_a and sorting == False:#ascending sort
                ascending = True
            elif event.key == pygame.K_d and sorting == False:#descending sort
                ascending = False

    pygame.quit()

    print(list_to_be_sorted)


if __name__ == "__main__":
    main()