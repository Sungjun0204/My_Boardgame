import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
width, height = 400, 400
screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Zoomable and Movable Grid Game")

# 격자 설정
grid_size = 8
cell_size = width // grid_size
zoom_factor = 1.0
offset_x, offset_y = 0, 0
dragging = False
last_mouse_pos = None

# 색깔 정의
grid_color = (0, 0, 0)

# 캐릭터 말 이동 값 변수
mv_x = 0
mv_y = 0


# 이미지 불러오기
new_width = 50; new_height = 50
image = pygame.image.load('Boardgames/pieces/170923-07-01-1-A.jpg')
image = pygame.transform.scale(image, (new_width, new_height))      # 이미지 크기조절
image_rect = image.get_rect()
# image_rect.center = (175+mv_x, 175+mv_y)              # 이미지의 중심점 설정



# 줄바꿈된 텍스트 생성
text_lines = [
    "[명령]",
    "1. 위로 이동",
    "2. 아래로 이동"
]
# 줄바꿈된 텍스트 렌더링
menu_font = pygame.font.SysFont("Dotum", 15)
rendered_text = []
for line_number, line in enumerate(text_lines):
    rendered_text.append(menu_font.render(line, True, (0, 0, 0)))   # 폰트 색상임
    text_rect = rendered_text[line_number].get_rect(topleft=(10, 20 + line_number * 30)) # 줄간격임
running = True
show_menu = False


# 직사각형 설정
rect_x = 20
rect_y = 50
rect_width = 100
rect_height = 20
rect_color = (255, 255, 255, 0)  #  투명한 검은색
rect_draw = False
# 투명한 사각형을 그릴 Surface 생성
transparent_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
transparent_surface.fill(rect_color)






# 게임 루프
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # 마우스 클릭 좌표 가져오기

            # 이미지에 마우스 왼쪽 버튼 클릭 시
            if (show_menu == False) and image_rect.collidepoint(event.pos):
                show_menu = True
                rect_draw = True
             # 메뉴 열린 상태에서 다른 곳 누르면
            elif (show_menu == True) and image_rect.collidepoint(event.pos):   
                show_menu = False
                rect_draw = False
           
            if (show_menu == True) and (rect_x < mouse_x < rect_x + rect_width) and (rect_y < mouse_y < rect_y + rect_height):      # 클릭한 좌표가 직사각형 내부에 있는지 확인
                print("직사각형을 클릭했습니다.")
                show_menu = False
                rect_draw = False
                mv_x += 50
        

    # 화면 색상 설정
    screen.fill((255, 255, 255, 0))

    # 가로선 그리기
    for row in range(grid_size + 1):
        pygame.draw.line(screen, grid_color,
                         (0 - offset_x, (row * cell_size * zoom_factor) - offset_y),
                         (width * zoom_factor - offset_x, (row * cell_size * zoom_factor) - offset_y), 1)

    # 세로선 그리기
    for col in range(grid_size + 1):
        pygame.draw.line(screen, grid_color,
                         ((col * cell_size * zoom_factor) - offset_x, 0 - offset_y),
                         ((col * cell_size * zoom_factor) - offset_x, height * zoom_factor - offset_y), 1)
        


    # 크기 조절된 이미지 화면에 그리기
    screen.blit(image, (width//2-new_width+mv_x, height//2-new_height+mv_y)) # 재조정된 사이즈와 생성 위치 설정
    image_rect.center = (175+mv_x, 175+mv_y)              # 이미지의 중심점 설정

    # 메뉴 화면 표시
    if show_menu:
        for line_number, rendered_line in enumerate(rendered_text):
            screen.blit(rendered_line, (20, 20 + line_number * 30))


    if rect_draw:
        # 직사각형 그리기
        #pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
        screen.blit(transparent_surface, (rect_x, rect_y))




    # 화면 업데이트
    pygame.display.flip()
