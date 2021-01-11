import pygame

pygame.init()

display_width = 800
display_height = 200

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game Of Innovation')

black = (0,0,0)
white = (250,250,100)

clock = pygame.time.Clock()
crashed = False
#carImg = pygame.image.load('imag.png')
run=True
myfont = pygame.font.SysFont('arial', 70)
carImg = myfont.render('INNOVATION', 0, (250,0,0))

# method for image or the text inside the game.
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.0)
y = (display_height * 0.2)
x_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        # print (event)
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                if x_change ==100:
                    x_change = 0
            elif event.key == pygame.K_UP:
                x_change = 5
            elif event.key == pygame.K_DOWN:
                x_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0

    x += x_change
    print(x)
    if x == 770.0:
        print("its completed")
        x =  (-425.0)
        y = (display_height * 0.2)
        carImg = myfont.render('INNOVATION', 0, (250,0,0))
        gameDisplay.blit(carImg, (x,y))
        
    gameDisplay.fill(white)
    car(x,y)
        
    pygame.display.update()
    clock.tick(15)
pygame.quit()
quit()

#So again, the changed code is around the # signs. The main bit of logic here is:




