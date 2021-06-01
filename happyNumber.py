'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

'''

'''

1. Find a way to dissect the number into its digits -> divide by 10's?
2. Convert into a string / list to get access to each digit?

'''

# My initial solution

def isHappy(self, n: int) -> bool:

    if n <= 0:
        return False

    stack = []

    while n != 1:

        while n > 0:
            stack.append(n % 10)
            n /= 10

        while len(stack) != 0:
            num = stack.pop()
            n += num**2

        if len(stack) == 0:
            return False

    return True

# Corrected solution

def isHappy(self, n: int) -> bool:
    seenNumbers = {}
    def helper(n, seenNumbers):
        seenNumbers[n] = "seen"
        currSum = 0
        for num in str(n):
            currSum += int(num)**2
        if currSum == 1:
            return True
        elif currSum in seenNumbers:
            return False
        else:
            return helper(currSum, seenNumbers)
    return helper(n, seenNumbers)
