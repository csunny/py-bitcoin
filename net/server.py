#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/11 
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=8888, debug=True)
