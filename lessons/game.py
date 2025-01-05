import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My first game')

GREY = (128, 128, 128)
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#print(event)
    gameDisplay.fill(GREY)
    pygame.display.update()
    clock.tick(60)