#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/9 
"""

import hashlib


def hash_pub_key(pub_key):
    if not isinstance(pub_key, (bytes, bytearray, str)):
        raise TypeError("pub 类型错误，需要str 或者bytes类型！")

    if isinstance(pub_key, str):
        pub_key = pub_key.encode("utf-8")

    # sha256 hash
    pub_sha256 = hashlib.sha256(pub_key).hexdigest()

    # ripemd160
    obj = hashlib.new("ripemd160", pub_sha256.encode('utf-8'))
    ripemd160_value = obj.hexdigest()

    return ripemd160_value
