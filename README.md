# MerkleTree
Implementation of Merkle Tree as part of CS104 Mathematical Foundations of Computing's project to understand Merkle Tree.

## Implementation of Merkle Tree
Given a scenario where we have peer file systems, we need to compare if there are any changes to the files.
In this project, we embark on a merkle tree that verifies the data in file systems.

# How to use
You may use CL arguments for the following feature:

1. To get the root hash of a folder path
```
python merkleTree.py --f1 <folderpath>
```

2. To compare two folders
```
python merkleTree.py --f1 <folderpath> --f2 <folderpath>
```

# Limitations of current file system
- Slow to verify the data in the files (Running through everything)

# What is Merkle Tree?
Merkle tree is a type of full binary tree where each parent node has two children. It maintains data integrity by using hash functions.

## Hash provides quick verification
Merkle tree hashes the content of a file, meaning if there are two files with different names but same content, the hash would still be the same.
With hash, we can immediately tell if the content of two files are different.

## Tree reduces time to search where the difference is at
In a scenario where two merkle trees have differing root hashes, we can speed up the process of searching the different file contents by looking at the left and right children node hashes.
In the worst case, it gives O(log2 n) since merkle tree is a full 2-ary tree unlike an old file system where it runs through every content at O(n).
