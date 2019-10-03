from setuptools import setup

setup(
    name='CinCan-Command-Program',
    version='0.1b',
    packages=['metatool'],
    install_requires=['docker'],
    entry_points = {
        'console_scripts': ['cccp=metatool.dockertools:main'],
    },
    description='CinCan Command Program',
    python_requires='>=3.6',
)