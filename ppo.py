"""
Train an agent using Proximal Policy Optimization from OpenAI Baselines
"""

import argparse
import os

import retro
from baselines.bench import Monitor
from baselines.common.vec_env import SubprocVecEnv
from baselines.common.retro_wrappers import make_retro, wrap_deepmind_retro
from baselines.ppo2 import ppo2

os.environ['OPENAI_LOGDIR'] = '/home/dhodwo/PycharmProjects/untitled/check_pts'
# os.environ['OPENAI_LOG_FORMAT'] = 'stdout,log, csv, tensorboard'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--game', default='Airstriker-Genesis')
    parser.add_argument('--state', default=retro.State.DEFAULT)
    parser.add_argument('--scenario', default=None)
    args = parser.parse_args()

    def make_env():
        #if I wanna record the game video, then add attribute "record = '.'"
        env = make_retro(game=args.game, state=args.state, scenario=args.scenario, record = '.')
        env = wrap_deepmind_retro(env)
        env = Monitor(env, None, True)
        # And activate all of the under codes
        env.reset()
        while True:
            _obs, _rew, done, _info = env.step(env.action_space.sample())
            if done:
                break

        return env
    
    venv = SubprocVecEnv([make_env] * 8)
    ppo2.learn(
        network='cnn', 
        env=venv, 
        total_timesteps=int(100e6),
        nsteps=128,
        nminibatches=4,
        lam=0.95, 
        gamma=0.99, 
        noptepochs=4, 
        log_interval=1,
        ent_coef=.01,
        lr=lambda f : f * 2.5e-4,
        cliprange=0.1,
        load_path='/home/dhodwo/PycharmProjects/untitled/check_pts/checkpoints/1'
    )


if __name__ == '__main__':
    main()
