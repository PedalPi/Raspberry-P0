from setuptools import setup
setup(
    name='PedalPi - Raspberry-P0',
    packages=[
        'raspberry_p0/',
        'raspberry_p0/action',
        'raspberry_p0/action',
        'raspberry_p0/component',
        'raspberry_p0/mvc',
        'raspberry_p0/mvc/pedalboards',
    ],
    package_data={
        'raspberry_p0/': ['*.ini']
    },
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
