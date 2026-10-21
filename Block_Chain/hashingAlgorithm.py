import math
import json
import hashlib

class kjpHash():
    def __init__(self):
        self.miner = ""
        self.prevHash = ""
        self.transfers = ""
    def set_miner(self, key):
        self.miner = key
    def set_prevHash(self, prev):
        self.prevHash = prev
    def set_transfers(self, transfers):
        self.transfers = transfers
    def calc_Hash(self):
        combination = self.miner + self.transfers + self.prevHash
        bytes1 = combination.encode("utf-8")
        thisHash = hashlib.sha256(bytes1)
        return thisHash, combination

hashCreator = kjpHash()
miner = input("Who is the miner" + "\n"
              "> ")
prevHash = input("What is the previous hash" + "\n"
                 "> ")
transfers = input("What are this block's transfers?" + "\n"
                  "> ")
hashCreator.set_miner(miner + "\\")
hashCreator.set_prevHash(prevHash + "\\")
hashCreator.set_transfers(transfers)
thisHash, combination = hashCreator.calc_Hash()
print(thisHash)
print(combination)