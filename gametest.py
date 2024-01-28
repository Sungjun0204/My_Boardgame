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
    "1. 앞으로 이동",
    "2. 뒤로 이동"
]
# 줄바꿈된 텍스트 렌더링
menu_font = pygame.font.SysFont("Dotum", 15)
rendered_text = []
for line_number, line in enumerate(text_lines):
    rendered_text.append(menu_font.render(line, True, (0, 0, 0)))   # 폰트 색상임
    text_rect = rendered_text[line_number].get_rect(topleft=(10, 20 + line_number * 30)) # 줄간격임
running = True
show_menu = False


# 버튼을 위한 직사각형 설정
rect_x = 20
rect_y = 50
rect_width = 100
rect_height = 20
rect_color = (0, 0, 0, 0)  #  메뉴 버튼 색상(투명한 검은색)
menu_bg_color = (255, 255, 153, 255) # 메뉴창 배경 색상
choose_piece_color = (255, 0, 0, 255) # 말 선택 효과 사각형 색상

menu_1_on = False           # 메뉴 항목 1 버튼 생성 여부
menu_2_on = False           # 메뉴 항목 2 버튼 생성 여부
menu_bg_on = False          # 메뉴창 생성 여부

# 말 클릭했을 때의 효과를 표현하는 사각형을 그릴 Surface 생성
choose_piece = pygame.Surface((56, 56), pygame.SRCALPHA)
choose_piece.fill(choose_piece_color)
# 메뉴창 배경 사각형을 그릴 Surface 생성
menu_bg = pygame.Surface((100, 100), pygame.SRCALPHA)
menu_bg.fill(menu_bg_color)
# [1. 앞으로 이동] 버튼 사각형을 그릴 Surface 생성
menu_1 = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
menu_1.fill(rect_color)
# [2. 뒤로 이동] 버튼 사각형을 그릴 Surface 생성
menu_2 = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
menu_2.fill(rect_color)






# 게임 루프
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:        # 마우스 클릭 이벤트 처리
            mouse_x, mouse_y = pygame.mouse.get_pos()  # 마우스 클릭 좌표 가져오기

            # 이미지에 마우스 왼쪽 버튼 클릭 시
            if (show_menu == False) and image_rect.collidepoint(event.pos):
                show_menu = True    # 메뉴 텍스트 띄움
                menu_1_on=True; menu_2_on=True    # 메뉴 버튼 띄움
             # 그러나 메뉴 열린 상태에서 이미지를 누르면
            elif (show_menu == True) and image_rect.collidepoint(event.pos):   
                show_menu = False   # 메뉴 텍스트 다시 닫음
                menu_1_on=False; menu_2_on=False   # 메뉴 버튼도 없어짐
           
            # 1. 앞으로 이동 메뉴를 눌렀을 때
            if (show_menu == True) and (rect_x < mouse_x < rect_x + rect_width) and (rect_y < mouse_y < rect_y + rect_height):      # 클릭한 좌표가 직사각형 내부에 있는지 확인
                print("앞으로 한 칸 이동.")   # 콘솔창 출력
                show_menu = False   # 메뉴창이 닫힘
                menu_1_on=False; menu_2_on=False   # 메뉴 버튼 닫힘
                mv_x += 50          # 말의 중심점과 생성위치를 grid 1칸만큼 +X축으로 이동

            # 2. 뒤로 이동 메뉴를 눌렀을 때
            if (show_menu == True) and (rect_x < mouse_x < rect_x + rect_width) and (rect_y+28 < mouse_y < rect_y+28 + rect_height):      # 클릭한 좌표가 직사각형 내부에 있는지 확인
                print("뒤로 한 칸 이동.")   # 콘솔창 출력
                show_menu = False   # 메뉴창이 닫힘
                menu_1_on=False; menu_2_on=False   # 메뉴 버튼 닫힘
                mv_x -= 50          # 말의 중심점과 생성위치를 grid 1칸만큼 -X축으로 이동
        

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
        


    # 메뉴 화면을 화면에 출력
    if show_menu:
        # 텍스트를 한 줄씩 줄바꿈하여 출력
        screen.blit(menu_bg, (rect_x, rect_y-30))
        for line_number, rendered_line in enumerate(rendered_text):
            screen.blit(rendered_line, (20, 20 + line_number * 30))
        screen.blit(choose_piece, (147+mv_x, 147+mv_y))

    # 크기 조절된 이미지 화면에 그리기
    screen.blit(image, (width//2-new_width+mv_x, height//2-new_height+mv_y)) # 재조정된 사이즈와 생성 위치 설정
    image_rect.center = (175+mv_x, 175+mv_y)              # 이미지의 중심점 설정

    # [1. 앞으로 이동]을 위한 사각 버튼을 화면에 출력
    if menu_1_on: screen.blit(menu_1, (rect_x, rect_y))
    if menu_2_on: screen.blit(menu_2, (rect_x, rect_y+28))
    



    # 화면 업데이트
    pygame.display.flip()
