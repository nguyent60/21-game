import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Blackjack")
bg = pygame.image.load("game_bg.jpg")
bg = pygame.transform.scale(bg, (1000, 600))
intro = pygame.image.load("front_bg.jpg")
intro = pygame.transform.scale(intro, (1000, 600))
# Set up the fonts
font = pygame.font.SysFont("Arial", 28)

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
cards_owned = []
bot1_owned = []
bot2_owned = []
bot3_owned = []
your_list = []
bot1_list = []
bot2_list = []
bot3_list = []

def random_card(list, total, count):
    count += 1
    number = random.randint(1, 11)
    if number == 11:
        total += 10
        new_num = random.randint(1,3)
        if new_num == 1:
            list.append("J")
        elif new_num == 2:
            list.append("Q")
        elif new_num == 3:
            list.append("K")
    elif number == 1:
        list.append("A")
        if list == your_list:
            total = ace_window(total)
        else:
            if total <= 10:
                total += 11
            else:
                total += 1
    else:
        list.append(number)
        total += number
    return total, count
        

# Define the start function
def start():
    global your_total, bot1_total, bot2_total, bot3_total, your_last, bot1_last, bot2_last, bot3_last, ace_count
    global your_count, bot1_count, bot2_count, bot3_count, you_stopped, bot1_stopped, bot2_stopped, bot3_stopped
    ace_count = 0
    you_stopped = False
    bot1_stopped = False
    bot2_stopped = False
    bot3_stopped = False
    your_first = 150
    bot1_first = 500
    bot2_first = 500
    bot3_first = 750
    your_last = your_first + 50
    bot1_last = bot1_first + 50
    bot2_last = bot2_first + 50
    bot3_last = bot3_first + 50
    your_count = 0
    bot1_count = 0
    bot2_count = 0
    bot3_count = 0
    your_total = 0
    bot1_total = 0
    bot2_total = 0
    bot3_total = 0
    cards_owned.clear()
    bot1_owned.clear()
    bot2_owned.clear()
    bot3_owned.clear()
    your_list.clear()
    bot1_list.clear()
    bot2_list.clear()
    bot3_list.clear()
    cards_owned.append((window, BLUE, (your_first, 200, 30, 40)))
    bot1_owned.append((window, BLUE, (bot1_first, 450, 30, 40)))
    bot2_owned.append((window, BLUE, (bot2_first, 50, 30, 40)))
    bot3_owned.append((window, BLUE, (bot3_first, 200, 30, 40)))
    cards_owned.append((window, BLUE, (your_last, 200, 30, 40)))
    bot1_owned.append((window, BLUE, (bot1_last, 450, 30, 40)))
    bot2_owned.append((window, BLUE, (bot2_last, 50, 30, 40)))
    bot3_owned.append((window, BLUE, (bot3_last, 200, 30, 40)))
    your_total, your_count = random_card(your_list, your_total, your_count)
    bot1_total, bot1_count = random_card(bot1_list, bot1_total, bot1_count)
    bot2_total, bot2_count = random_card(bot2_list, bot2_total, bot2_count)
    bot3_total, bot3_count = random_card(bot3_list, bot3_total, bot3_count)
    your_total, your_count = random_card(your_list, your_total, your_count)
    bot1_total, bot1_count = random_card(bot1_list, bot1_total, bot1_count)
    bot2_total, bot2_count = random_card(bot2_list, bot2_total, bot2_count)
    bot3_total, bot3_count = random_card(bot3_list, bot3_total, bot3_count)
    set_deck()

def set_card(list, condition):
    deck = pygame.Rect(500, 200, 30, 40)
    dist = 5
    if condition == False:
        card = list[-1]
        rect = card[2]
        rect_x = rect[0]
        rect_y = rect[1]
        while deck.x != rect_x or deck.y != rect_y:
            if deck.x > rect_x and deck.x - rect_x > dist:
                deck.x -= dist
            elif deck.x < rect_x and rect_x - deck.x > dist:
                deck.x += dist
            else:
                deck.x = rect_x
            if deck.y > rect_y and deck.y - rect_y > dist:
                deck.y -= dist
            elif deck.y < rect_y and rect_y - deck.y > dist:
                deck.y += dist
            else:
                deck.y = rect_y
            window.fill(WHITE)
            window.blit(bg, (0,0))
            for rect in cards_owned:
                if rect is not cards_owned[-1]:
                    pygame.draw.rect(rect[0], rect[1], rect[2])
            for rect in bot1_owned:
                if rect is not bot1_owned[-1]:
                    pygame.draw.rect(rect[0], rect[1], rect[2])
            for rect in bot2_owned:
                if rect is not bot2_owned[-1]:
                    pygame.draw.rect(rect[0], rect[1], rect[2])
            for rect in bot3_owned:
                if rect is not bot3_owned[-1]:
                    pygame.draw.rect(rect[0], rect[1], rect[2])
            pygame.draw.rect(window, BLUE, (500, 200, 30, 40))
            pygame.draw.rect(window, BLUE, deck)
            pygame.display.update()
            pygame.time.delay(5)
    

