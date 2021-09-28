"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Edge-cases / Questions:
- [{
- can it be empty string?
- ))))))))))

Algorithm:

1. Initialize a stack and push opening parenthesis while iterating over the str
1.1. Initialize a counter of removals
2. When seeing a closing parenthesis, pop element from the stack
3. If element is not an opening par, increment the counter of removals
4. Return the counter of removals

s = "(a(b(c)d)"
opening_stack = [0]
return_str = "a(b(c)d)"

s = "))((" // "(())"
")()"

"""

def minRemoveToMakeValid(self, s: str) -> str:
  if s == "":
    return 0
  opening_stack = []
  mismatch = []
  return_str = ""
  
  for i in range(len(s)):
    if s[i] == "(":
      opening_stack.append(i)
    if len(opening_stack) > 0:
      if char == ")": 
        opening_stack.pop()
      else:
        mismatch.append(i)
      
  mismatch = sorted(mismatch + opening_stack, reverse=True)
  for i in mistmatch:
    s = s[:i] + s[i+1:]
  return s
      
