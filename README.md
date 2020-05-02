# ProjectEuler-Task-30
Digit fifth powers
The task seems to be easy to bruteforce, thus there is a question - where are the bounds for possible digit fifth powers numbers exist.

We could easily find bounds using 1 and 9 digits - and see that even using only 9, the sum of powers will strongly lag behind number itself after 6-th digit

In solution - compute_bounds function returns numbers and power sums for input @power/digit@
