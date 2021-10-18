"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

[2, 7, 3, 6]

7236 +
3726
6732

[9, 9, 7, 3]

7993
9973 +
3973
9379
9793
"""

def maximumSwap(num: int) -> int:
  digits = list(map(str, list(str(num))))
  current_max = digits.copy()
  for i in range(len(digits)):
      for j in range(i + 1, len(digits)):
          digits[i], digits[j] = digits[j], digits[i]
          if int(''.join(list(map(str, digits)))) > int(''.join(list(map(str, current_max)))):
              current_max = digits.copy()
          digits[i], digits[j] = digits[j], digits[i]
  return int(''.join(list(map(str, current_max))))
