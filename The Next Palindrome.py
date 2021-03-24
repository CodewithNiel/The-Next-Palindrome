'''
Author: Niel
Date: 23 March 2021
Purpose: Python Practice
'''

# A palindrome is a string which when reversed is itself:
# Examples
# 616, mom, 676, 100001

# input: 3
# 451
# 10
# 2133
#
# output:
# next palindrome for 451 is 454
# next palindrome for 10 is 11
# next palindrome for 2133 is 2222

def nxt_palindrome(no):
    no = no + 1
    while not is_palindrome(no):
        no+=1
    return no
def is_palindrome(no):
    return str(no) == str(no)[::-1]



if __name__ == '__main__':
    no = int(input("Enter the no of numbers you want to "
              "enter.:"))
    numbers = []

    for i in range(no):
        val = int(input("Enter the numbers:\n"))
        numbers.append(val)
    for i in range(no):
        print(f"Next palindrome for {numbers[i]} is "
        f"{nxt_palindrome(numbers[i])}")


