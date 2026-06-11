import pygame as pg
import random
from shapes_data import *

class Block:
    def __init__(self, shape, color, container_x, container_y, container_size):
        self.shape = shape
        self.color = color
        self.container_x = container_x
        self.container_y = container_y
        self.container_size = container_size
        
        dxs = [dx for dx, dy in self.shape]
        dys = [dy for dx, dy in self.shape]
        self.width_cells = max(dxs) - min(dxs) + 1
        self.height_cells = max(dys) - min(dys) + 1
        self.min_dx = min(dxs)
        self.min_dy = min(dys)

        self.is_dragging = False
        self.current_cell_size = CELL_SIZE * PREVIEW_SCALE
        self.reset_to_tray()

    def reset_to_tray(self):
        self.is_dragging = False
        self.current_cell_size = CELL_SIZE * PREVIEW_SCALE
        block_w_px = self.width_cells * self.current_cell_size
        block_h_px = self.height_cells * self.current_cell_size
        self.x = self.container_x + (self.container_size[0] - block_w_px) / 2 - self.min_dx * self.current_cell_size
        self.y = self.container_y + (self.container_size[1] - block_h_px) / 2 - self.min_dy * self.current_cell_size
        self.update_rects()

    def update_rects(self):
        self.rects = []
        for dx, dy in self.shape:
            rect = pg.Rect(self.x + dx * self.current_cell_size, 
                           self.y + dy * self.current_cell_size, 
                           self.current_cell_size - 1, self.current_cell_size - 1)
            self.rects.append(rect)

    def draw(self, screen):
        for rect in self.rects:
            pg.draw.rect(screen, self.color, rect, border_radius=4)

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Bờ lóc bờ lát (Block Blast)")
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont("Arial", 30, bold=True)
        self.reset_game()

    def reset_game(self):
        self.grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.score = 0
        self.game_over = False
        self.selected_block = None
        self.spawn_blocks()

    def spawn_blocks(self):
        self.available_blocks = []
        c_width = SCREEN_WIDTH // 3
        for i in range(3):
            shape = random.choice(SHAPES)
            color = random.choice(SHAPE_COLORS)
            self.available_blocks.append(Block(shape, color, i * c_width, SCREEN_HEIGHT - 200, (c_width, 150)))
        self.check_game_over()

    def can_place_block(self, block):
        """Kiểm tra khối có thể đặt vào bất kỳ đâu trên lưới không"""
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                can_fit = True
                for dx, dy in block.shape:
                    nr, nc = r + dy, c + dx
                    if not (0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE) or self.grid[nr][nc]:
                        can_fit = False
                        break
                if can_fit: return True
        return False

    def check_game_over(self):
        if not self.available_blocks: return
        # Nếu không có khối nào đặt được nữa -> Thua
        if not any(self.can_place_block(b) for b in self.available_blocks):
            self.game_over = True

    def draw_grid(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                rect = pg.Rect(GRID_X_MARGIN + c * CELL_SIZE, GRID_TOP_MARGIN + r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pg.draw.rect(self.screen, COLOR_GRID, rect, 1)
                if self.grid[r][c]:
                    pg.draw.rect(self.screen, self.grid[r][c], rect.inflate(-2, -2), border_radius=5)

    def check_lines(self):
        rows = [r for r in range(GRID_SIZE) if all(self.grid[r][c] is not None for c in range(GRID_SIZE))]
        cols = [c for c in range(GRID_SIZE) if all(self.grid[r][c] is not None for r in range(GRID_SIZE))]
        for r in rows:
            for c in range(GRID_SIZE): self.grid[r][c] = None
            self.score += 100
        for c in cols:
            for r in range(GRID_SIZE): self.grid[r][c] = None
            self.score += 100

    def run(self):
        while True:
            self.screen.fill(COLOR_BG)
            mx, my = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT: pg.quit(); return

                if self.game_over:
                    if event.type == pg.KEYDOWN and event.key == pg.K_r: self.reset_game()
                else:
                    if event.type == pg.MOUSEBUTTONDOWN:
                        for b in self.available_blocks:
                            if any(r.collidepoint((mx, my)) for r in b.rects):
                                self.selected_block = b
                                b.is_dragging = True
                                b.current_cell_size = CELL_SIZE
                                break

                    if event.type == pg.MOUSEMOTION and self.selected_block:
                        self.selected_block.x = mx - (self.selected_block.width_cells * CELL_SIZE) / 2
                        self.selected_block.y = my - (self.selected_block.height_cells * CELL_SIZE) / 2
                        self.selected_block.update_rects()

                    if event.type == pg.MOUSEBUTTONUP and self.selected_block:
                        grid_c = round((self.selected_block.x - GRID_X_MARGIN) / CELL_SIZE)
                        grid_r = round((self.selected_block.y - GRID_TOP_MARGIN) / CELL_SIZE)

                        valid = True
                        for dx, dy in self.selected_block.shape:
                            nr, nc = grid_r + dy, grid_c + dx
                            if not (0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE) or self.grid[nr][nc]:
                                valid = False; break
                        
                        if valid:
                            for dx, dy in self.selected_block.shape:
                                self.grid[grid_r + dy][grid_c + dx] = self.selected_block.color
                            self.score += len(self.selected_block.shape) * 10
                            self.available_blocks.remove(self.selected_block)
                            self.check_lines()
                            if not self.available_blocks: self.spawn_blocks()
                            else:
                                self.check_game_over() # Check game over mỗi khi đặt 1 khối
                        else:
                            self.selected_block.reset_to_tray()
                        self.selected_block = None

            self.draw_grid()
            for b in self.available_blocks: b.draw(self.screen)
            self.screen.blit(self.font.render(f"Score: {self.score}", True, COLOR_TEXT), (20, 10))

            if self.game_over:
                overlay = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pg.SRCALPHA)
                overlay.fill((0, 0, 0, 180)) 
                self.screen.blit(overlay, (0, 0))
                msg = self.font.render("GAME OVER!", True, (255, 255, 255))
                sub = self.font.render("Press 'R' to Restart", True, (200, 200, 200))
                self.screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, SCREEN_HEIGHT//2 - 40))
                self.screen.blit(sub, (SCREEN_WIDTH//2 - sub.get_width()//2, SCREEN_HEIGHT//2 + 20))

            pg.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()