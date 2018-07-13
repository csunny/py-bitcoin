在介绍工作量证明算法之前，我们首先来回顾一下比特币白皮书（没有阅读过白皮书的同学，自己去下载阅读，地址我贴到参考目录里面了）。
比特币白皮书里讲到：

为了能够达到去中介化的目的，也就是为了实现在没有第三方参与的情况下，双方完成交易，同时又不会引起double-pay的问题。引入了两个很重要的概念，区块链与POW，pow是p2p节点之间的共识算法，大家都采用这样的一个算法来工作，谁最先达到目标，谁就获得记账的权利，就可以在链上添加数据。 下面的原版英文这里我也不翻译了，大家直接读吧，有困难的同学可以借助google translate， 毕竟现在人工智能在翻译领域已经吊炸天了。

> To implement a distributed timestamp server on a peer-to-peer basis, we will need to use a proofof-work system similar to Adam Back's Hashcash [6], rather than newspaper or Usenet posts. The proof-of-work involves scanning for a value that when hashed, such as with SHA-256, the hash begins with a number of zero bits. The average work required is exponential in the number of zero bits required and can be verified by executing a single hash. For our timestamp network, we implement the proof-of-work by incrementing a nonce in the block until a value is found that gives the block's hash the required zero bits. Once the CPU effort has been expended to make it satisfy the proof-of-work, the block cannot be changed without redoing the work. As later blocks are chained after it, the work to change the block would include redoing all the blocks after it. The proof-of-work also solves the problem of determining representation in majority decision making. If the majority were based on one-IP-address-one-vote, it could be subverted by anyone able to allocate many IPs. Proof-of-work is essentially one-CPU-one-vote. The majority decision is represented by the longest chain, which has the greatest proof-of-work effort invested in it. If a majority of CPU power is controlled by honest nodes, the honest chain will grow the fastest and outpace any competing chains. To modify a past block, an attacker would have to redo the proof-of-work of the block and all blocks after it and then catch up with and surpass the work of the honest nodes. We will show later that the probability of a slower attacker catching up diminishes exponentially as subsequent blocks are added. To compensate for increasing hardware speed and varying interest in running nodes over time, the proof-of-work difficulty is determined by a moving average targeting an average number of blocks per hour. If they're generated too fast, the difficulty increases.


ok， 那说完了pow，那怎么实现呢？   这里我们结合上一节讲到，生成一个区块，我们将hashset函数用pow来替换掉，来达到我们生成区块的目的，同时，我们进一步我们将区块链接起来，生成一条链。下面来看代码

**python 实现**
```python

import time
from consensus.proof_of_work import ProofOfWork


class Block:
    """

    Todo add index for block.

    doc  区块

    block = {
        "Timestamp": "",
        "Data": "",
        "PrevBlockHash": "",
        "Hash": "",
        "Nonce": ""
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

        pow = ProofOfWork(block)

        b_hash, nonce = pow.run()
        block["Hash"] = b_hash
        block["Nonce"] = nonce

        self.block = block
        return block

```


可以看到，这里在我们的代码中，去掉了hash_set 函数，而是采用了ProofOfWork这个类。
```python
maxNonce = 1 << 63 - 1
targetBits = 16

```

```python
import hashlib
from settings import maxNonce, targetBits


class ProofOfWork:
    """
    工作量证明算法
    """

    def __init__(self, block, nonce=0):
        self.nonce = nonce

        if not isinstance(block, dict):
            raise TypeError

        self.block = block
        self.target = 1 << (256-targetBits)

    def prepare_data(self):
        """
        准备计算的数据
        :return:
        """

        timestamp = hex(self.block["TimeStamp"])[0]

        data = "".join([
            self.block["PrevBlockHash"],
            self.block["Data"],
            timestamp,
            hex(targetBits),
            hex(self.nonce)
        ])

        return data

    def run(self):
        print("Mining  a new block...")

        hash_v = ""
        while self.nonce < maxNonce:
            data = self.prepare_data()

            hash_v = hashlib.sha256(data.encode("utf-8")).hexdigest()

            # print("-----> is mining ... %s" % hash_v)

            if int(hash_v, 16) <= self.target:
                break
            else:
                self.nonce += 1
        print("\n")

        return hash_v, self.nonce

    def validate(self):
        data = self.prepare_data()
        hash_v = hashlib.sha256(data.encode('utf-8')).hexdigest()

        print(int(hash_v, 16), self.target)

        if int(hash_v, 16) <= self.target:
            return True
        return False

```

