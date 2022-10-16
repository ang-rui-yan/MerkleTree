# Inspired by https://trebaud.github.io/posts/merkle-tree/

from typing import List
import hashlib
from os import walk
from os.path import join
import configparser, json

# Create a node class
class Node:
    def __init__(self, left, right, value, fileName: str = None) -> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value
        self.fileName = fileName if fileName is not None else ""

    def __str__(self) -> str:
        return str(self.value)

# Merkle Tree class
# This merkle tree implementation takes in files as input
# It outputs the hashes from all
class MerkleTree:
    # Takes in a path
    # Builds from files in the path
    def __init__(self, filePath: str, hashStoragePath: str = None) -> None:
        values = self._getAllFileContent(filePath)
        self._buildTree(values)
        if hashStoragePath is not None:
            self.hashStoragePath = hashStoragePath 
        else:
            config = configparser.ConfigParser()
            config.read('config.sys')
            self.hashStoragePath = config.get("System","HashStorage")

        self._saveRootHash(self.root.value, filePath, self.hashStoragePath)

    # Gets all the content from the files in the path
    def _getAllFileContent(self, filePath: str):
        # Get all files even in folder with full path
        onlyFiles = [join(dirpath,f) for (dirpath, dirnames, filenames) in walk(filePath) for f in filenames]

        # access all the content and store in a list
        values = []
        for file in onlyFiles:
            with open(file) as f:
                lines = str(f.readlines())
                values.append({"filename": f"{file}", "value": lines})

        return values
    
    # Builds the tree from strings of text
    def _buildTree(self, files: List[str]) -> None:
        if files is not None:
            leaves = []
            for leaf in files:
                # create nodes without any left and right
                leaves.append(Node(None, None, MerkleTree.hash(leaf["value"]), leaf["filename"]))
            
            # Merkle tree is a full binary tree
            if len(leaves) % 2 == 1:
                # Create a copy of the last element
                leaves.append(leaves[-1:][0])
            
            self.root: Node = self._buildTreeHelper(leaves)

    # Runs recursively
    def _buildTreeHelper(self, nodes: List[Node]) -> Node:
        # Half
        half: int = len(nodes) // 2

        # when we reach our base case of 2, we end the recursive
        if len(nodes) == 2:
            # Hash the parent of two leaves (at the lowest level)
            return Node(nodes[0], nodes[1], MerkleTree.hash(nodes[0].value + nodes[1].value))

        # Get all the left side at where we split the half
        left: Node = self._buildTreeHelper(nodes[:half])
        # Get all the right side at where we split the half
        right: Node = self._buildTreeHelper(nodes[half:])

        # Hash the parent of left and right
        value: str = MerkleTree.hash(left.value + right.value)

        # Top level
        return Node(left, right, value)
    
    def printTree(self):
        if self.root is not None:
            return self._printTreeHelper(self.root)
        return None
    
    def _printTreeHelper(self, node):
        if node is not None:
            self._printTreeHelper(node.left)
            print(node)
            self._printTreeHelper(node.right)

    def getRootHash(self)-> str:
        return self.root.value
        
    # Store the hashes somewhere
    def _saveRootHash(self, hash, systemName, filePath):
        # Read the data, return empty if null
        with open(filePath, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        
        # update the hashes
        with open(filePath, 'w') as f:
            data[systemName] = hash
            json.dump(data, f, indent=4)

    # accessible without declaring
    # SHA256
    @staticmethod
    def hash(value: str) -> str:
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    # Static method that compares two file system
    # It determines 
    # If they are the same, NOTHING happens
    # Else, they search down the hashes (stored in somewhere) to find the difference

    # Searches for nodes
