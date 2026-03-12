import pygame
import numpy as np

CELL = 60

BG_COLOR       = (20, 20, 30)
GRID_LINE      = (50, 50, 60)
WALL_COLOR     = (80, 80, 95)
DOOR_COLOR     = (139, 90, 43)
OBJECT_COLOR   = (218, 165, 32)
ARTIFACT_COLOR = (255, 215, 0)
EXIT_COLOR     = (0, 200, 100)
GUARD_COLOR    = (30, 100, 255)
INTRUDER_COLOR = (220, 50, 50)


class Viewer:

    def __init__(self, size):
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode((size * CELL, size * CELL))
        pygame.display.set_caption("Cat & Mouse Museum Heist")
        self.font = pygame.font.SysFont("Arial", 13, bold=True)

    def draw(self, env, belief):
        self.screen.fill(BG_COLOR)

        for x in range(self.size):
            for y in range(self.size):
                rect = pygame.Rect(y * CELL, x * CELL, CELL, CELL)
                pos = (x, y)

                if pos in env.walls:
                    pygame.draw.rect(self.screen, WALL_COLOR, rect)
                elif pos in env.doors:
                    pygame.draw.rect(self.screen, DOOR_COLOR, rect)
                    lbl = self.font.render("DOOR", True, (255, 220, 150))
                    self.screen.blit(lbl, (y * CELL + 6, x * CELL + 22))
                else:
                    prob = belief.map[x][y]
                    heat = int(min(255, prob * 4000))
                    pygame.draw.rect(self.screen, (heat, 0, 0), rect)

                pygame.draw.rect(self.screen, GRID_LINE, rect, 1)

        # Exit
        ex, ey = env.exit
        pygame.draw.rect(self.screen, EXIT_COLOR,
                         pygame.Rect(ey * CELL + 4, ex * CELL + 4, CELL - 8, CELL - 8), 3)
        self.screen.blit(self.font.render("EXIT", True, EXIT_COLOR),
                         (ey * CELL + 8, ex * CELL + 22))

        # Museum objects
        for ox, oy in env.objects:
            pygame.draw.rect(self.screen, OBJECT_COLOR,
                             pygame.Rect(oy * CELL + 10, ox * CELL + 10, CELL - 20, CELL - 20))
            self.screen.blit(self.font.render("OBJ", True, (30, 20, 0)),
                             (oy * CELL + 12, ox * CELL + 22))

        # Artifact
        ax, ay = env.artifact
        pygame.draw.rect(self.screen, ARTIFACT_COLOR,
                         pygame.Rect(ay * CELL + 6, ax * CELL + 6, CELL - 12, CELL - 12))
        self.screen.blit(self.font.render("ART", True, (0, 0, 0)),
                         (ay * CELL + 12, ax * CELL + 22))

        # Guard (blue circle)
        gx, gy = env.guard
        pygame.draw.circle(self.screen, GUARD_COLOR,
                           (gy * CELL + CELL // 2, gx * CELL + CELL // 2), CELL // 2 - 4)
        self.screen.blit(self.font.render("G", True, (255, 255, 255)),
                         (gy * CELL + CELL // 2 - 5, gx * CELL + CELL // 2 - 8))

        # Intruder (red circle)
        ix, iy = env.intruder
        pygame.draw.circle(self.screen, INTRUDER_COLOR,
                           (iy * CELL + CELL // 2, ix * CELL + CELL // 2), CELL // 2 - 4)
        self.screen.blit(self.font.render("I", True, (255, 255, 255)),
                         (iy * CELL + CELL // 2 - 4, ix * CELL + CELL // 2 - 8))

        pygame.display.update()