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