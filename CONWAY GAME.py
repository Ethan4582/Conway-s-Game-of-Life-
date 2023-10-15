import pygame
import random

pygame.init()

# Basic Variables
black = (0, 0, 0)
grey = (128, 128, 128)
yellow = (225, 255, 0)

WIDTH, HEIGHT = 800, 800
tile_size = 25

grid_width = WIDTH // tile_size
grid_height = HEIGHT // tile_size
fps = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, grid_width), random.randrange(0, grid_height)) for _ in range(num)])

# Drawing the Table
def draw_grid(positions):
    for position in positions:
        colm, row = position
        top_left = (colm * tile_size, row * tile_size)
        pygame.draw.rect(screen, yellow, (*top_left, tile_size, tile_size))

    for row in range(grid_height):
        pygame.draw.line(screen, black, (0, row * tile_size), (WIDTH, row * tile_size))

    for colm in range(grid_width):
        pygame.draw.line(screen, black, (colm * tile_size, 0), (colm * tile_size, HEIGHT))

def adjust_grid(positions):
    all_neighbour = set()
    new_position = set()

    for position in positions:
        neighbour = get_neighbour(position)
        all_neighbour.update(neighbour)

        neighbour = list(filter(lambda x: x in positions, neighbour))

        if len(neighbour) in [2, 3]:
            new_position.add(position)

    for position in all_neighbour:
        neighbour = get_neighbour(position)
        neighbour = list(filter(lambda x: x in positions, neighbour))

        if len(neighbour) == 3:
            new_position.add(position)

    return new_position

def get_neighbour(pos):
    x, y = pos
    neighbour = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx >= grid_width:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy >= grid_height:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbour.append((x + dx, y + dy))

    return neighbour

def main():
    running = True
    playing = False
    count = 0
    update_frequency = 120

    positions = set()

    while running:
        clock.tick(fps)

        if playing:
            count += 1

        if count >= update_frequency:
            count = 0
            if playing:
                positions = adjust_grid(positions)

        caption = "PLAYING" if playing else "PAUSED"
        pygame.display.set_caption(caption)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Adding Cells
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                colm = x // tile_size
                row = y // tile_size
                pos = (colm, row)

                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            # Handling Other Keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(4, 10) * grid_width)

        screen.fill(grey)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
