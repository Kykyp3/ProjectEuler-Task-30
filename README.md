# ProjectEuler-Task-30
Digit fifth powers
The task seems to be easy to bruteforce, thus there is a question - where are the bounds for possible digit fifth powers numbers exist.

Whilst, f.e. in MathBlog they suggest u could see as an upper bound 9^5, what already gives you 59049 -

https://www.mathblog.dk/project-euler-30-sum-numbers-that-can-be-written-as-the-sum-fifth-powers-digits/

I wouldn't accept this logic - and could be easily checked with generating single digit numbers like 11111 or 222222.

Fifth power nine-digit 333333333 gives you "only" 1944, so it is to be proven that we couldnt come up with long numbers for the solution of the problem

def compute_bounds - > counts results within @power@ / @digit@ input 
