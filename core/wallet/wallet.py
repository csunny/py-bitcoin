#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/7 
"""
import hashlib
from fastecdsa import keys, curve
from crypto.base58 import base58encode, base58decode

version = "0x"
addressChecksumLen = 4


class Wallet:
    """
    doc  钱包
    """

    def __init__(self):
        pass

    def new_keypair(self):
        """ 生成公私钥的键值对"""
        priv_key = keys.gen_private_key(curve.P256)

        pub_key = keys.get_public_key(priv_key, curve.P256)

        pub_key = "".join([str(pub_key.x), str(pub_key.y)])

        return priv_key, pub_key

    def get_address(self):
        """

        :return:
        """
        priv_key, pub_key = self.new_keypair()
        pubkey_hash = self.hash_pk(pub_key)
        version_payload = "".join([str(version), str(pubkey_hash)])
        checksum = self.checksum(version_payload)

        full_payload = "".join([str(version_payload), str(checksum)])

        address = base58encode(full_payload)
        return address

    def hash_pk(self, pub_key):
        """
        公钥加密
        :param pub_key:
        :return:
        """
        if not isinstance(pub_key, (bytes, bytearray, str)):
            raise TypeError("pub 类型错误，需要str 或者bytes类型！")

        if isinstance(pub_key, str):
            pub_key = pub_key.encode("utf-8")

        # sha256 加密
        pub_sha256 = hashlib.sha256(pub_key).hexdigest()

        # ripemd160
        obj = hashlib.new("ripemd160", pub_sha256.encode('utf-8'))
        ripemd160_value = obj.hexdigest()

        return ripemd160_value

    def checksum(self, payload):
        """"""

        if not isinstance(payload, (bytes, bytearray, str)):
            raise TypeError("payload 类型错误，需要str 或者bytes类型！")

        if isinstance(payload, str):
            payload = payload.encode("utf-8")

        first_sha = hashlib.sha256(payload).hexdigest()
        second_sha = hashlib.sha256(first_sha.encode('utf-8')).hexdigest()

        return second_sha[:addressChecksumLen]

    def validate_addr(self, address):
        """

        :return:
        """
        pub_key_hash = base58decode(address)

        actural_check_sum = pub_key_hash[len(pub_key_hash) - addressChecksumLen:]
        version = pub_key_hash[0]
        pub_key_hash = pub_key_hash[1:len(pub_key_hash) - addressChecksumLen]

        payload = "".join([str(version), str(pub_key_hash)])

        target_check_sum = self.checksum(payload)

        return actural_check_sum == target_check_sum