在比特币的实现中，我们知道比特币的挖矿难度会随着算力动态的调整。 在这里我们暂时不加入难度调整，等在后面我们在加入，免得一开始搞太多东西，大家接受起来有难度。 

在ProofOfWork类中，我们实现了三个方法，prepare_data 用来准备数据，run方法是工作方法，也就是比特币挖矿时矿工工作的算法， 可以说目前的矿机的核心能力就是利用此算法生成目标的hash值。谁能在最短的时间内生成目标hash，谁就能够获得记账的权利，获得奖励。
以上就是利用工作量证明算法来生成一个block

**Go语言实现**

```

package bitcoin

import (
   "time"
   log "github.com/sirupsen/logrus"
   "crypto/sha256"
   "bytes"
)

func init()  {
   log.SetFormatter(&log.JSONFormatter{})
}

// Block represents a block in the blockchain
type Block struct {
   TimeStamp int64
   Transactions []*Transaction
   PrevBlockHash []byte
   Hash []byte
   Nonce int
}

func NewBlock(transactions []*Transaction, prewBlockHash []byte) *Block  {
   block := &Block{time.Now().Unix(), transactions,
   prewBlockHash, []byte{}, 0}

   pow := NewProofOfWork(block)
   nonce, hash := pow.Run()
   block.Hash = hash[:]
   block.Nonce = nonce
   return block
}

```

```
package bitcoin

import (
   "math/big"
   "bytes"
   "fmt"
   "math"
   "crypto/sha256"
)

const targetBits = 24

var (
   maxNonce = math.MaxInt64
)

type ProofOfWork struct {
   Block *Block
   Target *big.Int
}

func NewProofOfWork(b *Block) *ProofOfWork  {
   target := big.NewInt(1)
   target.Lsh(target, uint(256-targetBits))

   pow := &ProofOfWork{b, target}
   return pow
}

func (pow *ProofOfWork) prepareData(nonce int) []byte  {
   data := bytes.Join(
      [][]byte{
         pow.Block.PrevBlockHash,
         pow.Block.HashTransactions(),
         IntToHex(pow.Block.TimeStamp),
         IntToHex(int64(targetBits)),
         IntToHex(int64(nonce)),
      },
      []byte{},
   )
   return data
}

func (pow *ProofOfWork) Run() (int, []byte) {
   var hashInt big.Int
   var hash [32]byte

   nonce := 0

   fmt.Printf("Minning the block containning %s\n", pow.Block.Data)
   for nonce < maxNonce{
      data := pow.prepareData(nonce)
      hash = sha256.Sum256(data)

      fmt.Printf("\r%x", hash)

      hashInt.SetBytes(hash[:])

      if hashInt.Cmp(pow.Target) == -1 {
         break
      }else {
         nonce ++
      }
   }

   fmt.Print("\n\n")
   return nonce, hash[:]
}

func (pow *ProofOfWork) Validate()bool  {
   var hashInt big.Int

   data := pow.prepareData(pow.Block.Nonce)
   hash := sha256.Sum256(data)

   hashInt.SetBytes(hash[:])

   isValid := hashInt.Cmp(pow.Target) == - 1

   return isValid
}

```

项目地址： https://github.com/csunny/py-bitcoin


参考目录：
* https://bitcoin.org/bitcoin.pdf
* https://github.com/Jeiwan/blockchain_go/tree/part_5