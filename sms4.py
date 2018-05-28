# -*- coding: UTF-8 -*-
__author__ = 'Sliver'

import base64
from operation import cipher, bytes2bin

class SMS4:
    def __init__(self, message, primarykey):
        self.message = message
        self.primarykey = primarykey

    @property
    def ciphertext(self):
        return self.__encrypt()

    @property
    def plaintext(self):
        return self.__decrypt().decode('utf-8').rstrip(b'\x00'.decode('utf-8'))

    def __encrypt(self):
        message = bytes(self.message.encode('utf-8'))
        length = len(message)
        times, mod = divmod(length, 16)
        result = bytes()

        if mod:
            space = 16 - mod
            message += bytes([0 for _ in range(space)])
            times += 1

        for i in range(times):
            result += cipher(bytes2bin(message[i * 16:i * 16 + 16]),
                             self.primarykey)

        return base64.b64encode(result).decode("ascii")

    def __decrypt(self):
        message = base64.b64decode(self.message.encode("ascii"))
        length = len(message)
        times, mod = divmod(length, 16)
        result = bytes()

        if mod:
            return False

        for i in range(times):
            result += cipher(bytes2bin(message[i * 16:i * 16 + 16]),
                             self.primarykey, mode='decrypt')

        return result


class File:
    def __init__(self, primarykey):
        self.primarykey = primarykey

    @staticmethod
    def __readfile(filename):
        with open(filename, 'rb') as f:
            bytesflow = f.read()
        return bytesflow

    @staticmethod
    def __writefile(filename, bytesflow, mode=0):
        first = {0: 'encrypt.', 1: 'decrypt.'}
        last = filename.split('.')[-1]
        with open(first[mode] + last, 'wb') as f:
            f.write(bytesflow)

    def encrypt(self, filename):
        message = self.__readfile(filename)
        length = len(message)
        times, mod = divmod(length, 16)
        result = bytes()

        if mod:
            space = 16 - mod
            message += bytes([0 for _ in range(space)])
            times += 1

        for i in range(times):
            result += cipher(bytes2bin(message[i * 16:i * 16 + 16]),
                             self.primarykey)

        self.__writefile(filename, result, mode=0)

    def decrypt(self, filename):
        message = self.__readfile(filename)
        length = len(message)
        times, mod = divmod(length, 16)
        result = bytes()

        if mod:
            return False

        for i in range(times):
            result += cipher(bytes2bin(message[i * 16:i * 16 + 16]),
                             self.primarykey, mode='decrypt')

        self.__writefile(filename, result.rstrip(b'\x00'), mode=1)


if __name__ == '__main__':
    a = SMS4('你好啊，我是 Sliver。', 'ABCDEFGHabcdefgh')
    print(a.ciphertext)

    b = SMS4(a.ciphertext, 'ABCDEFGHabcdefgh')
    print(b.plaintext)

    # e = File('ABCDEFGHABCDEFGH')
    # e.encrypt('test.js')
    # e.decrypt('encrypt.js')

    # f = File('ABCDEFGHABCDEFGH')
    # f.encrypt('test.jpeg')
    # f.decrypt('encrypt.jpeg')