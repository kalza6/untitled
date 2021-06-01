import pygame

pygame.init()


WHITE = (255,255,255)
size = [1600,900]
screen = pygame.display.set_mod(size)

done= False
clock=pygame.time.Clock()


airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))


def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=TRUE


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_UP:
                y -= 10
            elif event.key == pygame.k_down:
                y += 10

        screen.blit(airplane, (x, y))
        pygame.display.update()

runGame()
pygame.quit()

    
