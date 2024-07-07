import pygame

### Khởi tạo các module cần thiết của Pygame bằng hàm init.
pygame.init()


#### Ví dụ: Sử dụng pygame để vẽ một hình chữ nhật đơn giản.

### Tạo một cửa sổ có kích thước: 800x600
screen = pygame.display.set_mode((800, 600))

### Đặt tên cho cửa sổ
pygame.display.set_caption("Vẽ hình chữ nhật với Pygame")

### Định nghĩa màu sắc (R,G,B)
white = (255, 255, 255)
red = (255, 0, 0)

### Vẽ một hình chữ nhật đỏ 
rect = pygame.Rect(200, 200, 200, 150)
pygame.draw.rect(screen, red, rect )

### Cập nhật màn hình để hiển thị hình chữ nhật
pygame.display.flip()


### Đợi người dùng thoát ra khỏi cửa sổ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

### Thoát pygame
pygame.quit()