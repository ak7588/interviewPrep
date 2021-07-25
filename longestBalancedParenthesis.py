'''
Given a string of parentheses, find the size of the longest contiguous substring of balanced parentheses.
Parentheses are considered balanced when there is a valid closing parenthesis for an opening one.

Plan:
1. have two stacks that will keep the parenth
2. iterate through the string
  2.1. if '(' found - push to opening stack
  2.2. if ')' found - push to closing stack
3. one way to deremine if unbalanced is comparing the lengths of two stacks

(())()()(((()

(((((((( - opening
))))) - closing


'''


def longest_balanced(string):
  longestBalancedLength = 0
  opening = []
  closing = []
  for char in string:
    if char == '(':
      opening.append(char)
    elif char == ')':
      closing.append(char)
    if len(opening) == len(closing) and len(opening) != 0:
      longestBalancedLength = len(opening) + len(closing)
  return longestBalancedLength

def longest_balanced(string):
  if string = '':
      return 0
  longestBalancedLength = 0
  runningLength = 0
  for i in len(string):

      if string[i] == '(':
          runningLength += 1
      else:
          runningLength -= 1

      if runningLength < 0:
          break

      if runningLength == 0:
          longestBalancedLength = i + 1

      return longestBalancedLength
