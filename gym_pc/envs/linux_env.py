import sys
import time

import docker
import gym
import requests
from PIL import Image
from vncdotool import api


class LinuxEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.docker_client = docker.from_env()
        try:
            self.container = self.docker_client.containers.run(
                "breandan/ubuntuvnc",
                ports={'8000/tcp': 8000, '6080/tcp': 80, '5900/tcp': 5900},
                remove=True,
                detach=True)
        except:
            pass  # Ignore error if container is already running
        self.vnc_client = api.connect('127.0.0.1', password=None)

    def step(self, action):
        """
        Parameters
        ----------
        action : string representing the action to take.

        Returns
        -------
        ob, reward, episode_over, info : tuple
            ob (object) :
                a screen image
            reward (float) :
                amount of reward achieved by the previous action. The scale
                varies between environments, but the goal is always to increase
                your total reward.
            episode_over (bool) :
                whether it's time to reset the environment again. Most (but not
                all) tasks are divided up into well-defined episodes, and done
                being True indicates the episode has terminated. (For example,
                perhaps the pole tipped too far, or you lost your last life.)
            info (dict) :
                 diagnostic information useful for debugging. It can sometimes
                 be useful for learning (for example, it might contain the raw
                 probabilities behind the environment's last state change).
                 However, official evaluations of your agent are not allowed to
                 use this for learning.
        """
        self.vnc_client.timeout = 5
        episode_over = False
        reward = 0.0
        ob = None

        try:
            for k in str(action):
                self.vnc_client.keyPress(k)
            self.vnc_client.keyPress("enter")
            i = 0
            exit_code = 0
            while i < 20:
                try:
                    exit_code = int(requests.get("http://localhost:8000/exit_code.txt").text)
                    break
                except:
                    time.sleep(1.0)
                    i += 1
            reward = self.get_reward_from_exit_code(exit_code)
            self.vnc_client.captureScreen('screenshot.png')
            time.sleep(1.0)
            ob = Image.open('screenshot.png')
        except Exception as e:
            print(str(e))
            episode_over = True

        return ob, reward, episode_over, {}

    @staticmethod
    def get_reward_from_exit_code(code):
        if code == 0:
            return 1
        else:
            return 0

    def reset(self):
        try:
            self.container.kill()
            self.vnc_client.disconnect()
            self.__init__()
        except:
            pass

    def render(self, mode='human', close=False):
        screen = Image.open('screenshot.png')
        screen.show()
