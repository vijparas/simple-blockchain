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

