#!/usr/bin/env python

__author__ = 'Manish Dawash'
__date__ = '08 Jan 2021'
__version__ = '1.1.0'

import configparser


def create_config():
    """
        Function to return ConfigParser object to read configuration from pythief.ini file
    """
    config_parser = configparser.ConfigParser()
    config_parser.read('../../pythief.ini')
    return config_parser


config = create_config()
