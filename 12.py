import pygame 

pygame.init() 


WHITE = (153,255,255)
size = (1600,900)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

airplane = pygame.image.load('images/plane.png')
airplane = pygame.transform.scale(airplane, (80, 60))
DISPLAYSURF = pygame.display.set_mode((800,600))
DISPLAYSURF.blit(plain,Img,(airplain_pos_x,airplain_pos_y))



def runGame():
    global done, airplane
    x = 20
    y = 24

    while not done:
        clock.tick(60)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    airplain_moving_horizontal -= airplain_moving_speed
                elif event.key == pygame.K_DOWN:
                    airplain_moving_horizontal += airplain_moving_speed
                if event.key == pygame.K_LEFT:
                    airplain_moving_vertical -= airplain_moving_speed
                elif event.key == pygame.K_RIGHT:
                    airplain_moving_vertical += airplain_moving_speed

        screen.blit(airplane, (x, y))
        pygame.display.update()

runGame()
pygame.quit()
