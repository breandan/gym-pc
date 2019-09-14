from random import random

import numpy as np
import pytesseract

from gym_pc.envs import LinuxEnv

if __name__ == '__main__':
    with open('commands.txt') as fo:
        COMMAND_LIST = fo.readlines()

    epsilon = 0.9
    q_list = np.ones(len(COMMAND_LIST))
    n_list = np.ones(len(COMMAND_LIST))

    env = LinuxEnv()
    while True:
        p = random()
        if p > epsilon:
            action_index = np.argmax(q_list)
        else:
            action_index = np.random.choice(np.arange(len(COMMAND_LIST)), p=q_list / sum(q_list))
        action = COMMAND_LIST[action_index].rstrip('\n')
        img, reward, _, _ = env.step(action)
        n_list[action_index] += 1
        q_list[action_index] = q_list[action_index] + (reward - q_list[action_index]) / n_list[action_index]
        # env.render()
        wrd = pytesseract.image_to_string(img, lang= "eng", config="--psm 4 --oem 3 -c tessedit_char_whitelist=command")
        print('Action: ' + action + ', Reward: ' + str(reward))