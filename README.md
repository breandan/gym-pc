# gym-pc

Personal Computing Environment for OpenAI Gym. Teach a computer to use a computer like a human uses a computer.

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

Then, on your local machine run the following commands: 

```
git clone https://github.com/breandan/gym-pc && \
    cd gym-pc && \
    pip3 install . && \
    python3 gym-pc/envs/linux_env.py`
```

## Citation

If you wish to cite this work, please use the following `bibtex` entry:

```
@misc{considine2019gympc,
  authors = {Considine, Breandan and Gastellu, Nicolas and Rosenblitt, Jared and Simine, Yelina},
  title = {Personal Computing Environment for OpenAI Gym},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/breandan/gym-pc}},
}
```