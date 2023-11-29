import pygame
import os
import random as rd
import pygame_gui

pygame.init()


screen_width = 600
screen_height = 300 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Card Display")


card_directory = r"C:\Users\VR_Teacher\Desktop\20418\data__"


card_file = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


deck = card_file * 3


card_width = 120
card_height = 180


gui_manager = pygame_gui.UIManager((screen_width, screen_height))


button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((20, 200), (100, 50)),  
    text="CARD",  
    manager=gui_manager
)

point_text = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((150, 200), (100, 50)),
    text="포인트: 0", 
    manager=gui_manager
)

jackpot_text = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((280, 200), (100, 50)),  
    text="", 
    manager=gui_manager
)

def update_point_text(points):
    point_text.set_text(f"points: {points}")

def update_jackpot_text(jackpot):
    if jackpot:
        jackpot_text.set_text("JACK POT!!")
    else:
        jackpot_text.set_text("")

def draw_cards():
    selected_cards = rd.choices(deck, k=5)

    x = 0
    for card in selected_cards:
        card_path = os.path.join(card_directory, f"{card}.png")
        card_image = pygame.image.load(card_path)
        card_image = pygame.transform.scale(card_image, (card_width, card_height))
        screen.blit(card_image, (x, 0))
        x += card_width

    card_counts = {}
    round_points = 0
    jackpot = False 

    for card in selected_cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    for card, count in card_counts.items():
        if count == 2:
            points = 2
        elif count == 3:
            points = 3
        elif count == 4:
            points = 4
        elif count == 5:
            points = 5
            jackpot = True
        else:
            points = 0
        round_points += points

    global total_points
    total_points += round_points
    update_point_text(total_points)
    update_jackpot_text(jackpot)

total_points = 0 

def update_screen():
    screen.fill((0, 0, 0))
    draw_cards()
    gui_manager.update(1/60.0) 
    gui_manager.draw_ui(screen)
    pygame.display.update()

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    draw_cards()
                    update_screen()

    gui_manager.process_events(event)
    
    gui_manager.update(1/60.0)
    gui_manager.draw_ui(screen)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
