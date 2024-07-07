import pygame
import sys

## Khởi tạo pygame
pygame.init()

## Kích thước màn hình:
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

## Đặt tên cửa sổ
pygame.display.set_caption("Pong Game")

## Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)

## Thanh điều khiển (paddle)
paddle_width = 15
paddle_height = 100
paddle_speed = 7

## Vị trí của thanh điều khiển hiển thị lúc ban đầu
player1_x = 50
player1_y = screen_height // 2 - paddle_height // 2
player2_x = screen_width - 50 - paddle_width
player2_y = screen_height // 2 - paddle_height // 2

## Ball
ball_size = 20
ball_x = screen_width // 2 - ball_size // 2 ## chia 2 lấy phần nguyên
ball_y = screen_height // 2 - ball_size // 2 ## chia 2 lấy phần nguyên
ball_speed_x = 4
ball_speed_y = 4

## Score
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 74)

### Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    ## Get keys pressed
    keys = pygame.key.get_pressed()

    ### Move player 1
    if keys[pygame.K_w] and player1_y >0:
        player1_y -= paddle_speed ## mỗi lần ấn thì trừ đi 7 đơn vị
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed ## mỗi lần ấn thì trừ đi 7 đơn vị

    ### Move player 2
    if keys[pygame.K_UP] and player2_y >0:
        player2_y -= paddle_speed ## mỗi lần ấn thì trừ đi 7 đơn vị
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed ## mỗi lần ấn thì trừ đi 7 đơn vị

    ## Move Ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    ## Ball collision with top and bottom
    if ball_y <=0  or ball_y >= screen_height - ball_size:
        ball_speed_y *= -1 ## ball_speed_y = ball_speed_y * (-1)
    
    ## Ball collision with paddles (thanh player)
    if (ball_x <= player1_x + paddle_width and player1_y <= ball_y <= player1_y + paddle_height) or (ball_x >= player2_x - ball_size and player2_y <= ball_y <= player2_y + paddle_height):
        ball_speed_y *= -1 ## ball_speed_y = ball_speed_y * (-1)

    #### Ball goes out of bounds

    ### fill screen
    screen.fill(black)


    ### Draww




