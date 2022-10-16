from merkleTree import MerkleTree

# Hashing content from system1
def testCase1() -> None:
    print("Test case 1:")
    mTree = MerkleTree("data/system1")
    root_hash = mTree.getRootHash()
    print("system1:", root_hash)
    print("")

# Hashing content from system1
# Hashing content from system2
# Compare the hashes manually for now
def testCase2() -> None:
    print("Test case 2:")
    mTree1 = MerkleTree("data/system1")
    root_hash1 = mTree1.getRootHash()
    print("system1:", root_hash1)

    print("")
    mTree2 = MerkleTree("data/system2")
    root_hash2 = mTree2.getRootHash()
    print("system2:", root_hash2)
    assert root_hash1 == root_hash2, "Different hash values when it should be the same"
    print("")

def testCase3() -> None:
    print("Test case 3:")
    mTree1 = MerkleTree("data/system1")
    mTree3 = MerkleTree("data/system3")

    difference = MerkleTree.getDifferenceInTrees(mTree1, mTree3)
    print(difference)
    print("")

if __name__ == "__main__":
    testCase1()
    testCase2()
    testCase3()