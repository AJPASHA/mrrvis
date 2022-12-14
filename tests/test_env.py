
import numpy as np
from mrrvis.configuration import ConfigurationGraph
from mrrvis.movesets import squaremoves
from mrrvis.env import Environment

from collections import deque

state_0 = ConfigurationGraph('Square', np.array([[1,2],[2,2],[2,3],[3,3],[3,2],[3,1]]))
state_target = ConfigurationGraph('Square', np.array([[2,1],[2,2],[2,3],[3,3],[3,2],[3,1]]))
def test_init():
    env = Environment(state_0, 'Square', state_target)
    assert state_0 == env.state
    assert state_target == env.target_state
    assert env.moveset == {'slide': squaremoves.slide, 'rotate': squaremoves.rotate, 'push': squaremoves.slide_line}

    assert env.history[0] == state_0

def test_step():
    
    env = Environment(state_0, 'Square', state_target)
    next_state, reward, done = env.step('slide', [1,2], 'N')

    assert next_state == ConfigurationGraph('Square', np.array([[1,3],[2,2],[2,3],[3,3],[3,2],[3,1]]))
    assert reward == -1
    assert not done
    next_state,_,_ = env.step('slide', 0, 'S')
    assert next_state == ConfigurationGraph('Square', np.array([[1,2],[2,2],[2,3],[3,3],[3,2],[3,1]]))
    next_state,_,done = env.step('rotate', 0, 'SE')

    assert done

    assert len(env.history.history) == 4

def test_history():
    env = Environment(state_0, 'Square', state_target)
    env.step('slide', [1,2], 'N')
    env.step('slide', 0, 'S')
    env.step('rotate', 0, 'SE')

    
    assert env.history[1] == ConfigurationGraph('Square', np.array([[1,3],[2,2],[2,3],[3,3],[3,2],[3,1]]))
    assert env.history[2] == ConfigurationGraph('Square', np.array([[1,2],[2,2],[2,3],[3,3],[3,2],[3,1]]))
    assert env.history[3] == ConfigurationGraph('Square', np.array([[2,1],[2,2],[2,3],[3,3],[3,2],[3,1]]))

def test_reset():
    pass

def test_revert():
    pass

