import pygame

pygame.init()


WHITE = (255,255,255)
size = (400,300)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (60, 45))

character_speed = 2

def runGame():
    global done, airplane
    x = 20
    y = 24

    while True:
        clock.tick(10)
        screen.fill(WHITE)
        
        while True:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT]:
                player.x += 5
            if pressed[pygame.K_DOWN]:
                player.y += 5
            if pressed[pygame.K_LEFT]:
                player.x -= 5
            if pressed[pygame.K_UP]:
                player.y -= 5


            screen.blit(airplane, (x, y))
            pygame.display.update()

runGame()
pygame.quit()


