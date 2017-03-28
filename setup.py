from setuptools import setup
setup(
    name='PedalPi - Raspberry-P0',
    packages=[
        'action',
        'component',
        'mvc',
        'mvc/pedalboards',
    ],
    test_suite='test',
    install_requires=[
        'gpiozero',
        'PedalPi-Application',
        'PedalPi-Physical'
    ],
    dependency_links=[
        'https://github.com/PedalPi/Application/tarball/master#egg=PedalPi-Application',
        'https://github.com/PedalPi/Physical/tarball/master#egg=PedalPi-Physical'
    ]
)
