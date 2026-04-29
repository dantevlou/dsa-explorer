import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

numbers = [5, 3, 9, 1, 7, 4]
cell_width = WIDTH // len(numbers)

def draw_grid(highlight_index=None):
    screen.fill((30, 30, 30))
    for i, num in enumerate(numbers):
        color = (200, 200, 200)
        if i == highlight_index:
            color = (255, 100, 100)
        rect = pygame.Rect(i * cell_width, 0, cell_width - 2, 100)
        pygame.draw.rect(screen, color, rect)
        text = FONT.render(str(num), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

def linear_search(target):
    comparisons = 0
    for i, num in enumerate(numbers):
        comparisons += 1
        draw_grid(i)
        counter_text = FONT.render(f"Comparisons: {comparisons}", True, (255, 255, 255))
        screen.blit(counter_text, (10, 150))
        pygame.display.flip()
        if num == target:
            return i, comparisons
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(0.5)
    return -1, comparisons

def main():
    input_str = ""
    comparisons = 0
    running = True
    while running:
        draw_grid()
        input_text = FONT.render(f"Enter target: {input_str}", True, (255, 255, 255))
        screen.blit(input_text, (10, 110))
        counter_text = FONT.render(f"Comparisons: {comparisons}", True, (255, 255, 255))
        screen.blit(counter_text, (10, 150))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_str:
                    target = int(input_str)
                    input_str = ""
                    idx, comparisons = linear_search(target)
                    draw_grid(idx if idx != -1 else None)
                    result_text = FONT.render(f"Found at index {idx}" if idx != -1 else "Not found", True, (255, 255, 0))
                    screen.blit(result_text, (10, 110))
                    counter_text = FONT.render(f"Comparisons: {comparisons}", True, (255, 255, 255))
                    screen.blit(counter_text, (10, 150))
                    pygame.display.flip()
                    time.sleep(1.5)
                elif event.key == pygame.K_BACKSPACE:
                    input_str = input_str[:-1]
                elif event.unicode.isdigit():
                    input_str += event.unicode
        clock.tick(30)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()