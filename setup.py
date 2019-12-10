from setuptools import setup

setup(
    name='cincan-test-wrapper',
    version='0.2',
    packages=['metatool'],
    install_requires=['docker', 'cincan-command'],
    entry_points = {
        'console_scripts': ['cincan=metatool.dockertools:main'],
    },
    description='CinCan Test Wrapper',
    python_requires='>=3.6',
)
