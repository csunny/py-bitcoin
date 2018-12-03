#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/30
"""

from pyp2p.net import *
import time

# Magic Node
magic = Net(passive_bind="0.0.0.0", passive_port=4444, node_type="passive", debug=True)
magic.start()

