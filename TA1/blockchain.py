from hash import generateHash
import json
from time import time

# Create BlockChain class

    # Define __init__() method

        # Create object variable chain and initialize it to an empty list


    # Define method createGenesisBlock()    

        # Create new object of Block class with index=0, time = time(), empty transaction. In place of hash send string "No Previous Hash Present. Since this is the first block." 

        # Append the genesisBlock to the chain


    # Define printChain method

        # Loop through each block in self.chain and print its data


class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()

    def calculateHash(self):
        blockString = str(self.index) + str(self.timestamp) + str(self.previousHash) + str(self.transaction)
        return generateHash(blockString)
    

# Create a new chain using BlockChain class


# Call createGenesisBlock() method


# Call printChain() method