def set_deck():
    window.fill(WHITE)
    window.blit(bg, (0,0))
    global cards_owned, bot1_owned, bot2_owned, bot3_owned
    global you_stopped, bot1_stopped, bot2_stopped, bot3_stopped
    if you_stopped == False:
        set_card(cards_owned, you_stopped)
    if you_stopped == True:
        set_card(bot1_owned, bot1_stopped)
    if bot1_stopped == True:
        set_card(bot2_owned, bot2_stopped)
    if bot2_stopped == True: 
        set_card(bot3_owned, bot3_stopped)
    draw_board()
    
# Define the game check function
def draw_result(a: int, b: int, c: int, d: int):
    window.fill(WHITE)
    window.blit(bg, (0,0))
    window.blit(font.render("You have: " + str(a), True, WHITE), (50, 150))
    window.blit(font.render("Bot1 have: " + str(b), True, WHITE), (50, 200))
    window.blit(font.render("Bot2 have: " + str(c), True, WHITE), (50, 250))
    window.blit(font.render("Bot3 have: " + str(d), True, WHITE), (50, 300))
    window.blit(font.render("Your cards: " + str(your_count), True, WHITE), (450, 150))
    window.blit(font.render("Bot1 cards: " + str(bot1_count), True, WHITE), (450, 200))
    window.blit(font.render("Bot2 cards: " + str(bot2_count), True, WHITE), (450, 250))
    window.blit(font.render("Bot3 cards: " + str(bot3_count), True, WHITE), (450, 300))
    if (a > 21 and b > 21 and c > 21 and d > 21) or a == b == c == d:
        text = font.render("It's a draw!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a <= 21 and b <= 21 and c <= 21 and d <= 21):
        if your_count > bot1_count and your_count > bot2_count and your_count > bot3_count and your_count == 5:
            text = font.render("You win! Congrats", True, WHITE)
            window.blit(text, (400, 50))
        elif bot1_count > your_count and bot1_count > bot2_count and bot1_count > bot3_count and bot1_count == 5:
            text = font.render("Bot1 win!", True, WHITE)
            window.blit(text, (400, 50))
        elif bot2_count > your_count and bot2_count > bot1_count and bot2_count > bot3_count and bot2_count == 5:
            text = font.render("Bot2 win!", True, WHITE)
            window.blit(text, (400, 50))
        elif bot3_count > your_count and bot3_count > bot1_count and bot3_count > bot2_count and bot3_count == 5:
            text = font.render("Bot3 win!", True, WHITE)
            window.blit(text, (400, 50))
        elif (a < b and c < b and d < b):
            text = font.render("Bot1 win!", True, WHITE)
            window.blit(text, (400, 50))
        elif (b < a and c < a and d < a):
            text = font.render("You win! Congrats", True, WHITE)
            window.blit(text, (400, 50))
        elif (a < c and b < c and d < c):
            text = font.render("Bot2 win!", True, WHITE)
            window.blit(text, (400, 50))
        elif (a < d and b < d and c < d):
            text = font.render("Bot3 win!", True, WHITE)
            window.blit(text, (400, 50))
    elif (b > 21 and c > 21 and d > 21 and a <= 21):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and c > 21 and d > 21 and b <= 21):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and b > 21 and d > 21 and c <= 21):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and b > 21 and c > 21 and d <= 21):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and b <= 21 and ((b > c and b > d) or bot1_count == 5)):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and c <= 21 and ((c > b and c > d) or bot2_count == 5)):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and d <= 21 and ((d > b and d > c) or bot3_count == 5)):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and a <= 21 and ((a > c and a > d) or your_count == 5)):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50)) 
    elif (b > 21 and c <= 21 and ((c > a and c > d) or bot2_count == 5)):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and d <= 21 and ((d > a and d > c) or bot3_count == 5)):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (c > 21 and a <= 21 and ((a > b and a > d) or your_count == 5)):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50))
    elif (c > 21 and b <= 21 and ((b > d and b > a) or bot1_count == 5)):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (c > 21 and d <= 21 and ((d > a and d > b) or bot3_count == 5)):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (d > 21 and a <= 21 and ((a > b and a > c) or your_count == 5)):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50))
    elif (d > 21 and b <= 21 and ((b > c and b > a) or bot1_count == 5)):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (d > 21 and c <= 21 and ((c > a and c > b) or bot2_count == 5)):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and b > 21 and c < d and d <= 21):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and b > 21 and c > d and c <= 21):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and c > 21 and b > d and b <= 21):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and c > 21 and b < d and d <= 21):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and d > 21 and b < c and c <= 21):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and d > 21 and b > c and b <= 21):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and c > 21 and a < d and d <= 21):
        text = font.render("Bot3 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and c > 21 and a > d and a <= 21):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and d > 21 and a > c and a <= 21):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and d > 21 and a < c and c <= 21):
        text = font.render("Bot2 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (c > 21 and d > 21 and a < b and b <= 21):
        text = font.render("Bot1 win!", True, WHITE)
        window.blit(text, (400, 50))
    elif (c > 21 and d > 21 and a > b and a <= 21):
        text = font.render("You win! Congrats", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and b > 21 and c == d and c <= 21) or (c == d and c <= 21 and (a < c and b > 21) or (b < c and a > 21)):
        text = font.render("It's a draw for bots 2 and 3!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and c > 21 and b == d and b <= 21) or (b == d and b <= 21 and (a < b and c > 21) or (c < b and a > 21)):
        text = font.render("It's a draw for bots 1 and 3!", True, WHITE)
        window.blit(text, (400, 50))
    elif (a > 21 and d > 21 and b == c and b <= 21) or (b == c and b <= 21 and (a < b and d > 21) or (d < b and a > 21)):
        text = font.render("It's a draw for bots 1 and 2!", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and c > 21 and a == d and a <= 21) or (a == d and a <= 21 and (c < a and b > 21) or (b < a and c > 21)):
        text = font.render("It's a draw for you and bot 3!", True, WHITE)
        window.blit(text, (400, 50))
    elif (b > 21 and d > 21 and a == c and a <= 21) or (a == c and a <= 21 and (b < a and d > 21) or (d < a and b > 21)):
        text = font.render("It's a draw for you and bot 2!", True, WHITE)
        window.blit(text, (400, 50))
    elif (c > 21 and d > 21 and a == b and a <= 21) or (a == b and a <= 21 and (c < a and d > 21) or (d < a and c > 21)):
        text = font.render("It's a draw for you and bot 1!", True, WHITE)
        window.blit(text, (400, 50))
    window.blit(font.render("[s] to start again", True, WHITE), (400, 400))
    window.blit(font.render("[x] to quit", True, WHITE), (400, 450))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.unicode == 'x'):
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.unicode == 's':
            start()
    pygame.display.update()


def card_check(a: int, b: int, c: int, d: int):
    window.fill(WHITE)
    window.blit(bg, (0,0))
    window.blit(font.render("You:", True, WHITE), (50, 200))
    window.blit(font.render("Bot1:", True, WHITE), (300, 450))
    window.blit(font.render("Bot2:", True, WHITE), (300, 50))
    window.blit(font.render("Bot3:", True, WHITE), (650, 200))
    window.blit(font.render("Total:", True, WHITE), (50, 250))
    window.blit(font.render("Total:", True, WHITE), (300, 500))
    window.blit(font.render("Total:", True, WHITE), (300, 100))
    window.blit(font.render("Total:", True, WHITE), (650, 250))
    for rect in cards_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    for rect in bot1_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    for rect in bot2_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    for rect in bot3_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render(str(a), True, WHITE), (122, 250))
    window.blit(font.render(str(b), True, WHITE), (372, 500))
    window.blit(font.render(str(c), True, WHITE), (372, 100))
    window.blit(font.render(str(d), True, WHITE), (720, 250))
    pygame.display.update()
    for rect in cards_owned:
        if your_list:
            rect_x = rect[2][0]
            rect_y = rect[2][1]
            for i in range(1, 5):
                pygame.draw.rect(window, GREEN, (rect_x, rect_y, 7*i, 38))
                pygame.display.update()
                pygame.time.delay(10)
            window.blit(font.render(str(your_list[0]), True, BLACK), (rect_x + 2, rect_y))
            pygame.display.update()
            pygame.time.delay(400)
            your_list.remove(your_list[0])
    for rect in bot1_owned:
        if bot1_list:
            rect_x = rect[2][0]
            rect_y = rect[2][1]
            for i in range(1, 5):
                pygame.draw.rect(window, GREEN, (rect_x, rect_y, 7*i, 38))
                pygame.display.update()
                pygame.time.delay(10)
            window.blit(font.render(str(bot1_list[0]), True, BLACK), (rect_x + 2, rect_y))
            pygame.display.update()
            pygame.time.delay(400)
            bot1_list.remove(bot1_list[0])
    for rect in bot2_owned:
        if bot2_list:
            rect_x = rect[2][0]
            rect_y = rect[2][1]
            for i in range(1, 5):
                pygame.draw.rect(window, GREEN, (rect_x, rect_y, 7*i, 38))
                pygame.display.update()
                pygame.time.delay(10)
            window.blit(font.render(str(bot2_list[0]), True, BLACK), (rect_x + 2, rect_y))
            pygame.display.update()
            pygame.time.delay(400)
            bot2_list.remove(bot2_list[0])
    for rect in bot3_owned:
        if bot3_list:
            rect_x = rect[2][0]
            rect_y = rect[2][1]
            for i in range(1, 5):
                pygame.draw.rect(window, GREEN, (rect_x, rect_y, 7*i, 38))
                pygame.display.update()
                pygame.time.delay(10)
            window.blit(font.render(str(bot3_list[0]), True, BLACK), (rect_x + 2, rect_y))
            pygame.display.update()
            pygame.time.delay(400)
            bot3_list.remove(bot3_list[0])
    pygame.time.delay(500)
    draw_result(a, b, c, d)
                

def ace_window(total):
    global your_last
    window.fill(WHITE)
    window.blit(bg, (0, 0))
    pygame.draw.rect(window, BLUE, (500, 200, 30, 40))
    window.blit(font.render("YOU GOT AN ACE", True, WHITE), (20, 150))
    window.blit(font.render("[a]: HIT 1", True, WHITE), (350, 300))
    window.blit(font.render("[d]: HIT 11", True, WHITE), (350, 350))
    window.blit(font.render("Total:", True, WHITE), (50, 250))
    for rect in cards_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render(str(your_total), True, WHITE), (130, 250))
    window.blit(font.render("Bot1 draws:", True, WHITE), (300, 450))
    if bot1_stopped == True:
        window.blit(font.render("Bot1 stayed!", True, WHITE), (300, 500))
    for rect in bot1_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render("Bot2 draws:", True, WHITE), (300, 50))
    if bot2_stopped == True:
        window.blit(font.render("Bot2 stayed!", True, WHITE), (300, 100))
    for rect in bot2_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render("Bot3 draws:", True, WHITE), (600, 200))
    if bot3_stopped == True:
        window.blit(font.render("Bot3 stayed!", True, WHITE), (600, 250))
    for rect in bot3_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    pygame.display.update()
    card_dimension = your_last
    for iter in range(1, 5):
        pygame.draw.rect(window, GREEN, (card_dimension, 201, 7 * iter, 38))
        pygame.display.update()
        pygame.time.delay(20)
    window.blit(font.render(str(your_list[-1]), True, BLACK), (card_dimension + 2, 200))
    pygame.display.update()
    user_input = None
    while user_input not in ('a', 'd', pygame.QUIT):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.unicode == 'a':
                    total += 1
                    return total
                elif event.unicode == 'd':
                    total += 11
                    return total
                user_input = event.unicode
    
