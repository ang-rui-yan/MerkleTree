# MerkleTree
Implementation of Merkle Tree as part of CS104 Mathematical Foundations of Computing's project to understand Merkle Tree

# Limitations of current file system
- Slow to verify the data in the files (Running through everything)

## What is Merkle Tree?
Merkle tree is a type of full binary tree where each parent node has two children.

## Implementation of Merkle Tree
Given a scenario where we have peer file systems, we need to compare if there are any changes to the files.
In this project, we embark on a merkle tree that verifies the data in file systems.

## Flow of the code
### Creation of a new file system
1. Retrieve all the content in the selected file system.
2. Build the Merkle Tree.
3. Recursively hash the value of the files while storing the filename in a textfile.