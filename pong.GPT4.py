import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PINK = (255, 105, 180)
WHITE = (255, 255, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 3
WIN_SCORE = 3

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Create the paddles and the ball
player_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball speed and direction
ball_speed_x = BALL_SPEED * random.choice([-1, 1])
ball_speed_y = BALL_SPEED * random.choice([-1, 1])

# Score variables
player_score = 0
computer_score = 0

# Load the font for displaying the score
font = pygame.font.Font(None, 36)

def move_player_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

def move_computer_paddle():
    if computer_paddle.centery < ball.centery and computer_paddle.bottom < HEIGHT:
        computer_paddle.y += PADDLE_SPEED
    if computer_paddle.centery > ball.centery and computer_paddle.top > 0:
        computer_paddle.y -= PADDLE_SPEED

def move_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

def check_collisions():
    global ball_speed_x, ball_speed_y, player_score, computer_score

    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x = -ball_speed_x

    if ball.left <= 0:
        player_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        computer_score += 1
        reset_ball()

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x = BALL_SPEED * random.choice([-1, 1])
    ball_speed_y = BALL_SPEED * random.choice([-1, 1])

def draw_objects():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, PINK, player_paddle)
    pygame.draw.rect(screen, PINK, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    player_text = font.render(str(player_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 2 - 50, 10))

    computer_text = font.render(str(computer_score), True, WHITE)
    screen.blit(computer_text, (WIDTH // 2 + 20, 10))

def check_game_over():
    global player_score,    computer_score

    if player_score >= WIN_SCORE or computer_score >= WIN_SCORE:
        reset_game()

def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0
    reset_ball()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move_player_paddle()
    move_computer_paddle()
    move_ball()
    check_collisions()
    check_game_over()
    draw_objects()

    pygame.display.flip()
    pygame.time.Clock().tick(60)


