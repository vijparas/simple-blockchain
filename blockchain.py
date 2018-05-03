import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.createBlock(proof=1, previousHash='0')

    def createBlock(self, proof, previousHash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previousHash}
        self.chain.append(block)
        return block

    def getPreviousBlock(self):
        return self.chain[-1]

    def proofOfWork(self,previousProof):
        newProof=1
        checkProof=False
        while checkProof is False:
            hashOperation = hashlib.sha256(str(newProof**2-previousProof**2).encode()).hexdigest()
            if(hashOperation[:4]=='0000'):
                checkProof = True
            else:
                newProof+=1

    def hashBlock(self,block):
        encodedBlock=json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()

    def isChainValid(self,chain):
        blockIndex=1
        previousBlock=chain[0]
        while blockIndex<len(chain):
            block=chain[blockIndex]
            if block['previous_hash']!=self.hashBlock(previousBlock):
                return False
            previousProof=previousBlock['proof']
            proof=block['proof']
            hashOperation = hashlib.sha256(str(proof ** 2 - previousProof ** 2).encode()).hexdigest()
            if hashOperation[:4]!='0000':
                return False

            previousBlock=block
            blockIndex+=1

        return True





