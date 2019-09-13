from setuptools import setup

setup(
    name='CinCanCommandProgram',
    version='0.1beta',
    packages=['metatool', ],
    install_requires=['docker'],
    entry_points = {
        'console_scripts': ['metatool=metatool.dockertools:main'],
    }
)