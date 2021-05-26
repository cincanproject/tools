from setuptools import setup

setup(
    name='cincan-test-wrapper',
    version='0.2',
    packages=['testing'],
    install_requires=['docker', 'cincan-command', 'six'],
    entry_points={
        'console_scripts': ['cincan-test=testing.dockertools:main'],
    },
    description='CinCan Test Wrapper',
    python_requires='>=3.6',
)
