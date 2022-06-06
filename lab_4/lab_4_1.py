# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:29:51 2022

@author: amrsh
"""

import webbrowser
from random import choice


sites = ["https://google.com", "https://reddit.com", "https://facebook.com", "https://twitter.com"]


webbrowser.open(choice(sites), new=2)
