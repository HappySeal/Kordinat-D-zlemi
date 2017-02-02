import pygame
BLACK = (0  ,0  ,0  )
WHITE = (255,255,255)
RED =   (255,0  ,0  )
GREEN = (0  ,255,0  )
BLUE =  (0  ,0  ,255)

pygame.init()

displayH = 500
displayW = 500
gameDisplay = pygame.display.set_mode((displayW,displayH))
pygame.display.set_caption("Kordinat Sistemi")
clock = pygame.time.Clock()
def text_objects(text,font):
    textSurface = font.render(text,True,BLACK)
    return textSurface,textSurface.get_rect()

def cord_display(text,x,y):
    normalText = pygame.font.Font("font.ttf",14)
    TextSurf , TextRect = text_objects(text,normalText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def func_display(text):
    normalText = pygame.font.Font("font.ttf",14)
    TextSurf , TextRect = text_objects(text,normalText)
    TextRect.center = (430,490)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def dogru(x1,y1,x2,y2,color,bold):
    pygame.draw.line(gameDisplay,color,[x1,y1],[x2,y2],bold)

def cords(x,y):
    a = "("+str(-(round(((displayW/2)-x)/10)))+","+str(round(((displayH/2)-y)/10))+")"
    cord_display(a,x,y)

def func(startX,startY,endX,endY):
    try:
        m1 = (round(((displayH/2)-endY)/10))-(round(((displayH/2)-startY)/10))
        m2 = (-(round(((displayW/2)-endX)/10)))-(-(round(((displayW/2)-startX)/10)))
        m = m1/m2
        n = round(((round(((displayH/2)-endY)/10)) - (m*(-(round(((displayW/2)-endX)/10))))),3)
    except ZeroDivisionError:
        m= 0
        n = 0
    text = "y="+str(m1)+"/"+str(m2)+"x+"+str(n)
    func_display(text)

def game_loop():

    gameExit = False

    startX = 0
    startY = 0
    endX = 0
    endY = 0

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    posStart = list(pygame.mouse.get_pos())
                    startX = posStart[0]
                    startY = posStart[1]
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        posEnd = list(pygame.mouse.get_pos())
                        endX = posEnd[0]
                        endY = posEnd[1]

        gameDisplay.fill(WHITE)


        pygame.draw.line(gameDisplay,BLACK,[0,displayH/2],[displayW,displayH/2],3)
        pygame.draw.line(gameDisplay,BLACK,[displayW/2,0],[displayW/2,displayH],3)

        dogru(startX,startY,endX,endY,RED,3)
        cords(startX,startY)
        cords(endX,endY)
        func(startX,startY,endX,endY)

        pygame.display.flip()
        clock.tick(30)

game_loop()
pygame.quit()
quit()