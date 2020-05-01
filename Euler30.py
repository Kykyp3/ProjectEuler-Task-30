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

def compute_bounds(power):
    upper_bounds = [sum(9*10**i for i in range(1,b))+9 for b in range(1, 10)]
    upper_powers = []
    for i in range(0,len(upper_bounds)-1,1):
        upper_powers.append(upper_bounds[i]**power)
    print(upper_bounds,upper_powers)


if __name__=="__main__":
    print(compute_numbers(5))
