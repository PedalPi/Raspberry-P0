# Raspberry P0

[![Code Health](https://landscape.io/github/PedalPi/Raspberry-P0/master/landscape.svg?style=flat-square)](https://landscape.io/github/PedalPi/Raspberry-P0/master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/f3e1af57f11d4d9e8be097153ce68195)](https://www.codacy.com/app/mateus-moura/Raspberry-P0?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=PedalPi/Raspberry-P0&amp;utm_campaign=Badge_Grade)

A simple physical controller for change and view the current pedalboard with 2 buttons and 7 two segments displays

```
╔═══════════════════════════════════════════╗
║              P e d a l   P i           P0 ║
║                 ┌ ⎯  ⎯  ┐                 ║
║                 |⎥⎯⎜⎥ ⎜ |                 ║
║                 |⎥  ⎥⎯⎜.|                 ║
║                 └-------┘                 ║
║---------------------┬---------------------╢
║ ..=.............=.. | .........=......... ║
║ ....=.........=.... | ......=.....=...... ║
║ ......=.....=...... | ....=.........=.... ║
║ .........=......... | ..=.............=.. ║
╚═══════════════════════════════════════════╝

```

## Elements list:

 - ![A seven segments displays component](docs/seven-segments-example.jpg) 2 seven segments displays;
 - ![A push button component](docs/button-example.jpg) 2 push buttons for Pedalboard change.

## Installation

**FIXME**
View the [Application documentation](http://pedalpi-application.readthedocs.io/en/latest/?badge=latest#using) for more details how to add others components.

### Dependencies

**Pedal Pi - Raspberry P0** requires `gpiozero >= 1.2.0` for access GPIO and [Physical project](http://github.com/PedalPi/Physical) for SevenSegments lib ([gpiozero not contains yet](https://github.com/RPi-Distro/python-gpiozero/issues/493)). 

## `program.py`

The following example demonstrates a basic setup for the Pedal Pi - Raspberry P0. If you want to add other components, check the [component list](https://github.com/PedalPi/Components). 

```python
import sys
from signal import pause

sys.path.append('physical')
sys.path.append('raspberry_p0')

from application.application import Application
from raspberry_p0.raspberry_p0 import RaspberryP0

address = 'localhost'
port = 3000

application = Application(data_patch="data/", address=address, test=True)
application.register(RaspberryP0(application))

application.start()

pause()
```

## Schematic

![P0 in the Fritzing](docs/schematic.jpg)

### Pins

The pins of the seven-segment displays are shared with each other. That is, the `pin_a` of display 1 is shorted with the` pin_a` of display 2, `pin_b` of display 1 is shorted with` pin_b` of display 2 and so on.
However, this rule does not apply to `common_pin`, where each display must have its own control pin.

The used pins are:
 
| Config identifier      | Pin¹     | Type         | Function                          |
| ---------------------- | -------- | ------------ |---------------------------------- | 
| pin_a                  | `13`     | integer      | Seven segments - Pin A            |
| pin_b                  | ` 6`     | integer      | Seven segments - Pin B            |
| pin_c                  | `16`     | integer      | Seven segments - Pin C            |
| pin_d                  | `20`     | integer      | Seven segments - Pin D            |
| pin_e                  | `21`     | integer      | Seven segments - Pin E            |
| pin_f                  | `19`     | integer      | Seven segments - Pin F            |
| pin_g                  | `26`     | integer      | Seven segments - Pin G            |
| pin_h                  | ` 0`     | integer      | Seven segments - Dot point pin    |
| common_pins            | `[5, 1]` | integer list | Seven segments - Dot point pin    |
| common_anode           | True          | bool         | `True` if the displays are anode. `False` if are cathode. |
| next_pedalboard        | `14`     | integer      | Button - Set to next Pedalboard   |
| before_pedalboard      | `15`     | integer      | Button - Set to before Pedalboard |

¹ [**BCM** pin numeration](https://pinout.xyz/)

## Configure file

It's possible changes the pins using a configuration file. The numbering of the pins corresponds to **BCM**.
It's necessary informs all configurations.
  
A Raspberry Pi pinout schematic can be seen in [pinout.xyz](https://pinout.xyz/)

The __config_file__ has the following structure:
```
[DEFAULT]
pin_a = 13
pin_b = 6
pin_c = 16
pin_d = 20
pin_e = 21
pin_f = 19
pin_g = 26
pin_dp = 0

common_pins = [5, 1]
common_anode = True

next_pedalboard = 14
before_pedalboard = 15

[test]
test = True
```

For P0 loads the new configuration, references the file in `RaspberryP0` constructor.

```python
# The config file has named as 'path/my_awersome_config.ini'.
application.register(RaspberryP0(application, configuration_file='my_awersome_config.ini'))
```

### ![A seven segments displays component](docs/seven-segments-example.jpg)  Seven segments display

<img align="left" height="150" src="https://raw.githubusercontent.com/PedalPi/Raspberry-P0/master/docs/7_segment_display_pin_outs.png" alt="Seven segments display pinout" />

The seven-segment display consists of eight pins corresponding to the leds (`pin_a` to` pin_g` and `pin_dp`) and two common pins (which are short-circuited).

There are two types of seven-segment displays: Cathode and Anode. `common_anode` informs if the displays are Anode or Cathode.

The image obtained from [Circuits Today](http://www.circuitstoday.com/arduino-and-7-segment-display) illustrates the correspondence of the pins with the LEDs.

#### Led pins

To save the amount of pins required for the project, the pins of the seven-segment displays are shared with each other. In this way, the pins corresponding to the pins' leds (`pin_a` to` pin_g` and `pin_dp`) must respectively be shorted to the displays.
That is, the `pin_a` of display 1 is shorted with the` pin_a` of display 2, `pin_b` of display 1 is shorted with` pin_b` of display 2 and so on.

| Config identifier      | Default value | Type         | Function                          |
| ---------------------- | ------------- | ------------ |----------------- | 
| `pin_a`                | `13`          | integer      | Pin A            |
| `pin_b`                | ` 6`          | integer      | Pin B            |
| `pin_c`                | `16`          | integer      | Pin C            |
| `pin_d`                | `20`          | integer      | Pin D            |
| `pin_e`                | `21`          | integer      | Pin E            |
| `pin_f`                | `19`          | integer      | Pin F            |
| `pin_g`                | `26`          | integer      | Pin G            |
| `pin_h`                | ` 0`          | integer      | Dot point pin    |

#### Common pins

To describe the `common_pin` of the displays, a list of integers is used, where the significance of the digits follows the ascending order:
the _tens_ corresponds to the first element of the list and the _units_ to the second element of the list.


| Config identifier      | Default value | Type         | Function                          |
| ---------------------- | ------------- | ------------ |---------------------------------- | 
| `common_pins`          | `[5, 1]`      | integer list | Dot point pin                     |
| `common_anode`         | True          | bool         | `True` if the displays are anode. `False` if are cathode. |   

### ![A push button component](docs/button-example.jpg) Push buttons

<img align="right" height="150" src="https://raw.githubusercontent.com/PedalPi/Raspberry-P0/master/docs/momentary-footswitch.jpg" alt="Momentary footswitch example" />

Simple push buttons were used to change the current pedalboard. For use with foot, is recommended use of momentary footswitches. In the future, two states button support will be added.

| Config identifier      | Default value | Type    | Function                                  |
| ---------------------- | ------------- | ------- |------------------------------------------ | 
| next_pedalboard        | `14`          | integer | Set the current pedalboard for the next   |
| before_pedalboard      | `15`          | integer | Set the current pedalboard for the before |

### Other configurations

| Config identifier | Default value  | Type | Function                                |
| ----------------- | -------------- | ---- | --------------------------------------- | 
| `test`            | `False`        | bool | Disable GPIOZero for development tests  |

## Examples

![P0 in a protoboard](docs/Example.jpg)