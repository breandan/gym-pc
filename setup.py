from setuptools import setup

setup(
    name='gym_pc',
    version='0.1',
    install_requires=['gym', 'docker', 'vncdotool', 'pytesseract'],
    packages=["gym-pc"],
    url="https://github.com/breandan/gym-pc"
)
