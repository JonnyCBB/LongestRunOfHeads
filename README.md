# Longest Run Of Heads

This repository contains a list of methods which calculate properties associated
with the longest run of heads in a coin toss experiment. These functions are
implementations of the methods described in [[1]](#References)

### Installation
Currently the only way to use this package is get the code from the [Longest HeadRun.py file.](https://github.com/JonnyCBB/LongestRunOfHeads/blob/master/LongestHeadRun.py) If you use Github then you can clone the repository to obtain it by running
```
git clone https://github.com/JonnyCBB/LongestRunOfHeads.git
```
in the command prompt/terminal. Otherwise you can [fork this repository](https://help.github.com/articles/fork-a-repo/) or just copy and paste the Python code into a new .py file.

### Usage
```python
>>> import LongestHeadRun as lhr

# Find number of sequences of length 8 where the longest run of heads is 3 for
# a fair coin
>>> lhr.A_fair(8, 3)

# Calculate the probability of observing the number of sequences of length 8
# in which the longest run of heads does not exceed 3 in a coin toss sequence
# with a fair coin.
>>> lhr.prob_longest_head_run_fair(8, 3)

# Calculate the probability of observing the number of sequences of length 8
# in which the longest run of heads does not exceed 3 in a coin toss sequence
# with a biased coin. Probability of throwing heads is 0.75.
>>> lhr.prob_longest_head_run_fair(8, 3, 0.75)
```

You can generate a random coin toss sequence too.
```python
# Simulate a coin toss sequence of length 10 with probability of heads 0.5
# (e.g. a fair coin).
>>> seq = lhr.generate_random_sequence(10, 0.5)

# From the sequence determine the longest run of Heads or Tails
>>> longest_run, value = lhr.determine_longest_run(seq)

# From the sequence determine the longest run of the specified value.
>>> longest_run, value = lhr.determine_longest_run(seq, heads_val="Head", only_heads=True)
```

All methods have been thoroughly documented using the [Numpy style docstring format](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html).
So to get help just type `help(some_method)` where `some_method` is the name of a method in the file.

### References
[1] [Schilling, Mark F. "The longest run of heads." College Math. J 21.3 (1990):
196-207.](https://www.maa.org/sites/default/files/pdf/upload_library/22/Polya/07468342.di020742.02p0021g.pdf)
