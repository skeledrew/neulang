# Neu
Coding for humans.

## Description
Neu is a natural language layer running on Python. It takes scripts containing pseudocode in [Org](http://orgmode.org/) format (other formats coming soon) and runs it.

## Why?
As the easiest programming language for anyone to learn, Python is awesome.
But there's still that curve that continues to shut many out of the coding world.
People shouldn't have to learn another language to code, esp in this age of smart devices, IoT and AI.
Let's bring coding to the people, not the people to coding.
Oh, and I have a lot of pseudocode in Org that I'd like to make executable.

## Installing
* `pip install git+https://github.com/skeledrew/neulang.git`

## Features
* Command line mode
  * `neu [options] -c "command"`
* Interactive mode
  * Written in org!
  * `neu [options]`
  * Exit with `-*exit*-` or `-*quit*-`
* Importable as module
  * `from neulang.cerebrum import Cerebrum`
  * `c = Cerebrum()`
  * `script = "* print hello world"`
  * `c.read(script)`
  * `c.think()`
* Run script files
  * `neu [options] /path/to/script.org`

## To Do
* Add all keywords and builtins
* Add support for YAML and MD styles