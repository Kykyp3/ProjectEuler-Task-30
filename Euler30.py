# Find the sum of all the numbers that can be written as the sum of fifth powers of their digit
#  Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#

def compute_numbers(power):
    numbers = []
    for number in range(999,99999,1):
        number_lst = [int(i) for i in str(number)]
        print(number_lst)
        number_sum = 0
        for z in range(0,len(number_lst),1):
            print(number_lst[z])
            number_sum += number_lst[z]**power
            print(number_sum)
        if number_sum == number:
            numbers.append(number)
    return numbers

def compute_bounds(power,digit):
    upper_bounds = [sum(digit*10**i for i in range(1,b))+digit for b in range(1, 10)]
    upper_powers = []
    for i in range(0,len(upper_bounds)-1,1):
        bound = upper_bounds[i]
        boundpower = 0
        while bound:
            boundpower += (bound % 10)**power
            bound //= 10
        upper_powers.append(boundpower)
    return(upper_bounds,upper_powers)


if __name__=="__main__":
    print(compute_bounds(5,9))
