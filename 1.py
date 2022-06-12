'''
1. Write a Python program find a list of integers with exactly two
occurrences of nineteen and at least three occurrences of five.

Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
'''

number = [19, 15, 15, 5, 3, 3, 5, 2]
number = [19, 19, 5, 5, 5, 5, 5]
number = [19, 19, 15, 5, 3, 5, 5, 2]


def funct(nums):
    count_19 = 0
    count_5 = 0

    for n in nums:
        if n == 5:
            count_5 += 1
        if n == 19:
            count_19 += 1
        if count_5 >= 3 and count_19 >= 2:
            return True
            # return False

        # else:
        #     return False
    return nums.count(19) > 2 and nums.count(5) >= 3


t = funct(number)
print(t)
