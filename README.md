# useful-scripts

Useful scripts for configuring many aspects of GNU/Linux

# About

Sets more sensible settings than the defaults with an emphasis on speed, usability, aesthetics, and reducing wear on the SSD.
Installed programs are automatically detected and configured by running `all.py`.
Any type of config file can be modified with easy to use API.

## Supported programs

bash, firefox, neovim, python

# Requirements

- python >= 3.8

# Usage

to configure everything automatically run `python all.py`

you can also selectively run for each program: `python firefox`

you can even choose to only configure a certain aspect of the program: `python bash/prompt.py`
