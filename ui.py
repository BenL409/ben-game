import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def draw_game_over(screen):
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, "white")
    sub_text = font.render("Press any key to Restart", True, "gray")
    
    # Center the text
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(sub_text, (SCREEN_WIDTH // 2 - sub_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))