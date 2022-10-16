from merkleTree import MerkleTree, getDifferenceInTrees

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

    mTree2 = MerkleTree("data/system2")
    root_hash2 = mTree2.getRootHash()
    print("system2:", root_hash2)

    print("There is no difference." \
        if root_hash1 == root_hash2 else "Different hash values when it should be the same")
    print("")

# Hashing content from system1
# Hashing content from system2
# Compare the hashes manually for now
def testCase3() -> None:
    print("Test case 3:")
    mTree1 = MerkleTree("data/system1")
    root_hash1 = mTree1.getRootHash()
    print("system1:", root_hash1)

    mTree3 = MerkleTree("data/system3")
    root_hash3 = mTree3.getRootHash()
    print("system3:", root_hash3)

    print("There is no difference." \
        if root_hash1 == root_hash3 else "Different hash values")
    print("")


# Compare system1 and system2
# The result should be the same
def testCase4() -> None:
    print("Test case 4:")
    difference = getDifferenceInTrees("data/system1", "data/system2")
    print("There is no difference." if difference is None else difference)
    print("")

# Compare system1 and system3
# The result should be the different
# It will return list of list of different filename
def testCase5() -> None:
    print("Test case 5:")
    difference = getDifferenceInTrees("data/system1", "data/system3")
    print("There is no difference." if difference is None else difference)
    print("")

if __name__ == "__main__":
    testCase1()
    testCase2()
    testCase3()
    testCase4()
    testCase5()