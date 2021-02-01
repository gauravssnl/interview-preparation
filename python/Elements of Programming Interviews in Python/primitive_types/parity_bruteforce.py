# Computing the parity of the word.
# The parity of a binary word is 1 if the number of 1s in the word is odd; 
# otherwise, it is 0
# Time Complexity : O(n)
def parity(x):
    result = 0 # store count of 1's in the number
    while x:
        result ^= x & 1
        x >>= 1
    return result


if __name__ == "__main__":
    num = 11
    print("num: {0} , binary: {0:b}, partity: {1}".format(num, parity(11)))

    binary_num = 10001000
    print("binary: {}, num: {} , parity: {}".format(binary_num, int(str(binary_num), 2), parity(11)))

