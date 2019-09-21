# gym-pc

Personal Computing Environment for [OpenAI Gym](https://gym.openai.com).

## Installation

Prerequisites: 

* [Docker](https://docs.docker.com/install/)
* [Python 3+](https://www.python.org/downloads/)

Install via `pip install .`

## Usage

To use `gym-pc`, first import it and make an environment.

```
import gym
import gym_pc
env = gym.make('GymPC-Ubuntu')
```

An [example agent](gym_pc/agent.py) is provided.

## Testing

First, start a container: `docker run -it --rm -p 8000:8000 -p 6080:80 -p 5900:5900 breandan/ubuntuvnc`

Then visit: [http://127.0.0.1:6080/](http://127.0.0.1:6080/) and manually open the terminal window.

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