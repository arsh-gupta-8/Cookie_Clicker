import pygame

pygame.init()

# Text
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))

# Screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cookie Clicker")

# Loop Start
clock = pygame.time.Clock()
running = True
FPS = 60

# Game Setting
cookies = 0


def write(text):
    write_line = my_font.render(text, False, (0, 0, 0))
    screen.blit(write_line, (0, 0))


while running:
    clock.tick(FPS)
    pygame.display.update()
    write(cookies)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cookies += 1

        if event.type == pygame.MOUSEBUTTONUP:
            cookies += 1


