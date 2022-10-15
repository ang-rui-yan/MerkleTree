# Inspired by https://trebaud.github.io/posts/merkle-tree/

from typing import List
import hashlib

# Create a node class
class Node:
    def __init__(self, left, right, value) -> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    # accessible without declaring
    # SHA256
    @staticmethod
    def hash(value: str) -> str:
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Merkle Tree class
# This merkle tree implementation takes in files as input
# It outputs the hashes from all
class MerkleTree:
    # builds from files
    def __init__(self, files: List[str]) -> None:
        self._buildTree(files)

    # builds from hashes

    # Builds the tree
    def _buildTree(self, files: List[str]) -> None:
        if files is not None:
            leaves = []
            for leaf in files:
                # create nodes without any left and right
                leaves.append(Node(None, None, Node.hash(leaf)))
            
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
            # hash the 
            return Node(nodes[0], nodes[1], Node.hash(nodes[0].value + nodes[1].value))

        # Get all the left side at where we split the half
        left: Node = self._buildTreeHelper(nodes[:half])
        # Get all the right side at where we split the half
        right: Node = self._buildTreeHelper(nodes[half:])

        # Hash the parent of left and right
        value: str = Node.hash(left.value + right.value)

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


    # Static method that compares two file system
    # It determines 
    # If they are the same, NOTHING happens
    # Else, they search down the hashes (stored in somewhere) to find the difference

    # Searches for nodes

    # Store the hashes somewhere
    def _saveTree(self):
        pass
