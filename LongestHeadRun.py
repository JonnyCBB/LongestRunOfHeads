"""
This is a script that contains functions which calculate properties associated
with the longest run of heads in a coin toss experiment. These functions are
implementations of the methods described in:
Schilling, Mark F. "The longest run of heads." College Math. J 21.3 (1990):
196-207.
"""
import numpy as np


def A_fair(n, x):
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
            num_seq += A_fair(num, x)
    return num_seq


def B_fair(n, x):
    """
    Calculate the number of sequences of length n in which the longest run of
    heads OR tails does not exceed x.

    Parameters
    ----------
    n : int
        sequence length
    x : int
        longest run of heads or tails

    Returns
    -------
    num_seq : int
        number of sequences

    Examples
    --------
    >>> number_of_sequences = B(9, 4)
    """
    if x == 0:
        return 0
    else:
        return 2 * A_fair(n-1, x-1)


def prob_longest_head_run_fair(n, x):
    """
    Calculate the probability of observing the number of sequences of length n
    in which the longest run of heads does not exceed x.

    Parameters
    ----------
    n : int
        sequence length
    x : int
        longest run of heads

    Returns
    -------
    prob : float
        probability of observing the calculated number of sequences

    Examples
    --------
    >>> probability = prob_longest_head_run(8, 3)
    """
    return float(A_fair(n, x)) / 2**n


def prob_longest_head_or_tail_run_fair(n, x):
    """
    Calculate the probability of observing the number of sequences of length n
    in which the longest run of heads OR tails does not exceed x.

    Parameters
    ----------
    n : int
        sequence length
    x : int
        longest run of heads or tails

    Returns
    -------
    prob : float
        probability of observing the calculated number of sequences

    Examples
    --------
    >>> probability = prob_longest_head_or_tail_run(9, 4)
    """
    return float(B_fair(n, x)) / 2**(n-1)
