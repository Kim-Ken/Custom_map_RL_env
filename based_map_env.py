import gym
from gym import spaces,logger
from gym import seeding
import numpy as np 

class MySanmokuEnv(gym.Env):
    
    meta_data={
        'render.modes':['human','rgb_array']
    }

    def __init__(self):
        self.status = None

        self.x_limit = 500
        self.y_limit = 600
        self.map_type_nums = 4
        self.map = np.zeros(x_limit,y_limit)

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0,high=4,shape=map.shape,dtype=np.float32)

        self.shuffle_flag = False
        self.seed()
        self.viewr = None
        self.state = None
        

        self.step_beyond_done = None


    def seed(self,seed=None):
        pass
    

    