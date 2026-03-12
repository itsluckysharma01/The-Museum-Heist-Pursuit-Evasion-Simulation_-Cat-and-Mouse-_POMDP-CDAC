import pygame
from env.grid_world import GridWorld
from env.sensors import MotionSensor
from pomdp.belief_update import Belief
from visualization.viewer import Viewer

env = GridWorld()
sensor = MotionSensor()
belief = Belief(env.size)
viewer = Viewer(env.size)

env.reset()
clock = pygame.time.Clock()

print("Guard  -> Arrow Keys")
print("Intruder -> W A S D")

running = True
while running:
    guard_action = None
    intruder_action = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Guard: Arrow keys
            if event.key == pygame.K_UP:
                guard_action = "UP"
            elif event.key == pygame.K_DOWN:
                guard_action = "DOWN"
            elif event.key == pygame.K_LEFT:
                guard_action = "LEFT"
            elif event.key == pygame.K_RIGHT:
                guard_action = "RIGHT"

            # Intruder: WASD
            elif event.key == pygame.K_w:
                intruder_action = "UP"
            elif event.key == pygame.K_s:
                intruder_action = "DOWN"
            elif event.key == pygame.K_a:
                intruder_action = "LEFT"
            elif event.key == pygame.K_d:
                intruder_action = "RIGHT"

            elif event.key == pygame.K_ESCAPE:
                running = False

    if guard_action:
        env.guard = env.move(env.guard, guard_action)

    if intruder_action:
        env.intruder = env.move(env.intruder, intruder_action)

    if guard_action or intruder_action:
        observation = sensor.detect(env.guard, env.intruder)
        belief.update(observation)

    viewer.draw(env, belief)

    if env.guard == env.intruder:
        print("Guard caught the intruder!")
        running = False

    clock.tick(60)

pygame.quit()