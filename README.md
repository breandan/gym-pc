# gym-pc

An OpenAI Gym environment for a PC. Teach a computer to use a computer like a human uses a computer.

## Usage

Prerequisites: 

* Docker
* Python

Install via `pip install .`

```
import gym
import gym_pc
env = gym.make('GymPC-Ubuntu')
```

## Testing

First, start a container: `docker run -it --rm -p 6080:80 -p 5900:5900 breandan/ubuntuvnc`

Then visit: [http://127.0.0.1:6080/](http://127.0.0.1:6080/) and manually open the terminal window.

Then, on your local machine run the following: 

```
git clone https://github.com/breandan/gym-pc && \
    cd gym-pc && \
    pip3 install . && 
    python3 gym-pc/envs/linux_env.py`
```
