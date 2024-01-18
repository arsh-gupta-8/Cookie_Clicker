import pygame

pygame.init()

# Text
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

# Screen
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Cookie Clicker")
cookie_img = pygame.image.load("cookie.png")
cookie = pygame.transform.scale(cookie_img, (250, 250))
cookie2 = pygame.transform.scale(cookie_img, (300, 300))

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 30

# Game Setting
cookies = 0
enlarge = False

def write(text):
    write_line = font.render("Cookies: " + str(text), False, (0, 0, 0))
    screen.blit(write_line, (0, 0))


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

    screen.fill((4, 146, 194))
    write(cookies)
    if enlarge == True:
        screen.blit(cookie2, (50, 65))
    else:
        screen.blit(cookie, (75, 90))
    pygame.display.update()
    clock.tick(FPS)


