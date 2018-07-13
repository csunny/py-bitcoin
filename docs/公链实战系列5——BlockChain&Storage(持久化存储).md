如果前面大家有认真看这个系列的教程，相信到这里大家对于区块链已经有了自己的理解与认识，今天我们重要要生成一条链了，大家是不是很激动，有没有很开心？ 

今天我们来生成一条真正的链，本来今天的内容在区块链的角度来讲应该是比较简单的，只要把一个Block链接起来就生成一个BlockChain了，本来打算把下一节API层的知识也放到这里来一起讲的，后来想了想，其实Storage这里面又有很多东西，所以API层的东西，还是放在下一节，单独拿出来讲一讲，这样也能多讲点东西。

Ok，话不多说，直接上代码:
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from core.blockchain.block import Block
from consensus.proof_of_work import ProofOfWork


class BlockChain:
    """
    doc New blockchain
    """

    def __init__(self):
        # At first storage blocks in a memory list
        # and then we storage this in redis
        
        self.blocks = []

    def add_block(self, data):

        if self.blocks.get('l'):
            # there we should mark last block hash to create a new block.
            # in the redis the l is the last block hash value key.
            last_block = self.blocks[-1]
            b = Block()

            new_block = b.new_block(data, last_block["Hash"])

            pow = ProofOfWork(new_block, new_block["Nonce"])

            if pow.validate():
                self.blocks.append(new_block)

        else:
            b = Block()
            new_block = b.new_block(data)

            pow = ProofOfWork(new_block, new_block["Nonce"])
            if pow.validate():
                self.blocks.append(new_block)

    def print_blockchain(self):
        """
        输出blockchain

        :return:
        """
        for b in self.blocks:
            print(b)
        
```

**测试代码**

```python

from core.blockchain.blockchain import BlockChain


if __name__ == '__main__':
    bc = BlockChain()

    for i in range(10):
        bc.add_block("Magic Test %d" %i)

    bc.print_blockchain()
    
```    

看了代码之后是不是觉得很简单？ 是的，在这里我们只用了一个BlockChain的类就实现了创建一条区块链，在类里也只有一个核心的方法，那几是add_block，我们通过add_block 将每一个block添加到链上，并存储在内存中。这样我们就实现了一个链。 但是这里有个问题，有个非常大的问题，具体是什么问题呢？  大家可以先想想。


没错，我们实际中不可能将数据存储到内存当中，因为一旦我们服务重启或者机器down机，那数据就全没有了，所以我们需要对数据进行持久化，持久化的目的就是在我们下一次重新启动服务的时候，还可以加载之前的数据，就像开篇在架构介绍的时候说的一样，数据存储是一个非常，非常，非常重要的步骤，我们一定要重视，在这里为了方便，我仅仅采用k-v数据库redis对数据进行了存储。当然redis也是一个内存数据库， 虽然它有数据出久化的方案，但实际生产中，还是建议大家直接放到磁盘中，所谓落袋为安。另外如果有条件，做好数据备份那就更好了。

这里为了简单，不让大家陷入繁杂的软件安装与配置的细枝末节之中，我用docker起了一个redis，操作步骤如下：

#### 首先拉去redis镜像

> docker pull redis.   

#### 编写docker-compose.yaml文件
```python
version: "2"
services:
  db:
    image: redis
    ports:
      - "6379:6379"

```

#### 启动redis 容器
> docker-compose up -d

#### 检查容器是否启动成功

> docker ps -a


如果终端有如图所示，说明你的redis-container已经成功启动了，接下类，就可以快乐的写代码了

首先我们对redis进行一个简单的封装，方便我们后续直接使用：

**python代码**
```python

#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/11 
"""

import redis


class Redis:
    """

    """

    settings = {
        "host": "localhost",
        "port": 6379,
        "db": 0
    }

    def __init__(self, config=None):
        self.config = config if config else self.settings

        self.rds = redis.StrictRedis(**self.config)

    def get(self, key):
        return self.rds.get(key)

    def set(self, key, value):
        self.rds.set(key, value)

    def remove(self, key):
        self.rds.delete(key)

    def keys(self):
        return self.rds.keys()

    @property
    def empty(self):
        return self.rds.dbsize() == 0

```

# 测试代码

```python

#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/7/11 
"""

from storage.redis_storage import Redis


if __name__ == '__main__':
    r = Redis()

    r.set('magic', {"index": 1, "sex": "男", "age": 18})

    # print(r.get("magic").decode())
    #
    # print(r.rds.keys())

    for k in r.keys():
        print(r.get(k).decode())

    # r.remove("magic")
    # print(r.get("magic"))

```

ok， redis封装好之后，我们来修改以下我们之前的链生产的代码，把数据存储到redis里面，而不是直接放到内存数据里。 


```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This Document is Created by  At 2018/6/29

- 该模块用于生成区块链，区块形式格式如下
"""
import json
from storage.redis_storage import Redis
from core.blockchain.block import Block
from consensus.proof_of_work import ProofOfWork


class BlockChain:
    """
    doc New blockchain
    """

    def __init__(self):
        # At first storage blocks in a memory list
        # and then we storage this in redis
        # self.blocks = []

        self.blocks = Redis()

    def add_block(self, data):

        if self.blocks.get('l'):
            # there we should mark last block hash to create a new block.
            # in the redis the l is the last block hash value key.
            last_hash = self.blocks.get('l').decode()
            b = Block()

            new_block = b.new_block(data, last_hash)

            pow = ProofOfWork(new_block, new_block["Nonce"])

            if pow.validate():
                # self.blocks.append(new_block)

                self.blocks.set(new_block["Hash"], new_block)
                self.blocks.set("l", new_block["Hash"])

        else:
            b = Block()
            new_block = b.new_block(data)

            pow = ProofOfWork(new_block, new_block["Nonce"])
            if pow.validate():
                # self.blocks.append(new_block)
                self.blocks.set(new_block["Hash"], new_block)
                self.blocks.set("l", new_block["Hash"])

    def print_blockchain(self):
        """
        输出blockchain

        :return:
        """
        # for b in self.blocks:
        #     print(b)

        blocks = []

        for b in self.blocks.keys():

            if b.decode() != 'l':
                v = self.blocks.get(b).decode()
                blocks.append(eval(v))
        return blocks
```

好了，到这里我们的工作就告一段落了，我们成功的生产了一条链，我们用到了hash函数、用到了pow算法、用到了docker、用到了redis、还认识了区块链这种特殊的链表结构。突然感觉还是挺多内容的，相信大家需要好好消化消化，所以在下一节中，我们谈一谈在架构设计里面最上面的那一层，也就是API层，API层相对来说比较传统，在API层里，我们详细介绍下，怎么浏览我们的区块、如何浏览我们的链。 嗯，你可以认为它就是一个区块浏览器。 下一节如果可能，嗯，我是说如果，我会稍微讲一讲关于框架开发，以及中间件开发的一些内容，当然了，篇幅所限，另外也不是本系列教程的重点，所以肯定不会很深。 希望大家学的愉快，有问题随时与我探讨。


项目地址：  https://github.com/csunny/py-bitcoin


参考教程：
* https://www.docker.com/