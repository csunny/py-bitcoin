Base58 是用于Bitcoin中使用的一种独特的编码方式，主要用于产生Bitcoin的钱包地址，相比于Base64、Base58步使用 0， 大些字母O、I和小写字母 l 以及 + 和 / 符号。

**设计Base58的主要目的有以下几点:**

1. 避免混淆，在某些字体下，数字0和字母大写O 以及字母大写I和字母小写l会非常相似，难以辨认。
2. 不使用+和/的原因是非字母或数字的字符串作为账号较难被接受。
3. 没有标点符号，通常不会被从中间分行
4. 大部分软件支持双击选择整个字符串。

**Base58编码**

Value | Char | Value | Char | Value| Char| Value| Char
------|------|-------|------|------|-----|------|-----
0     | 1    | 16    | H    | 32   | Z   |  48  | q 
1     | 2    | 17    | J    | 33   | a   |  49  | r
2     | 3    | 18    | K    | 34   | b   |  50  | s
3     | 4    | 19    | L    | 35   | c   |  51  | t
4     | 5    | 20    | M    | 36   | d   |  52  | u
5     | 6    | 21    | N    | 37   | e   |  53  | v
6     | 7    | 22    | P    | 38   | f   |  54  | w
7     | 8    | 23    | R    | 39   | g   |  55  | x
8     | 9    | 24    | S    | 40   | h   |  56  | y
9     | A    | 25    | T    | 41   | i   |  57  | z
10    | B    | 26    | U    | 42   | j   
11    | C    | 27    | V    | 43   | k
12    | D    | 28    | W    | 44   | m
13    | E    | 29    | X    | 45   | n
14    | F    | 30    | Y    | 46   | o
15    | G    | 31    | Z    | 47   | p


即
```python
Base58=[1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", 
"F", "G", "H", "G", "K", "L", "M", "N", "P", "Q", "R", "S", 
"T", "U", "V", "W", "X", "Y", "Z", "O", "P", "Q", "R", "S", "T", 
"U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g",
 "h", "i", "g", "k","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", 
 "w", "x", "y", "z" ]

```

以上是Base58加密算法的理论，接下来，我们分别用python和go语言来实现Base58加密算法。

#### python 实现

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/6 
"""

Base58Alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def base58decode(data):
    """
    base58 解码
    :param data:
    :return:
    """
    result = 0

    for d in data:
        charIndex = Base58Alphabet.find(d)
        result = result * len(Base58Alphabet)
        result = result + charIndex

    decoded = hex(result)

    # if data[0] == Base58Alphabet[0]:
    #     decoded = str(0x0) + decoded

    return decoded


def base58encode(data):

    result = []
    # 首先将字符串转换成十六进制数
    x = int(data, 16)
    base = 58

    zero = 0

    while x != zero:
        x, mod = divmod(x, base)
        result.append(Base58Alphabet[mod])

    # if data[0] == str(0x0):
    #     result.append(Base58Alphabet[0])

    # 利用自己实现的reverse算法，当然实际工作中直接调用python标准库中的函数
    return "".join(reverse(result))


def reverse(res):
    """
    反转列表
    :param res:
    :return:
    """

    if len(res) <= 1:
        return res

    length_half = int(len(res) / 2)
    length = len(res) - 1

    for i in range(length_half):
        tmp = res[i]
        res[i] = res[length-i]
        res[length-i] = tmp

    return res

```

代码解读：

Base58编码过程
1. 将字符串转化为16进制
2. 将16进制转化为十进制
3. 将十进制转化为Base58中的字符
4. 颠倒字符串顺序

Base58解码：
1. 将编码的字符串转换为十进制
2. 将十进制转化为十六进制
3. 将十六进制转化为字符串

#### 简单测试
```python

from crypto.base58 import base58encode, base58decode

if __name__ == '__main__':

    # data = "0x110966776006953D5567439E5E39F86A0D273BEED61967F6"
    #
    # r = base58encode(data)
    # print(r)
    #
    # s = base58decode(r)
    #
    # assert len(s) == len(data)
    # assert s.lower() == data.lower()
    
    data3 = "0xa0b50f87ffd489b87b5539879d70a1ca857bc43ce229"

    res = base58encode(data3)
    print(res)

    sv = base58decode(res)
    print(sv)
    print(data3)

```

#### go实现

``` 

package main

import (
	"bytes"
	"math/big"
	"fmt"
)

var b58Alphabet = []byte("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")

// Base58Encode encodes a byte array to Base58
func Base58Encode(input []byte) []byte {
	var result []byte

	x := big.NewInt(0).SetBytes(input)

	base := big.NewInt(int64(len(b58Alphabet)))
	zero := big.NewInt(0)
	mod := &big.Int{}

	fmt.Println(x, base)
	for x.Cmp(zero) != 0 {
		x.DivMod(x, base, mod)
		result = append(result, b58Alphabet[mod.Int64()])
	}

	// https://en.bitcoin.it/wiki/Base58Check_encoding#Version_bytes
	if input[0] == 0x00 {
		result = append(result, b58Alphabet[0])
	}

	ReverseBytes(result)

	return result
}

// Base58Decode decodes Base58-encoded data
func Base58Decode(input []byte) []byte {
	result := big.NewInt(0)

	for _, b := range input {
		charIndex := bytes.IndexByte(b58Alphabet, b)

		result.Mul(result, big.NewInt(58))
		result.Add(result, big.NewInt(int64(charIndex)))

		fmt.Println("--------", string(b), charIndex, result)


	}

	decoded := result.Bytes()

	if input[0] == b58Alphabet[0] {
		decoded = append([]byte{0x00}, decoded...)
	}

	return decoded
}

```

项目源码地址: https://github.com/csunny/py-bitcoin

参考：
- https://zh.wikipedia.org/wiki/Base58
- https://github.com/Jeiwan/blockchain_go/tree/part_5


