import hashingAlgorithm

class Blockchain:
    def __init__(self):
        self.chain = []
        self.blockCount = 0
    def make_Genesis(self):
        x = 1
    def getTrasnfers(self):
        a = 1
        while a == 1:
            publicA = input("what is your public key? ")
            trasnfer = input("How many cheesecoins are you transferring? ")
            publicB = input("What public key are you trasnferring to? ")
    def makeBlock(self, transfers):
        x = Block()
        self.blockChain

class  Block:
    def __init__(self):
        self.hash = 0
        self.transfer = [0, 1, 2]
        self.hashBack = 0
    def calculateHast(self):
        self.hash = 1

def getAction():
    action = int(input("What would you like to do? " + "\n"
    "1. Make a transfer " + "\n"
    "2. Calculate your balance " + "\n"
    "3. Create the next block " + "\n"
    "4. Calculate your public key " + "\n"
    "5. Validate the blockchain " + "\n"
    "6. Get the block count" + "\n"
    "> "))
    return action

chain = Blockchain()
