# -*- coding: UTF-8 -*-
__author__ = 'Sliver'

S = [[0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05],
     [0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99],
     [0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62],
     [0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6],
     [0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8],
     [0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35],
     [0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87],
     [0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e],
     [0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1],
     [0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3],
     [0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f],
     [0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51],
     [0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8],
     [0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0],
     [0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84],
     [0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]]

CK = [0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
      0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
      0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
      0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
      0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
      0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
      0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
      0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279]

FK = [0xA3B1BAC6, 0x56AA3350, 0x677D9197, 0xB27022DC]


def dex2bin8(dex):
    '''
    将十进制数值转化为8位二进制字符串。
    如：97 -> '01100001'
    '''
    bin_str = bin(dex).replace('0b', '')
    space = 8 - len(bin_str)
    # 不足8位的补全为8位
    bin_str = '0' * space + bin_str
    return bin_str


def dex2bin32(dex):
    '''
    将十进制数值转化为32位二进制字符串。
    如：233 -> '00000000000000000000000011101001'
    '''
    bin_str = bin(dex).replace('0b', '')
    space = 32 - len(bin_str)
    # 不足32位的补全为32位
    bin_str = '0' * space + bin_str
    return bin_str


def bytes2bin(text):
    '''
    将输入的bytes类型数据转化为包含二进制流的列表。
    如：b'ABCDEFGHABCDEFGH' -> ['01000001010000100100001101000100',
                               '01000101010001100100011101001000',
                               '01000001010000100100001101000100',
                               '01000101010001100100011101001000']
    '''
    # string = string.encode('utf-8')
    temp = [dex2bin8(text[i]) for i in range(len(text))]
    result = []
    for i in range(4):
        result.append(''.join(temp[i * 4:i * 4 + 4]))
    return result


def bin2bytes(text):
    '''
    将输入包含二进制流的列表转化为bytes类型的输出。
    如：['01000001010000100100001101000100',
        '01000101010001100100011101001000', -> b'ABCDEFGHABCDEFGH'
        '01000001010000100100001101000100',
        '01000101010001100100011101001000']
    '''
    string = ''.join(text)
    temp = [int(string[i * 8:i * 8 + 8], 2) for i in range(16)]
    return bytes(temp)


def shift(num, times):
    '''
    将传入的二进制序列按指定次数往左循环移位。
    如：'01000001010000100100001101000100' & 2 -> '00000101000010010000110100010001'
    '''
    return num[times:] + num[:times]


def group(text):
    '''
    分组操作，将所输入字符串以8位为一分组，存储在列表中并返回。
    如：'01000001010000100100001101000100' -> ['01000001', '01000010', '01000011', '01000100']
    '''
    result = []
    for i in range(len(text) // 8):
        temp = text[i * 8:i * 8 + 8]
        result.append(temp)
    return result


def xor(num1, num2):
    '''两个32位二进制字符串的异或操作。'''
    num1, num2 = int(num1, 2), int(num2, 2)
    return dex2bin32(num1 ^ num2)


def xor4(num1, num2, num3, num4):
    '''四个32位二进制字符串的异或操作。'''
    num1, num2, num3, num4 = map(lambda num: int(num, 2), [num1, num2, num3, num4])
    return dex2bin32(num1 ^ num2 ^ num3 ^ num4)


def SBox(num):
    '''S盒置换：将8位输入的高半字节作为行号，低半字节作为列号进入S盒得到8位输出。'''
    high, low = int(num[:4], 2), int(num[4:], 2)
    return dex2bin8(S[high][low])


def tPermutation(text):
    '''非线性变换τ：使用4个S盒并行置换32位输入，得到32位输出。'''
    text = group(text)
    return ''.join([SBox(num) for num in text])


def LPermutation(text, flag=0):
    '''
    字节性部件变换L：32位输入，32位输出。
    flag != 0 时，使用逆置换。'''
    copy = text[:]
    MOVETIMES = [2, 10, 18, 24] if flag == 0 else [13, 23]
    for i in range(len(MOVETIMES)):
        temp = shift(copy, MOVETIMES[i])
        text = xor(text, temp)
    return text


def TPermutation(text, flag=0):
    '''
    字合成变换T：由非线性变换τ和线性变换L复合而成，32位输入得到32位输出。
    flag != 0 时，使用逆置换。
    '''
    return LPermutation(tPermutation(text), flag)


def F(X, subkey):
    '''轮函数：与轮密钥一起，得到32位输出。'''
    temp = TPermutation(xor4(X[1], X[2], X[3], subkey))
    return xor(X[0], temp)


def CreateSubKeys(primarykey):
    '''密钥拓展：产生32个轮密钥。'''
    subkeys = []
    K = [0 for _ in range(36)]
    for i in range(4):
        K[i] = xor(primarykey[i], dex2bin32(FK[i]))

    for i in range(32):
        temp = TPermutation(xor4(K[i + 1], K[i + 2], K[i + 3], dex2bin32(CK[i])), flag=1)
        K[i + 4] = xor(K[i], temp)
        subkeys.append(K[i + 4])
    return subkeys


def cipher(message, primarykey, mode='encrypt'):
    primarykey = bytes2bin(primarykey.encode('utf-8'))

    if mode == 'encrypt':
        subkeys = CreateSubKeys(primarykey)
    else:
        subkeys = CreateSubKeys(primarykey)[::-1]

    X = [0 for _ in range(36)]
    X[0:4] = message

    for i in range(32):
        X[i + 4] = F(X[i:i + 4], subkeys[i])

    return bin2bytes(X[::-1][:4])


if __name__ == '__main__':
    a = cipher(bytes2bin('abcdefghABCDEFGH'.encode()), 'ABCDEFGHabcdefgh')
    print(a)
    b = cipher(bytes2bin(a), 'ABCDEFGHabcdefgh', mode='decrypt')
    print(b)