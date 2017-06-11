# Copyright 2017 SrMouraSilva
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
from setuptools import setup


def readme():
    here = path.abspath(path.dirname(__file__))

    with open(path.join(here, 'README.rst'), encoding='UTF-8') as f:
        return f.read()

setup(
    name='PedalPi-Raspberry-P0',
    version='0.2.1',

    description='A simple physical controller for change and view the current pedalboard',
    long_description=readme(),

    url='https://github.com/PedalPi/Raspberry-P0',

    author='Paulo Mateus Moura da Silva (SrMouraSilva)',
    author_email='mateus.moura@hotmail.com',
    maintainer='Paulo Mateus Moura da Silva (SrMouraSilva)',
    maintainer_email='mateus.moura@hotmail.com',

    license="Apache Software License v2",

    packages=[
        'raspberry_p0',
        'raspberry_p0/configurations',
        'raspberry_p0/physical',
    ],
    package_data={
        'raspberry_p0': ['*.ini']
    },
    install_requires=[
        'gpiozero',
        'PedalPi-Application>=0.3.0',
        'PedalPi-Raspberry-Physical'
    ],

    test_suite='test',
    test_requires=[
        'gpiozero',
        'PedalPi-Application>=0.3.0',
        'PedalPi-Raspberry-Physical>=0.2.0'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Multimedia :: Sound/Audio',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='pedal-pi mod-host lv2 audio plugins-manager raspberry',

    platforms='Linux',
)
