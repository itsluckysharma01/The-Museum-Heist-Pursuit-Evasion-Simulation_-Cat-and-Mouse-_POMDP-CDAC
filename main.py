from env.grid_world import GridWorld
from env.sensors import MotionSensor
from pomdp.belief_update import BeliefState
from agents.guard_agent import GuardAgent
from agents.intruder_agent import IntruderAgent

env = GridWorld()

sensor = MotionSensor()

belief = BeliefState(env.size)

guard = GuardAgent(belief)

intruder = IntruderAgent()

state = env.reset()

for step in range(100):

    guard_action = guard.choose_action()
    intruder_action = intruder.choose_action()

    env.guard_pos = env.move(env.guard_pos, guard_action)
    env.intruder_pos = env.move(env.intruder_pos, intruder_action)

    observation = sensor.detect(env.guard_pos, env.intruder_pos)

    belief.update(observation)

    print("Step:", step)
    print("Guard:", env.guard_pos)
    print("Observation:", observation)

    if env.guard_pos == env.intruder_pos:
        print("Guard caught intruder!")
        break