import pygame 

pygame.init() 


WHITE = (153,255,255)
size = (1600,900)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (80, 60))


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
                    y -= 100
                elif event.key == pygame.K_DOWN:
                    y += 100

        screen.blit(airplane, (x, y))
        pygame.display.update()

runGame()
pygame.quit()
