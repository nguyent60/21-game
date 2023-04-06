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

# Define the start function
def start():
    global start_card
    your_card = random.randint(1, 10)
    start_card = your_card
    window.blit(font.render("Let's start with " + str(your_card), True, BLACK), (50, 100))
    game_check(take_card(your_card), opponent_card())

# Define the game check function
def game_check(a: int, b: int):
    window.fill(WHITE)
    window.blit(font.render("You have: " + str(a), True, BLACK), (50, 100))
    window.blit(font.render("They have: " + str(b), True, BLACK), (50, 150))
    if a > 21:
        text = font.render("They win.", True, BLACK)
        window.blit(text, (50, 200))
    elif a == b:
        text = font.render("It's a draw.", True, BLACK)
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
def take_card(a: int):
    window.fill(WHITE)
    b = random.randint(1, 10)
    window.blit(font.render("Let's start with " + str(start_card), True, BLACK), (50, 50))
    window.blit(font.render("You draw: ", True, BLACK), (50, 100))
    window.blit(font.render("Your card value now: ", True, BLACK), (50, 150))
    pygame.draw.rect(window, BLACK, (170, 100, 30, 30))
    pygame.draw.rect(window, BLACK, (310, 150, 30, 30))
    pygame.display.update()
    for i in range(10, 50):
        pygame.draw.rect(window, WHITE, (170 + i-10, 100, 30, 30))
        pygame.draw.rect(window, WHITE, (310 + i-10, 150, 30, 30))
        pygame.draw.rect(window, BLACK, (170 + i, 100, 30, 30))
        pygame.draw.rect(window, BLACK, (310 + i, 150, 30, 30))
        pygame.display.update()
        pygame.time.delay(10)
    window.blit(font.render(str(b), True, BLACK), (200, 100))
    window.blit(font.render(str(a + b), True, BLACK), (330, 150))
    pygame.display.update()
    window.blit(font.render("Opponent draws their card.", True, BLACK), (50, 200))
    window.blit(font.render("Press [d] to draw next card", True, BLACK), (50, 300))
    window.blit(font.render("Press [c] to check cards", True, BLACK), (50, 350))
    pygame.display.update()
    user_input = None
    while user_input not in ('d', 'c', pygame.QUIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.unicode == 'd':
                    return take_card(a + b)
                elif event.unicode == 'c':
                    game_check(a, opponent_card())
                user_input = event.unicode

    return int(a + b)

# Define the opponent card function
def opponent_card():
    return random.randint(15, 21)

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
        window.blit(font.render("Press [s] to start.", True, BLACK), (50, 300))
        window.blit(font.render("Or Press [x] to quit the game", True, BLACK), (50, 350))

        pygame.display.update()
# Quit Pygame
pygame.quit()
