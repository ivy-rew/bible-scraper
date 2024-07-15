#!/usr/bin/env python3

import runpy
import os

pwd=os.path.dirname(os.path.abspath(__file__))

runpy.run_path(path_name=pwd+'/scraper/main.py')

