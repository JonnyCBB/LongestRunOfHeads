import numpy as np


def A(n, x):
    num_seq = 0
    if n <= x:
        num_seq += 2**n
    else:
        nums = n - 1 - np.arange(x+1)
        for num in nums:
            num_seq += A(num, x)
    return num_seq
