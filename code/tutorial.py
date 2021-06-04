import pygame

pygame.init()


WHITE = (255,255,255)
size = (400,300)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))

character_speed = 0.6

def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= character_speed
                elif event.key == pygame.K_DOWN:
                    y += character_speed
                    MOVESPEED = 6

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


        screen.blit(airplane, (x, y))
        pygame.display.update()

runGame()
pygame.quit()
