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
        self.current_step_num = 0
        self.max_step_num = 1000

        self.damage_reward = -10
        self.treasure_reward = 100
        self.penalty = -0.1

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0,high=4,shape=map.shape,dtype=np.float32)

        self.shuffle_flag = False
        self.seed()
        self.viewr = None
        self.state = (0,0,0) #x,y,zの座標の点を表す(二次元なら最後は使わない)
        
        self.step_beyond_done = None


    def seed(self,seed=None):
        pass
    
    def step(self,action):
        assert self.action_space.contains(action),"%r (%s) invalid"(action,type(action))

        state = self.state
        self.current_step_num += self.current_step_num + 1 
        
        state,reward,done = process_env(self,action)
        
        
        if done:
            reward += reward + self.treasure_reward
        else:
            reward += self.penalty
        
        return state,reward,done,{}

    def process_env(self,action):
