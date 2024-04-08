# JOYSTICK JUNKIE

## Description

Repository: https://github.com/kelvgooding/joystick_junkie

Joystick Junkie is web app, which is used to centralise your video game collection. The data is stored in an local SQLite3 database, which is created for the first time when the application is launched.

## OS Compatibility

- Linux
- Windows

## Dependencies

### Linux Packages

- python3
- python3-pip

### Python Modules

- from flask import Flask, render_template, request, flash
- from modules import db_check
- import os

## Installation

To download this web application, run the following commands on your linux environment:

Downloading the repository from GitHub:
```
cd ~
git clone git@github.com:kelvgooding/joystick_junkie.git
```

Installating the requirements.txt file to ensure the correct packages are available and installed:

```
cd ~/joystick_junkie
pip3 install -r requirements.txt
```

Running the application:

```
cd ~/joystick_junkie
python3 ~/joystick_junkie/app.py >> ~/joystick_junkie`date +\%Y\%m\%d`.log 2>&1 &
```

The log file will contain the URL for the application, along with each request that is made.

## Stakeholders

PM: Kelvin Gooding | kelv.gooding@outlook.com<br>
Design: Kelvin Gooding | kelv.gooding@outlook.com<br>
Dev: Kelvin Gooding | kelv.gooding@outlook.com<br>
QA: Kelvin Gooding | kelv.gooding@outlook.com<br>
Support: Kelvin Gooding | kelv.gooding@outlook.com

## Contribution

Issue Tracker: https://github.com/kelvgooding/joystick_junkie/issues<br>
Contact: Kelvin Gooding | kelv.gooding@outlook.com
