'Wheel File Creation for the website for efficient loading.'
from setuptools import find_packages,setup
packages=find_packages(exclude=['tests','base-hack','build','dist','docs','scripts','tmp'])
setup(name='dk64rando',version='1.0.0',packages=packages)