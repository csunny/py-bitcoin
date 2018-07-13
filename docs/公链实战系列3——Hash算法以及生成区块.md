散列函数（英文：Hash function） 又称为散列算法、哈希函数，是一种从任何一种数据汇总创建的数字“指纹”的方法。 Hash函数把消息或数据压缩成摘要，使得数据量变小，将数据的格式固定下来。该函数将数据打乱混合，重新创建一个叫做散列值（hash value， hash code， hash sums 或hashes）的指纹。 散列值通常用一个短的随机字母和数字组成的字符串代表。 好的散列函数在输入域很少出现散列冲突，在散列表和数据处理中，不抑制冲突来区别数据，会使得数据库记录更难找到。

Hash函数的性质 （非常重要）
所有的Hash函数都有如下一个基本的特性： 如果两散列值是不同的（根据同一函数）， 那么这两个散列值的原始输入也不相同。 这个特性是散列函数具有确定性的结果，具有这种性质的散列函数称为单散列函数。但另一方面， 散列函数的输入和输出不是唯一对应关系的，如果两个散列值相同，两个输入值很可能是相同的，也有可能不同，这种情况称为”散列碰撞“（collision）。

**Hash函数的应用非常广泛：**

最重要的一个应用就是数据结构与算法里讲到的hashtable（哈希表）hash表的重要性这里就不赘述了，想必大家日常编程中肯定是离不开的。
另外hash函数还有以下主要的应用：
* 加密
* 确保传递真实的信息
* 错误校正
* Rabin-Karp字符串搜索算法。

另外这里顺便提一下， 之前在做分布式爬虫与分布式存储相关工作的时候也遇到了hash函数的典型应用，在分布式爬虫里面，我们为了标记那个地址在数据量较小时我们会采用hashtable来快速查找，后面随着数据量的增大，会使用类似Bloom Filter这样更高效的算法。（对Bloom Filter感兴趣的同学可以自己了解下），Bloom Filter在这里不是重点，但使用起来非常方便，各种语言基本都有实现。
另外在分布式存储中，比如Openstack体系里的Swift就是用的hash算法，只不是在Swift中，由于存储需要，其设计了一种非常有些的hash映射算法，在保证均衡映射的前提下，也尽大可能的降低了新文件加入时的变化量。 其官方名字就 hash ring（一致性hash环）， Swift的作为分布式的文件存储系统，在设计上可以说比较优秀，有兴趣的同学，我建议可以读一读Swift的源码， Swift是用python写的，整个代码也比较好懂，个人认为只要搞懂了hash ring那部分的实现，其他架构上的东西，比如分zone、分区等等概念都是比较好理解的，好了，点到为止。关于hash函数的应用暂时就讲到这里。


在本文中，我们要实现区块的生成，就必然要用到hash函数，在下面的代码中我们用的是sha256 加密算法， 关于sha256 算法这里就不讲了，感兴趣的同学自行查阅学习。

前面我们提到，在BlockChain其实就是一个特殊的链表，这个链表只能在尾部添加元素，每一个Block其实就是一个块。同时在这个块中，有几个值相当重要： TimeStamp（时间戳）、 Transactions（交易信息）、PrevBlockHash（上一个块的hash值）、Hash（当前块的hash值）
在这里我们因为还没有交易数据，所以我们把Transactions用data来代替：

**格式如下：**

```python

block = {
    "Timestamp": "",
    "Data": "",
    "PrevBlockHash": "",
    "Hash": "",
}

```

ok，还是那句话，talk is cheap， show  me  the code， 我们上代码吧!

python 实现：
```python

import time
import hashlib

class Block:
    """

    Todo add index for block.

    doc  区块

    block = {
        "Timestamp": "",
        "Data": "",
        "PrevBlockHash": "",
        "Hash": "",
    }
    """

    def __init__(self):
        self.block = dict()

    def new_block(self, data, prev_hash=""):
        block = {
            "TimeStamp": int(time.time()),
            "Data": data,
            "PrevBlockHash": prev_hash,
        }

        b_hash = self.set_hash(block)
        block["Hash"] = b_hash

        self.block = block
        return block

    def set_hash(self, block):
        """

        v1
        # timestamp = hex(block["TimeStamp"])[0]
        #
        # data = "".join([block["PrevBlockHash"], block["Data"], timestamp])
        #
        # return hashlib.sha256(data.encode("utf-8")).hexdigest()
        :param block:
        :return:
        """
        # use pow to set the hash value
        timestamp = hex(block["TimeStamp"])[0]

        data = "".join([block["PrevBlockHash"], block["Data"], timestamp])

        return hashlib.sha256(data.encode("utf-8")).hexdigest()

```

测试:

```python

from core.blockchain.block import Block

if __name__ == '__main__':
    b = Block()

    b.new_block("Magic", "")

    block = b.block

    new_block = b.new_block("This is a test block", b.block["Hash"])

    assert new_block["PrevBlockHash"] == block["Hash"]
 ```   


项目地址： https://github.com/csunny/py-bitcoin

参考教程：
* https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8