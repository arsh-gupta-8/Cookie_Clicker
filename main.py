import pygame

pygame.init()

# Text
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

# Screen
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Cookie Clicker")

# Image imports
cookie_img = pygame.image.load("cookie.png")
cookie = pygame.transform.scale(cookie_img, (250, 250))
cookie2 = pygame.transform.scale(cookie_img, (300, 300))
# Shop items already have correct dimensions
shop_cursor = pygame.image.load("shop_items/shop_item_cursor.png")
shop_tree = pygame.image.load("shop_items/shop_item_tree.png")
shop_oven = pygame.image.load("shop_items/shop_item_oven.png")
shop_bakery = pygame.image.load("shop_items/shop_item_bakery.png")
cursor_resize = pygame.transform.scale(shop_cursor, (310, 110))
tree_resize = pygame.transform.scale(shop_tree, (310, 110))
oven_resize = pygame.transform.scale(shop_oven, (310, 110))
bakery_resize = pygame.transform.scale(shop_bakery, (310, 110))

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 30

# Game Setting
cookies = 0
enlarge = False
shop_scroll = 0

def write(text):
    write_line = font.render("Cookies: " + str(text), False, (0, 0, 0))
    screen.blit(write_line, (0, 0))

def show_buttons(shop_scroll):
    if enlarge == True:
        screen.blit(cookie2, (50, 65))
    else:
        screen.blit(cookie, (75, 90))
    if 500 <= x <= 800 and 15 + shop_scroll <= y <= 115 + shop_scroll:
        screen.blit(cursor_resize, (495, 10 + shop_scroll))
    else:
        screen.blit(shop_cursor, (500, 15 + shop_scroll))
    if 500 <= x <= 800 and 135 + shop_scroll <= y <= 235 + shop_scroll:
        screen.blit(tree_resize, (495, 130 + shop_scroll))
    else:
        screen.blit(shop_tree, (500, 135 + shop_scroll))
    if 500 <= x <= 800 and 255 + shop_scroll <= y <= 355 + shop_scroll:
        screen.blit(oven_resize, (495, 250 + shop_scroll))
    else:
        screen.blit(shop_oven, (500, 255 + shop_scroll))
    if 500 <= x <= 800 and 375 + shop_scroll <= y <= 475 + shop_scroll:
        screen.blit(bakery_resize, (495, 370 + shop_scroll))
    else:
        screen.blit(shop_bakery, (500, 375 + shop_scroll))




while running:

    x, y = pygame.mouse.get_pos()
    if 75 <= x <= 325 and 90 <= y <= 340:
        enlarge = True
    else:
        enlarge = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and 75 <= x <= 325 and 90 <= y <= 340:
                cookies += 1

            elif 480 <= x <= 820:
                if event.button == 4 and shop_scroll < 0:
                    shop_scroll += 45

                elif event.button == 5:
                    shop_scroll -= 45

    screen.fill((4, 146, 194))
    write(cookies)
    show_buttons(shop_scroll)
    pygame.display.update()
    clock.tick(FPS)


