"""
You've devised a simple encryption method for alphabetic strings that shuffles the characters in such a way that the resulting string is hard to quickly read,
but is easy to convert back into the original string.

Ex.: bax -> abx

left - center - right

base case: if char == "", return


"""

def encryptedWordsRecursion(s):
  if not s:
    return ""
  else:
    left = 0
    right = len(s) - 1
    mid = (left + right) // 2
    return s[mid] + s[:mid] + s[mid+1:]
  
