import pygame, sys, time, random
from pygame.locals import *
#pygame初始化
pygame.init()
#创建fpsClock变量，用来控制游戏的速度（帧率（Frame rate）是用于测量显示帧数的量度，所谓的测量单位为每秒显示帧数(Frames per Second，简称：FPS），此处用其得到物体移动的效果。FPS越大，画面越流畅，移动的速度就越快。
fpsClock = pygame.time.Clock()
#新建一个窗口，标题为Raspberry Snake
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Raspberry Snake')

#定义一些颜色。
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
#初始化程序中用到的变量。
snakePosition = [100,100]
snakeSegments = [[100,100],[80,100],[60,100]]
raspberryPosition = [300,300]
raspberrySpawned = 1
direction = 'right'
changeDirection = direction

#定义游戏结束函数。用大号字体将Game Over打印在屏幕上，停留5秒钟，然后退出pygame和Python程序。你也可以自己去设计结束函数。
def gameOver():
    # 通过字体文件获得字体对象。
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    # 配置要显示的文字。
    gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
    # 获得要显示的对象的rect，以便于设置其坐标位置。
    gameOverRect = gameOverSurf.get_rect()
        # 设置显示对象的坐标。
    gameOverRect.midtop = (320, 10)
    # 绘制字体。
    playSurface.blit(gameOverSurf, gameOverRect)
    #更新整个待显示的Surface对象到屏幕上。
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
#主循环程序
while True:
#对一些键盘操作的设置。QUIT是指按“ESC”健。
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
#控制蛇的移动方向，按照输入移动。
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                changeDirection = 'left'
            if event.key == K_UP or event.key == ord('w'):
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
#每次移动的距离。
    if direction == 'right':
        snakePosition[0] += 20
    if direction == 'left':
        snakePosition[0] -= 20
    if direction == 'up':
        snakePosition[1] -= 20
    if direction == 'down':
        snakePosition[1] += 20
#使蛇的身体变长，将蛇身体变长的部分放在头部。
    snakeSegments.insert(0,list(snakePosition))
#蛇是否吃掉树莓的两种结果。
    if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
        raspberrySpawned = 0
    else:
        snakeSegments.pop()
        # print(1)
    if raspberrySpawned == 0:
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        raspberryPosition = [int(x*20),int(y*20)]
    raspberrySpawned = 1

#进行绘制。
    playSurface.fill(blackColour)
    for position in snakeSegments:
            pygame.draw.rect(playSurface,whiteColour,Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface,redColour,Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
            pygame.display.flip()
#游戏结束条件。
    if snakePosition[0] > 620 or snakePosition[0] < 0:
        gameOver()
    if snakePosition[1] > 460 or snakePosition[1] < 0:
        gameOver()
    for snakeBody in snakeSegments[1:]:
        if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
            gameOver()
    #控制游戏速度。
    fpsClock.tick(10)