# Define the take card function
def draw_board():
    global your_total, bot1_total, bot2_total, bot3_total, your_last, bot1_last, bot2_last, bot3_last
    global your_count, bot1_count, bot2_count, bot3_count, bot1_stopped, bot2_stopped, bot3_stopped, you_stopped
    window.fill(WHITE)
    window.blit(bg, (0, 0))
    pygame.draw.rect(window, BLUE, (500, 200, 30, 40))
    if not you_stopped: 
        window.blit(font.render("[d]: HIT", True, WHITE), (350, 300))
        window.blit(font.render("[c]: STAND", True, WHITE), (350, 350))
    else:
        window.blit(font.render("[d]: NEXT", True, WHITE), (350, 300))
        window.blit(font.render("[c]: NEXT", True, WHITE), (350, 350))
    window.blit(font.render("You draw: ", True, WHITE), (20, 200))
    window.blit(font.render("Total: ", True, WHITE), (20, 250))
    if you_stopped == True:
        window.blit(font.render("You stayed!", True, WHITE), (20, 300))
    for rect in cards_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render("Bot1 draws:", True, WHITE), (300, 450))
    if bot1_stopped == True:
        window.blit(font.render("Bot1 stayed!", True, WHITE), (300, 500))
    for rect in bot1_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render("Bot2 draws:", True, WHITE), (300, 50))
    if bot2_stopped == True:
        window.blit(font.render("Bot2 stayed!", True, WHITE), (300, 100))
    for rect in bot2_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    window.blit(font.render("Bot3 draws:", True, WHITE), (600, 200))
    if bot3_stopped == True:
        window.blit(font.render("Bot3 stayed!", True, WHITE), (600, 250))
    for rect in bot3_owned:
        pygame.draw.rect(rect[0], rect[1], rect[2])
    pygame.display.update()
    last_card = cards_owned[-1]
    card_dimension = last_card[2][0] + 1
    for iter in range(1, 5):
        pygame.draw.rect(window, GREEN, (card_dimension, 201, 7 * iter, 38))
        pygame.display.update()
        pygame.time.delay(20)
    window.blit(font.render(str(your_list[-1]), True, BLACK), (card_dimension + 2, 200))
    window.blit(font.render(str(your_total), True, WHITE), (130, 250))
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
                    if you_stopped == False and your_count != 5:
                        cards_owned.append((window, BLUE, (your_last, 200, 30, 40)))
                        your_total, your_count = random_card(your_list, your_total, your_count)
                    else:
                        if 18 > bot1_total and bot1_count != 5:
                            bot1_last += 50
                            bot1_owned.append((window, BLUE, (bot1_last, 450, 30, 40)))
                            bot1_total, bot1_count = random_card(bot1_list, bot1_total, bot1_count)
                        else:
                            bot1_stopped = True
                            if 18 > bot2_total and bot2_count != 5:
                                bot2_last += 50
                                bot2_owned.append((window, BLUE, (bot2_last, 50, 30, 40)))
                                bot2_total, bot2_count = random_card(bot2_list, bot2_total, bot2_count)
                            else:
                                bot2_stopped = True
                                if 18 > bot3_total and bot3_count != 5:
                                    bot3_last += 50
                                    bot3_owned.append((window, BLUE, (bot3_last, 200, 30, 40)))
                                    bot3_total, bot3_count = random_card(bot3_list, bot3_total, bot3_count)
                                else:
                                    bot3_stopped = True
                    if you_stopped == bot1_stopped == bot2_stopped == bot3_stopped == True:
                        card_check(your_total, bot1_total, bot2_total, bot3_total)
                    else:
                        set_deck()
                elif event.unicode == 'c':
                    you_stopped = True
                    if 18 > bot1_total and bot1_count != 5:
                        bot1_last += 50
                        bot1_owned.append((window, BLUE, (bot1_last, 450, 30, 40)))
                        bot1_total, bot1_count = random_card(bot1_list, bot1_total, bot1_count)
                    else:
                        bot1_stopped = True
                        if 18 > bot2_total and bot2_count != 5:
                            bot2_last += 50
                            bot2_owned.append((window, BLUE, (bot2_last, 50, 30, 40)))
                            bot2_total, bot2_count = random_card(bot2_list, bot2_total, bot2_count)    
                        else:
                            bot2_stopped = True
                            if 18 > bot3_total and bot3_count != 5 and you_stopped == bot1_stopped == bot2_stopped == True:
                                bot3_last += 50
                                bot3_owned.append((window, BLUE, (bot3_last, 200, 30, 40)))
                                bot3_total, bot3_count = random_card(bot3_list, bot3_total, bot3_count)
                            else:
                                bot3_stopped = True
                    if you_stopped == bot1_stopped == bot2_stopped == bot3_stopped == True:
                        card_check(your_total, bot1_total, bot2_total, bot3_total)
                    else:
                        set_deck()
                user_input = event.unicode

# Game loop
game_started = False
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)
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
        window.blit(intro, (0,0))
        window.blit(font.render("[s] to start", True, WHITE), (400, 400))
        window.blit(font.render("[x] to quit", True, WHITE), (400, 450))

        pygame.display.flip()
# Quit Pygame
pygame.quit()
