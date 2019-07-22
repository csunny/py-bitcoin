#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created bt Magic at 2019/7/22
"""

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

ENCRYPTO_KEY = b"45c7809a825c424f"

class AESCrypto:
    """
    : aes crypto
    """
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    # 加密
    def encrypto(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)

        if (count % length) != 0:
            add = length - (count % length)
        else:
            add = 0
        
        text = text + (b'\0' * add)
        self.ciphertext = cryptor.encrypt(text)

        return b2a_hex(self.ciphertext)

    def decrypto(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))

        return plain_text.rstrip(b'\0')


if __name__ == "__main__":
    ase = AESCrypto(ENCRYPTO_KEY)

    s = ase.encrypto(b'123')
    print(s)

    a = ase.decrypto(s)
    print(a)

    assert a == b"123"