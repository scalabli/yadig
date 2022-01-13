#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="citus",
    install_requires=[
        "quo",
        "multiparse",
        "asgiref>= 3.4.0",
        "h11>= 0.8",
        "typing-extensions", # env_marker_below_38",
        "python-dotenv>= 0.13",
        "PyYAML>= 5.1",
        "watchgod>= 0.6",
        "websockets>= 9.1", # env_marker_below_37",
        "websockets>= 10.0", # env_marker_gte_37",
        "httptools>= 0.2.0,< 0.4.0",
        "uvloop>= '0.14.0', != '0.15.0', != '0.15.1'", #env_marker_cpython",
    ],
)
