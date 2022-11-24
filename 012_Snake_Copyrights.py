import pygame
import time
import random

pygame.init()
#       определение цветов
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (33, 10, 245)  # dark_blue
#       определение размеров экрана
dis_width = 800
dis_height = 400
#       шапка экрана
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Pythonist')
#       х.з. для чего это...))
clock = pygame.time.Clock()
#       длинна змейки и скорость змейки
snake_block = 10
snake_speed = 15
#      шрифты: формы и размеры
font_style = pygame.font.SysFont("algerian", 25)
score_font = pygame.font.SysFont("monotypecorsiva", 25)


#       функция вывода/отображения очков/баллов
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
    global s
    s = str(score)


#       функция отображения наращивания длинны змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


#       функция сообщения1
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3 - 60, dis_height / 3])  # координаты Начала текста


#       функция сообщения2
def message_2(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3 - 60, dis_height / 2])  # координаты Начала текста


#       главная функция цикла (петля)
def gameLoop():
    game_over = False
    game_close = False
    #      начальное положение змейки
    x1 = dis_width / 2
    y1 = dis_height / 2
    #       переменные координаты змейки
    x1_change = 0
    y1_change = 0
    #       определение состовляющих змейки
    snake_List = []
    Length_of_snake = 1
    #       определение координат еды: рандомное формирование
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    #       функция 2ого уровеня
    while not game_over:
        #       функция  сообщения для выбора: выйти  или продолжить
        while game_close == True:
            dis.fill(black)
            Your_score(Length_of_snake - 1)
            message(f"***Well Done!*** Your_score = {s} =", yellow)
            message_2(" Press C <-play_again or Q <-quit", red)
            pygame.display.update()
            #       цикл для Продолжения или Выхода из игры
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # выход
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # продолжить
                        gameLoop()
        #       цикл для управления движением змейки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        #       цикл остановки игры при достижении края экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change  # формирование финальной координаты змейки по горизонтали
        y1 += y1_change  # формирование финальной координаты змейки по вертикали
        dis.fill(blue)  # цвет фона игры
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])  # цвет еды змейки
        #       формирование хвоста змейки: наращивание при поглощении еды
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        #       окончание игры при хвост(посл.символ)=голова
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        #       вызов функций змейки и баллов
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        #       обновление экрана
        pygame.display.update()
        #       формирование координат еды для змейки
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
