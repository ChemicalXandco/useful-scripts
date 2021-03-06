# useful-scripts

Configurations for a wide range of software.

# About

Sets more sensible settings than the defaults with an emphasis on speed, usability, aesthetics, and reducing wear on the SSD.
Installed programs are automatically detected and configured by running `all.sh`.
Any type of config file can be modified with easy to use API.
An advantage of managing the configs this way is that only the modifications are stored and can be applied to any file no matter what it already contains.

# Compatibility

## Operating system

Arch and Debian have first class support.
Alpine, Gentoo, NixOS, OpenSUSE, Red Hat, MacOS, Windows, and derivatives should be usable also.

## Supported program configs

all configurations are listed in [./config/](config/)

# Requirements

- python >= 3.8

# Usage

to configure everything automatically run `sh all.sh`

you can also selectively run for each program: `python config/firefox`

you can even choose to only configure a certain aspect of the program: `python config/bash/prompt.py`
