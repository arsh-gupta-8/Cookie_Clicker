import pygame
import math

pygame.init()

# Text
pygame.font.init()
cookie_display_font = pygame.font.SysFont('Comic Sans MS', 30)   # For Cookie Amount Display
stat_display_font = pygame.font.SysFont('Raleway Bold', 25)   # For Stat Display
multiplier_display_font = pygame.font.SysFont('Times New Roman', 25)   # For Multiplier Display

# Screen
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Cookie Clicker")

# Image imports
cookie_img = pygame.image.load("cookie.png")
cookie = pygame.transform.scale(cookie_img, (250, 250))
cookie_enlarged = pygame.transform.scale(cookie_img, (270, 270))
cookie_x = 125
cookie_y = 75

# Shop items already have correct dimensions
shop_item_icons = []
shop_item_icons_enlarged = []

shop_item_icons.append(pygame.image.load("shop_items/shop_item_cursor.png"))
shop_item_icons.append(pygame.image.load("shop_items/shop_item_tree.png"))
shop_item_icons.append(pygame.image.load("shop_items/shop_item_oven.png"))
shop_item_icons.append(pygame.image.load("shop_items/shop_item_bakery.png"))

for item in shop_item_icons:
    shop_item_icons_enlarged.append(pygame.transform.scale(item, (310, 110)))

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 30

# Game Setting
cookies = 0
enlarge = False
shop_scroll = 0
shop_keeper = []
shop_prices = []
item_clicks_storage = []
item_click_rate = []
for num in range(len(shop_item_icons)):
    shop_keeper.append(0)
    shop_prices.append(int("1" + "0" * (num + 1)))
    item_clicks_storage.append(0)
    item_click_rate.append(shop_prices[num]//10)
frame_iteration = 0
quantity_suffix = ["", "K", "M", "B", "T", "Qd", "Qn", "Sx", "Hept", "Oct", "Non", "Dec"]
multiplier = 1
multipliers = [1, 10, 100, "MAX"]


def decimal_divider(string):
    if len(string) > 3:
        str_rep = ""
        quant = quantity_suffix[(len(string) - 1) // 3]
        dec_places = (len(string)) % 3
        if dec_places == 0:
            str_rep += string[:3]
        elif dec_places == 2:
            if string[2] == '0':
                str_rep += string[:2]
            else:
                str_rep += string[:2] + "." + string[3]
        else:
            if string[2] == '0':
                if string[1] == '0':
                    str_rep += string[0]
                else:
                    str_rep += string[0] + "." + string[1]
            else:
                str_rep += string[0] + "." + string[1:3]
        str_rep += " " + quant
    else:
        str_rep = string
    return str_rep


def print_cookie_count(cookies):
    str_cookies = str(cookies)
    cookie_display_str = "Cookies: " + decimal_divider(str_cookies)
    write_line = cookie_display_font.render(cookie_display_str, False, (0, 0, 0))
    cookie_counter_width = write_line.get_width()
    screen.blit(write_line, (500//2 - cookie_counter_width//2, 5))


def show_buttons(cookies, shop_scroll, item_key, item_click_rate, shop_prices, shop_keeper, item_clicks_storage, mult):
    can_buy = 0
    if str(mult).isdigit():
        can_buy = mult
    else:
        can_buy = int(math.floor(cookies / shop_prices))
    difference = item_key*120
    if 500 <= x <= 800 and (20 + difference) + shop_scroll <= y <= 120 + difference + shop_scroll:
        screen.blit(shop_item_icons_enlarged[item_key], (495, 15 + difference + shop_scroll))
    else:
        screen.blit(shop_item_icons[item_key], (500, 20 + difference + shop_scroll))
    data_list = [item_click_rate*can_buy, shop_prices*can_buy, shop_keeper, item_clicks_storage]
    str_list = ["Cookies/S: ", "Price: ", "Owned: ", "Cooked: "]
    for display_data in range(4):
        stat_display_string = stat_display_font.render(str_list[display_data] + decimal_divider(str(data_list[display_data])), False, (150, 75, 0))
        str_width = stat_display_string.get_width()
        screen.blit(stat_display_string, (800 + 200//2 - str_width//2, 24 + difference + 25 * display_data + shop_scroll))


def shop_updater(shop_keeper, x, y, shop_scroll, cookies, mult):
    bg_colour = screen.get_at((x, y))[:3]
    item_index = (shop_scroll * -1) // 120 + (y-15) // 120
    can_buy = 0
    if str(mult).isdigit():
        can_buy = mult
    else:
        can_buy = int(math.floor(cookies / shop_prices[item_index]))
    if bg_colour != (4, 146, 194):
        if shop_prices[item_index] * can_buy <= cookies:
            shop_keeper[item_index] += 1 * can_buy
            cookies -= shop_prices[item_index] * can_buy
    print(shop_keeper)
    return shop_keeper, cookies


while running:

    x, y = pygame.mouse.get_pos()
    if 75 <= x <= 325 and 90 <= y <= 340:
        enlarge = True
    else:
        enlarge = False

    frame_iteration += 1

    if frame_iteration == FPS:
        for i in range(len(shop_keeper)):
            add_amount = shop_keeper[i] * item_click_rate[i]
            cookies += add_amount
            item_clicks_storage[i] += add_amount
        frame_iteration = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1 and 75 <= x <= 325 and 90 <= y <= 340:
                cookies += 1

            elif (event.button == 4 or event.button == 5) and 480 <= x <= 820:
                if event.button == 4 and shop_scroll < 0:
                    shop_scroll += 120

                elif event.button == 5:
                    shop_scroll -= 120

            elif event.button == 1 and 500 <= x <= 800 and y > 14:
                shop_keeper, cookies = shop_updater(shop_keeper, x, y, shop_scroll, cookies, multiplier)

            elif event.button == 1 and 420 <= x <= 480 and 20 <= y <= 50:
                current_mult = multipliers.index(multiplier)
                if current_mult == 3:
                    current_mult = 0
                else:
                    current_mult += 1
                multiplier = multipliers[current_mult]

    screen.fill((4, 146, 194))
    print_cookie_count(cookies)
    multi_buy_button = pygame.draw.rect(screen, (182, 123, 80), pygame.Rect(420, 20, 60, 30))
    multiplier_display = multiplier_display_font.render(str(multiplier), False, (152, 251, 152))
    multiplier_display_width = multiplier_display.get_width()
    screen.blit(multiplier_display, (420 + 60 // 2 - multiplier_display_width // 2, 20))
    if cookie_x <= x <= cookie_x+250 and cookie_y <= y <= cookie_y+250:
        screen.blit(cookie_enlarged, (cookie_x-10, cookie_y-10))
    else:
        screen.blit(cookie, (cookie_x, cookie_y))
    for item_key in range(len(shop_item_icons)):
        show_buttons(cookies, shop_scroll, item_key, item_click_rate[item_key], shop_prices[item_key], shop_keeper[item_key], item_clicks_storage[item_key], multiplier)
    pygame.display.update()
    clock.tick(FPS)


