import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blackjack")

# Set up the fonts
font = pygame.font.SysFont("Arial", 32)

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
cards_owned = []
bot1_owned = []
bot2_owned = []
bot3_owned = []


# Define the start function
def start():
    global your_total, bot1_total, your_last, bot1_last, bot2_last, your_count, bot1_count
    your_last = 150
    bot1_last = 400
    bot2_last = 260
    your_count = 0
    bot1_count = 0
    your_total = 0
    bot1_total = 0
    cards_owned.clear()
    bot1_owned.clear()
    cards_owned.append((window, BLACK, (your_last, 200, 30, 40)))
    cards_owned.append((window, BLUE, (your_last + 5, 205, 20, 30)))
    bot1_owned.append((window, BLACK, (bot1_last, 450, 30, 40)))
    bot1_owned.append((window, BLUE, (bot1_last + 5, 455, 20, 30)))
    draw_board()

# Define the game check function
def game_check(a: int, b: int):
    window.fill(WHITE)
    window.blit(font.render("You have: " + str(a), True, BLACK), (20, 100))
    window.blit(font.render("They have: " + str(b), True, BLACK), (20, 150))
    if (a > 21 and b > 21) or a == b:
        text = font.render("It's a draw.", True, BLACK)
        window.blit(text, (50, 200))
    elif b > 21 or your_count == 5:
        text = font.render("You win.", True, BLACK)
        window.blit(text, (50, 200))
    elif a > 21 and b <= 21:
        text = font.render("They win.", True, BLACK)
        window.blit(text, (50, 200))
    elif a < b:
        text = font.render("They win.", True, BLACK)
        window.blit(text, (50, 200))
    else:
        text = font.render("You win.", True, BLACK)
        window.blit(text, (50, 200))
    window.blit(font.render("Press [s] to play again", True, BLACK), (50, 300))
    window.blit(font.render("Or Press [x] to quit the game", True, BLACK), (50, 350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.unicode == 'x'):
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.unicode == 's':
            start()
    pygame.display.update()

# Define the take card function
def draw_board():
    global your_total, bot1_total, your_last, bot1_last, your_count, bot1_count
    window.fill(WHITE)
    window.blit(font.render("[d]: Draw card", True, BLACK), (20, 50))
    window.blit(font.render("[c]: Stay", True, BLACK), (20, 100))
    window.blit(font.render("You draw: ", True, BLACK), (20, 200))
    window.blit(font.render("Total: ", True, BLACK), (20, 250))
    for rect in cards_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render("Bot1 draws:", True, BLACK), (250, 450))
    for rect in bot1_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    pygame.display.update()
    last_card = cards_owned[-1]
    card_dimension = last_card[2][0]
    your_card = random.randint(1, 10)
    bot1_card = random.randint(1, 10)
    your_total += your_card
    bot1_total += bot1_card
    your_count += 1
    bot1_count += 1
    if bot1_total > 21:
        bot1_total = random.randint(18, 22)
    for iter in range(0, 50):
        pygame.draw.rect(window, WHITE, (card_dimension + iter-10, 200, 5, 40))
        pygame.display.update()
        pygame.time.delay(10)
    window.blit(font.render(str(your_card), True, BLACK), (card_dimension, 200))
    window.blit(font.render(str(your_total), True, BLACK), (130, 250))
    pygame.display.update()
    user_input = None
    while user_input not in ('d', 'c', pygame.QUIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.unicode == 'd':
                    your_last += 50
                    bot1_last += 50
                    cards_owned.append((window, BLACK, (your_last, 200, 30, 40)))
                    cards_owned.append((window, BLUE, (your_last + 5, 205, 20, 30)))
                    if bot1_total < 20 or bot1_count < 5:
                        bot1_owned.append((window, BLACK, (bot1_last, 450, 30, 40)))
                        bot1_owned.append((window, BLUE, (bot1_last + 5, 455, 20, 30)))
                    draw_board()
                elif event.unicode == 'c':
                    game_check(your_total, bot1_total)
                user_input = event.unicode

# Game loop
game_started = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.unicode == 'x' or event.key == pygame.K_ESCAPE)):
            running = False
        elif event.type == pygame.KEYDOWN and event.unicode == 's':
            game_started = True
            start()
            
    if game_started == False:
        # Fill the background with white
        window.fill(WHITE)
        # Draw the text
        window.blit(font.render("Welcome to our humble blackjack game", True, BLACK), (50, 50))
        window.blit(font.render("[s] to start", True, BLACK), (50, 300))
        window.blit(font.render("[x] to quit", True, BLACK), (50, 350))

        pygame.display.update()
# Quit Pygame
pygame.quit()
