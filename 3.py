'''
Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.

Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
'''


def funct():
    n = int(input('enter the number : '))
    if n % 34 == 4 and n > 4 ^ 4:
        return True
    else:
        return False


result = funct()
print(result)
