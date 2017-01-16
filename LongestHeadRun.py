"""
This is a script that contains functions which calculate properties associated
with the longest run of heads in a coin toss experiment. These functions are
implementations of the methods described in:
Schilling, Mark F. "The longest run of heads." College Math. J 21.3 (1990):
196-207.
"""
import numpy as np
from scipy.special import binom
from scipy.stats import bernoulli


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


def generate_random_sequence(n, p):
    """
    Simulate a coin toss sequence by generating a set of random numbers of 1's
    and 0's from a Bernoulli distribution.

    Parameters
    ----------
    n : int
        sequence length
    p : float
        probability of a toss resulting in a head

    Returns
    -------
    sequence : list
        random sequence of coin flips

    Examples
    --------
    >>> random_sequence = generate_random_sequence(10, 0.5)
    """
    sequence = []
    nums = bernoulli.rvs(p, size=n)
    for num in nums:
        if num == 1:
            sequence.append("Head")
        else:
            sequence.append("Tails")
    return sequence


def determine_longest_run(sequence, heads_val=None, only_heads=False):
    """
    Determine the longest run of either just heads or the longest run of heads
    or tails from a list.

    Parameters
    ----------
    sequence : list
        sequence of values. There should only be 2 unique values in this list.
    heads_val : Any, optional (default=None)
        This is the value in the list that will play the part of 'heads' in a
        coin toss. E.g. it could be that the sequence given contains the
        strings: "one" and "zero". In this case we can set heads_val="one". If
        instead the list contained the integers: 1 and 0, then we could have
        heads_val=1.
    only_heads : bool, optional (default=False)
        determine whether the method should find the longest run of only the
        heads_val specified, or whether it should find the longest run of
        either heads or tails.

    Returns
    -------
    longest_run : int
        Longest run
    longest_run_value : Any
        Value for which the longest run was found. If the longest run of the
        two values was the same then both values are returned as a single
        string separated by a comma

    Examples
    --------
    >>> seq = generate_random_sequence(10, 0.5)
    >>> longest_run, longest_run_value = determine_longest_run(seq)
    """
    # Perform sanity checks. There should only be 2 unique
    sequence_set = set(sequence)
    if len(sequence_set) > 2:
        raise AssertionError("{} unique values found in the sequence.\n"
                             "There should only be 2 unique "
                             "values. ".format(len(sequence_set)))
    elif len(sequence_set) == 1:
        longest_run = len(sequence_set)
        longest_run_value = sequence.pop()
        print("There was only 1 unique value in the "
              "sequence: {}".format(longest_run_value))
        return longest_run, longest_run_value
    elif len(sequence_set) == 0:
        raise ValueError("The input sequence was empty.")

    if heads_val is None:
        heads_val = sequence_set.pop()
        if only_heads:
            print("************************ WARNING ***********************\n"
                  "The 'heads_val' wasn't set but it has been specified to\n"
                  "determine the longest run of heads. Code is running\n"
                  "assuming heads_val={}. If this isn't "
                  "correct, please run\nagain and specify "
                  "heads_val".format(heads_val))

    elif heads_val not in sequence_set:
        raise ValueError("{} is not in the {}".format(heads_val, sequence_set))
    longest_run = 0
    current_run = 0
    if only_heads:  # Find longest run of heads
        longest_run_value = heads_val
        for entry in sequence:
            if entry == heads_val:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 0
    else:  # Find longest run of heads or tails
        prev_entry = heads_val
        longest_run_value = heads_val
        for i, entry in enumerate(sequence):
            if entry == prev_entry or i == 0:
                current_run += 1
            else:
                current_run = 1
            if current_run > longest_run:
                if i == 0:
                    longest_run = current_run
                    longest_run_value = entry
                else:
                    longest_run = current_run
                    longest_run_value = prev_entry
            if current_run == longest_run:
                if longest_run_value == "":
                    longest_run_value = entry
                elif longest_run_value != entry:
                    longest_run_value = ",".join([str(longest_run_value),
                                                  str(entry)])
            prev_entry = entry
    return longest_run, longest_run_value
