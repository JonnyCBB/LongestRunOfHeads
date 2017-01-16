"""
This is a script that contains functions which calculate properties associated
with the longest run of heads in a coin toss experiment. These functions are
implementations of the methods described in:
Schilling, Mark F. "The longest run of heads." College Math. J 21.3 (1990):
196-207.
"""
import numpy as np
from scipy.special import binom


def A_fair(n, x):
    """
    Calculate the number of sequences of length n in which the longest run of
    heads does not exceed x in a coin toss sequence with a fair coin.

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
    >>> number_of_sequences = A_fair(8, 3)
    """
    num_seq = 0
    if n <= x:
        num_seq += 2**n
    else:
        for num in n - 1 - np.arange(x+1):
            num_seq += A_fair(num, x)
    return num_seq


def B_fair(n, x):
    """
    Calculate the number of sequences of length n in which the longest run of
    heads OR tails does not exceed x in a coin toss sequence with a fair coin.

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
    >>> number_of_sequences = B_fair(9, 4)
    """
    if x == 0:
        return 0
    else:
        return 2 * A_fair(n-1, x-1)


def prob_longest_head_run_fair(n, x):
    """
    Calculate the probability of observing the number of sequences of length n
    in which the longest run of heads does not exceed x in a coin toss sequence
    with a fair coin.

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
    >>> probability = prob_longest_head_run_fair(8, 3)
    """
    return float(A_fair(n, x)) / 2**n


def prob_longest_head_or_tail_run_fair(n, x):
    """
    Calculate the probability of observing the number of sequences of length n
    in which the longest run of heads OR tails does not exceed x in a coin toss
    sequence with a fair coin.

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
    >>> probability = prob_longest_head_or_tail_run_fair(9, 4)
    """
    return prob_longest_head_run_fair(n-1, x-1)


def C(n, k, x):
    """
    Calculate the number of strings of length n in which exactly k heads occur,
    but not more than x of these occur consecutively.

    Parameters
    ----------
    n : int
        sequence length
    k : int
        number of heads that occur
    x : int
        longest run of heads

    Returns
    -------
    num_strings : int
        number of strings

    Examples
    --------
    >>> number_of_strings = C(7, 5, 3)
    """
    num_strings = 0
    if k <= x:
        num_strings += binom(n, k)
    elif x < k < n:
        for k_num, n_num in zip(k - np.arange(x+1), n - 1 - np.arange(x+1)):
            num_strings += C(n_num, k_num, x)
    return int(num_strings)


def A_bias(n, x):
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
    >>> number_of_sequences = A_bias(8, 3)
    """
    num_seq = 0
    for k in np.arange(n + 1):
        num_seq += C(n, k, x)
    return num_seq


def prob_longest_head_run_bias(n, x, p):
    """
    Calculate the probability of observing the number of sequences of length n
    in which the longest run of heads does not exceed x in a coin toss sequence
    with a biased coin.

    Parameters
    ----------
    n : int
        sequence length
    x : int
        longest run of heads
    p : float
        probability of a toss resulting in a head

    Returns
    -------
    prob : float
        probability of observing the calculated number of sequences

    Examples
    --------
    >>> probability = prob_longest_head_run_bias(8, 3, 0.5)
    """
    q = 1 - p
    probability = 0
    for k in np.arange(n + 1):
        probability += C(n, k, x) * p**k * q**(n-k)
    return probability
