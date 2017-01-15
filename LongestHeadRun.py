"""
This is a script that contains functions which calculate properties associated
with the longest run of heads in a coin toss experiment. These functions are
implementations of the methods described in:
Schilling, Mark F. "The longest run of heads." College Math. J 21.3 (1990):
196-207.
"""
import numpy as np


def A(n, x):
    """
    Calculate the number of sequences of length n in which the longest run of
    heads does not exceed x.

    Parameters
    ----------
    n : int
        sequence length
    x : int
        longest run of heads

    Returns
    -------
    num_seq : int
        number of sequences

    Examples
    --------
    >>> number_of_sequences = A(8, 3)
    """
    num_seq = 0
    if n <= x:
        num_seq += 2**n
    else:
        nums = n - 1 - np.arange(x+1)
        for num in nums:
            num_seq += A(num, x)
    return num_seq
