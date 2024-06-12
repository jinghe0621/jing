
import pygame
import sys
import random

# 初始化pygame模块
pygame.init()

# 设置窗口大小和标题
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇')

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 帧率控制（每秒帧数）
clock = pygame.time.Clock()

# 蛇的初始位置和方向
snake_pos = [(window_width // 4, window_height // 4), (window_width // 2, window_height // 4)]
snake_direction = 'RIGHT'

# 食物随机生成位置（不在蛇身体上）
food_position = (random.randint(0, window_width - 10) // 10 * 10, random.randint(0, window_height - 10) // 10 * 10)

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 键盘事件处理，改变蛇的方向
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # 移动蛇的头部
    head_pos = (snake_pos[0][0], snake_pos[0][1])
    if snake_direction == 'UP':
        head_pos = (head_pos[0], head_pos[1] - 10)
    elif snake_direction == 'DOWN':
        head_pos = (head_pos[0], head_pos[1] + 10)
    elif snake_direction == 'LEFT':
        head_pos = (head_pos[0] - 10, head_pos[1])
    elif snake_direction == 'RIGHT':
        head_pos = (head_pos[0] + 10, head_pos[1])

    # 添加蛇的头部
    snake_pos.insert(0, head_pos)

    # 检查是否吃到食物并生成新的食物位置
    if head_pos == food_position:
        food_position = (
            random.randint(0, window_width - 10) // 10 * 10,
            random.randint(0, window_height - 10) // 10 * 10
        )
    else:
        # 移除蛇的尾巴部分（如果需要）
        snake_pos.pop()

    # 清屏并绘制游戏对象
    screen.fill(black)

    for pos in snake_pos:
        pygame.draw.rect(screen, white, (pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, red, (food_position[0], food_position[1], 10, 10))

    # 更新显示和帧率
    pygame.display.flip()
    clock.tick(25)  # 调整蛇的速度，5是FPS（Frames Per Second）