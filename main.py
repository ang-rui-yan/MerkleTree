from merkleTree import MerkleTree

def testCase1() -> None:
    print("Test case 1:")
    elements = ["Hello", "World", "From Merkle"]
    mTree = MerkleTree(elements)
    root_hash = mTree.getRootHash()
    print(root_hash)
    print("")

def testCase2() -> None:
    print("Test case 2:")
    elements = ["Hello", "World", "From Merkle 2"]
    mTree = MerkleTree(elements)
    root_hash = mTree.getRootHash()
    print(root_hash)
    print("")

if __name__ == "__main__":
    testCase1()
    testCase2()