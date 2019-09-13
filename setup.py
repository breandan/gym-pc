from setuptools import setup

setup(
    name='gym_pc',
    version='0.1',
    url="https://github.com/breandan/gym-pc",
    description='Graphical UI environments for OpenAI Gym',
    packages=['gym_pc', 'gym_pc.envs'],
    install_requires=['gym', 'docker', 'vncdotool', 'pytesseract', 'Pillow'],
)
