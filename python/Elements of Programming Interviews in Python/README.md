# Primitive Types

1. Count number of bits that are set to 1.

```python
    def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


if __name__ == "__main__":
    num = 12
    print("{0} in binary form: {0:b}".format(num))
    print(count_bits(12))
    print(count_bits(2))

```

* Integers in Python are unbounded.
* Constant `sys.maxsize` can be used to find the word-size, e.g. 2 ** 63 - 1 for a 64-bt machine.

* `sys.float_info` can be used for floats bounds.


<b> Tips & Tasks : </b>

*  Be very comfortable with the bitwise operators, particularly XOR.

* Understand how to use <b> masks </b> and create them in an machine independent way.

* Know fast ways to clear the lowermost set bit (and by extension, set the lowermost 0, get its
index, etc.).

* Understand <b> signedness </b> and its implications to shifting.

* Consider using a <b> cache </b> to accelerate operations by using it to brute-force small inputs.

* Be aware that <b> commutativity </b> and <b> associativity </b> can be used to perform operations in parallel
and reorder operations.

#### Know Your Primitive Types

* Be very familiar with the bit-wise operators such as `&` , `|` , `>>` , `<<` ,  `~` , `^` . 

* Negative numbers are treated as their 2's complement value. (There is no concept of an unsigned shift in Python, since integers have infinite precision).

* The key methods are `abs(x)` , `math.ceil(x)` , `math.floor(x)` , `min(x)` , `max(x, y)` , `power(a, b)` or `a ** b ` , `math.sqrt(num)` .

* Know how to interconvert integers and strings.

* Unlike integers, floats are not infinite precision, and it's convenient to refer to infinity as
`float('inf ')` and `float('-inf ')` . These values are comparable to integers, and can be used to create psuedo max-int and pseudo min-int.

* When comparing floating point values consider using `math.isclose()` - it is robust, e.g., when comparing very large values, and can handle both absolute and relative differences

* The key methods in random are `random.randrange(40)` , `random.randint(10, 18)` ,
`random.random()`, `random.shuffle(A)` , and `random.choice(A)` .

2. Computing the parity of the word.

    a) Brute-force Algorithm : Time Complexity : O(n)
    ```python
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
    ``` 

