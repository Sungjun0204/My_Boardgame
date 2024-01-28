import pygame
import sys

# Pygame 초기화
pygame.init()

# 창 설정
WINDOW_WIDTH, WINDOW_HEIGHT = 400, 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 보드 설정
BOARD_WIDTH, BOARD_HEIGHT = 1000, 1000
GRID_SIZE = 5
board = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))

# 말 이미지 불러오기
piece_image = pygame.image.load('Boardgames/pieces/170923-07-01-1-A.jpg')

# 게임 루프
running = True
camera_x, camera_y = 0, 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 말 클릭 이벤트 및 메뉴 구현
        # ...

    # 마우스 위치에 따른 카메라 이동 구현
    # ...

    # 보드와 말 그리기
    window.fill((255, 255, 255))  # 흰색 배경
    window.blit(board, (-camera_x, -camera_y))
    #window.blit(piece_image, (piece_x - camera_x, piece_y - camera_y))

    pygame.display.update()

pygame.quit()