#!/usr/bin/env python
"""
Installation script for the boilerplate, it will take care of everything and
leave a fully working django project in a virtualenv.
"""

import sys
import os
import shutils
import subprocess


def _check_if_command_exists(cmd):

    """
    Quick check using the subprocess module to see if a command exists or is
    accesible from the current path.
    """
    return subprocess.call("type " + cmd, shell=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE) == 0


def install_virtualenv():

    """
    Installs virtualenv globally in the destination computer
    """
    try:
        subprocess.Popen("sudo apt-get install python-virtualenv")
    except:
        sys.exit(" * ERROR: Couldn't install virtualenv. Please try to install it manually. Exiting program...")


def checks():

    """
    Check the python version installed on the system, check if virtualenv is
    already installed, if not it will install it.
    """
    if not sys.version_info[:2] == (2, 7):
        sys.exit(' * ERROR: I need Python 2.7 to run. Exiting.')
    else:
        print " * INFO: Python 2.7 or greater detected."
    try:
        _check_if_command_exists("virtualenv")
        print " * INFO: Virtualenv already installed."
    except:
        print " * WARN: Virtualenv not installed, installing... (will require root access)"
        install_virtualenv()


def install_dependencies():

    """
    This will install any required dependencies like node.js.
    """
    try:
        subprocess.Popen("sudo apt-get install python-software-properties python g++ checkinstall make libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev")
        print " * INFO: Installed system dependencies, proceeding with Node.JS"
        subprocess.Popen("sudo add-apt-repository ppa:chris-lea/node.js")
        subprocess.Popen("sudo apt-get update && sudo apt-get install nodejs")
    except:
        sys.exit(" * ERROR: Something went wrong while installing system dependencies and NodeJS.")

def create_project():

    """
    This function will ecreate a new project with the dboilerplate template.
    """
    pass


def create_htdocs():
    pass

def start():
    checks()
    install_dependencies()
    create_project()
