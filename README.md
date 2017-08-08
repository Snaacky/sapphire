# Sapphire
A trigger bot for CS:GO written in Python.

## Warning
Sapphire comes as is with no guarentees regarding VAC status. This is a cheat and can very well get you banned if you attempt to use it on any cheat protected servers. I will not be held resposible if you get banned because of this project.

## Requirements
* [Python 3.x](https://www.python.org/)
* [Pymem](https://github.com/srounet/Pymem)
* [keyboard](https://github.com/boppreh/keyboard)
* [pywin32](https://sourceforge.net/projects/pywin32/files/?source=navbar)

## Limitation
As of this commit, [keyboard](https://github.com/boppreh/keyboard) currently does not have support for simulating mouse clicks. A temporary workaround for simulating mouse clicks is binding an unused key in-game to +attack and specifiying which key under config.py while we wait for support in a future update.
