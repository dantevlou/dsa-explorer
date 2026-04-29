import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

queue = []

BLOCK_WIDTH, BLOCK_HEIGHT = 60, 40
START_X = 20
BASE_Y = (HEIGHT - BLOCK_HEIGHT) // 2

ENQUEUE_BTN = pygame.Rect(20, 140, 120, 40)
DEQUEUE_BTN = pygame.Rect(160, 140, 120, 40)


def draw_queue(offset=0):
    screen.fill((50, 50, 50))
    for i, val in enumerate(queue):
        rect = pygame.Rect(START_X + i * (BLOCK_WIDTH + 5) - offset, BASE_Y, BLOCK_WIDTH, BLOCK_HEIGHT)
        pygame.draw.rect(screen, (100, 150, 250), rect)
        text = FONT.render(str(val), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
    pygame.draw.rect(screen, (100, 200, 100), ENQUEUE_BTN)
    pygame.draw.rect(screen, (200, 100, 100), DEQUEUE_BTN)
    screen.blit(FONT.render("Enqueue", True, (0, 0, 0)), (ENQUEUE_BTN.x + 10, ENQUEUE_BTN.y + 10))
    screen.blit(FONT.render("Dequeue", True, (0, 0, 0)), (DEQUEUE_BTN.x + 10, DEQUEUE_BTN.y + 10))


def animate_enqueue(val):
    target_x = START_X + len(queue) * (BLOCK_WIDTH + 5)
    current_x = WIDTH
    while current_x > target_x:
        current_x = max(current_x - 25, target_x)
        draw_queue()
        rect = pygame.Rect(current_x, BASE_Y, BLOCK_WIDTH, BLOCK_HEIGHT)
        pygame.draw.rect(screen, (100, 150, 250), rect)
        text = FONT.render(str(val), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
    queue.append(val)


def animate_dequeue():
    offset = 0
    while offset < BLOCK_WIDTH + 5:
        offset += 20
        draw_queue(offset)
        pygame.display.flip()
        clock.tick(60)
    queue.pop(0)


def main():
    counter = 1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if ENQUEUE_BTN.collidepoint(pos):
                    animate_enqueue(counter)
                    counter += 1
                elif DEQUEUE_BTN.collidepoint(pos) and queue:
                    animate_dequeue()

        draw_queue()
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()