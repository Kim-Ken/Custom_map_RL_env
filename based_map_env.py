import Custom_map_RL_env
import gym
from gym import spaces,logger
from gym import seeding
import numpy as np 

from enum import IntEnum


class Action(IntEnum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3

class Map_Property(IntEnum):
    Normal = 0
    Damege = 1
    Treasure = 2
    Wall = 3
    Seeker = 4


class MySanmokuEnv(gym.Env):
    
    meta_data={
        'render.modes':['human','rgb_array']
    }

    def __init__(self):
        self.status = None

        self.x_limit = 8
        self.y_limit = 12
        self.map_type_nums = 4
        self.map = np.zeros(x_limit,y_limit)
        self.current_step_num = 0
        self.max_step_num = 1000
        self.one_step_size = 1
        self.map_floor_info = self.generate_map()

        self.damage_reward = -1
        self.treasure_reward = 1
        self.penalty = -0.1

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0,high=map_type_nums,shape=map.shape,dtype=np.float32)

        self.shuffle_flag = False
        self.seed()
        self.viewr = None

        self.pos_x = 0  #xの座標の点を表す
        self.pos_y = 0  
        self.pos_z = 0  #z座標の点を表す(二次元なら使わない)
        
        self.step_beyond_done = None


    def seed(self,seed=None):
        pass
    
    def step(self,action):
        assert self.action_space.contains(action),"%r (%s) invalid"(action,type(action))

        state = None
        self.current_step_num += self.current_step_num + 1 
        
        observation,reward,done = process_env(self,action)
        
        return observation,reward,done,{}
    
    def reset(self):
        self.pos_x,self.pos_y = 0,0
        self.reward = 0
        return insert_obs()

    def insert_obs(self):
        obs = np.deepcopy(self.map_info):
        obs[self.pos_x,self.pos_y] = Map_Property.Seeker
        return obs

    def process_env(self,action):
        
        move_dist_x = 0
        move_dist_y = 0
        this_time_reward = 0
        done = False

        #位置の調整
        if Color(action) == Color.UP:
            move_dist_y = self.one_step_size

        elif Color(action) == Color.LEFT:
            move_dist_x = self.one_step_size

        elif Color(action) == Color.DOWN:
            move_dist_y = -self.one_step_size

        elif Color(action) == Color.LEFT:
            move_dist_y = -self.one_step_size
        
        if map_info(self.pos_x,self.pos_y) != Map_Property.Wall.value:
            if 0 <= move_dist_x + self.pos_x < self.x_limit:
                self.pos_x += move_dist_x
        
            if 0 <= move_dist_y + self.pos_y < self.y_limit:
                self.pos_y += move_dist_y
        
        #アイテム取得の処理
        if map_info(self.pos_x,self.pos_y) == Map_Property.Damege.value:
            this_time_reward += self.damage_reward
        
        elif map_info(self.pos_x,self.pos_y) == Map_Property.Treasure.value:
            this_time_reward += self.treasure_reward
            done = True 
        
        else:
            this_time_reward += self.penalty

        return insert_obs(),reward,done
            
    #mapの床情報を(x_limit,y_limit,z_limit)サイズのarrayで返す
    def generate_map(self,mode='default'):
        map_info = np.zeros((self.x_limit,self.y_limit))

        map_info(1,3) = Map_Property.Damege.value
        map_info(1,8) = Map_Property.Damege.value
        map_info(3,5) = Map_Property.Damege.value
        map_info(4,2) = Map_Property.Damege.value
        map_info(4,10)= Map_Property.Damege.value
        map_info(5,4) = Map_Property.Damege.value
        map_info(5,7) = Map_Property.Damege.value

        map_info(5,9) = Map_Property.Treasure.value

        return map_info 
        
    
if __name__ = '__main__':
    import gym
    env