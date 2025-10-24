import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 15
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Player vs AI")
clock = pygame.time.Clock()

# Paddle class
class Paddle:
    def __init__(self, x, y, is_ai=False):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 7
        self.is_ai = is_ai
        self.ai_speed = 5  # AI moves slightly slower for balance
    
    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        
        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    
    def ai_move(self, ball):
        # AI follows the ball with some reaction delay
        paddle_center = self.rect.centery
        ball_center = ball.rect.centery
        
        # Add some imperfection to AI
        if abs(paddle_center - ball_center) > 20:
            if paddle_center < ball_center:
                self.rect.y += self.ai_speed
            else:
                self.rect.y -= self.ai_speed
        
        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
    
    def draw(self, color=WHITE):
        pygame.draw.rect(screen, color, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = 5
        self.speed_y = 5
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
    
    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)
    
    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 5 if random.choice([True, False]) else -5
        self.speed_y = random.randint(-5, 5)
    
    def increase_speed(self):
        # Slightly increase speed after each hit
        if abs(self.speed_x) < 12:
            self.speed_x *= 1.05

# Create game objects
player_paddle = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ai_paddle = Paddle(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, is_ai=True)
ball = Ball()

# Scores
player_score = 0
ai_score = 0
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys
    keys = pygame.key.get_pressed()
    
    # Player paddle controls (W/S or Arrow keys)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_paddle.move(up=True)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_paddle.move(up=False)
    
    # AI paddle movement
    ai_paddle.ai_move(ball)
    
    # Move ball
    ball.move()
    
    # Ball collision with paddles
    if ball.rect.colliderect(player_paddle.rect):
        ball.speed_x = abs(ball.speed_x)  # Always go right
        ball.increase_speed()
        # Add some angle variation based on where ball hits paddle
        hit_pos = (ball.rect.centery - player_paddle.rect.centery) / (PADDLE_HEIGHT / 2)
        ball.speed_y += hit_pos * 2
    
    if ball.rect.colliderect(ai_paddle.rect):
        ball.speed_x = -abs(ball.speed_x)  # Always go left
        ball.increase_speed()
        # Add some angle variation based on where ball hits paddle
        hit_pos = (ball.rect.centery - ai_paddle.rect.centery) / (PADDLE_HEIGHT / 2)
        ball.speed_y += hit_pos * 2
    
    # Ball goes out of bounds
    if ball.rect.left <= 0:
        ai_score += 1
        ball.reset()
    if ball.rect.right >= WIDTH:
        player_score += 1
        ball.reset()
    
    # Drawing
    screen.fill(BLACK)
    
    # Draw center line
    for i in range(0, HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, i, 4, 10))
    
    # Draw game objects
    player_paddle.draw(GREEN)  # Player in green
    ai_paddle.draw(RED)  # AI in red
    ball.draw()
    
    # Draw scores
    player_text = font.render(str(player_score), True, GREEN)
    ai_text = font.render(str(ai_score), True, RED)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(ai_text, (3 * WIDTH // 4 - ai_text.get_width(), 20))
    
    # Draw labels
    player_label = small_font.render("YOU", True, GREEN)
    ai_label = small_font.render("AI", True, RED)
    screen.blit(player_label, (WIDTH // 4 - 20, 100))
    screen.blit(ai_label, (3 * WIDTH // 4 - 20, 100))
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()