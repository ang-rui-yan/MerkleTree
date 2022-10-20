from typing import List
import hashlib
from os import walk
from os.path import join
import argparse

# Create a node class
class Node:
    def __init__(self, left, right, value, fileName: str = None) -> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value
        self.fileName = fileName if fileName is not None else None

    def __str__(self) -> str:
        return str(self.value)

# Merkle Tree class
# This merkle tree implementation takes in files as input
# It outputs the hashes from all
class MerkleTree:
    # Takes in a path
    # Builds from files in the path
    def __init__(self, filePath: str) -> None:
        values = self._getAllFileContent(filePath)
        self._buildTree(values)

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
    
    def _printTreeHelper(self, node: Node):
        if node is not None:
            self._printTreeHelper(node.left)
            print(node)
            self._printTreeHelper(node.right)

    def getRootHash(self)-> str:
        return self.root.value

    # accessible without declaring
    # SHA256
    @staticmethod
    def hash(value: str) -> str:
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Compares two file system
# It determines 
# If they are the same, NOTHING happens
# Else, they search down the hashes (stored in somewhere) to find the difference
def getDifferenceInTrees(merkleTree1_filePath: str, merkleTree2_filePath: str):

    difference = []
    merkleTree1 = MerkleTree(merkleTree1_filePath)
    merkleTree2 = MerkleTree(merkleTree2_filePath)
    
    def _comparisonHelper(node1: Node, node2: Node):
        if node1 is not None or node2 is not None:
            _comparisonHelper(node1.left, node2.left)
            if node1.value != node2.value and (node1.fileName is not None and node2.fileName is not None):
                # Store in a list of differences
                difference.append([node1.fileName, node2.fileName])
            _comparisonHelper(node1.right, node2.right)

    if merkleTree1.root is None or merkleTree2.root is None:
        return None
    elif merkleTree1.root.value == merkleTree2.root.value:
        return None
    else:
        # Find the difference
        _comparisonHelper(merkleTree1.root, merkleTree2.root)
        return difference


if __name__ == '__main__':  
    parser = argparse.ArgumentParser(description='Welcome to Merkle Tree!')
    parser.add_argument("--f1", type=str, help="Enter a folder path and get the root hash")
    parser.add_argument("--f2", type=str, help="[Optional] Enter a second folder path and compare the root hash")
    
    args = parser.parse_args()

    # When there is only the second argument
    if args.f1 is None and args.f2 is not None:
        parser.error('--f1 and --f2 must be given together or use only --f1')
    # When there are both
    elif args.f1 is not None and args.f2 is not None: 
        difference = getDifferenceInTrees(args.f1, args.f2)
        print("There is no difference." if difference is None else f"Error! There are {len(difference)} different files:\n{difference}")
    # When there is only the first argument
    elif args.f1 is not None:
        mTree1 = MerkleTree(args.f1)
        print(mTree1.getRootHash())

    