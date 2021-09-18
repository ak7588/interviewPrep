"""
Matching Pairs
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.

1. if len(s) != len(t), not s, not t -> 0
2. create a dictionary to map each character of one str to another
3. compare the value of t[i]/s[i] to the mapped value from the dict
4. if they match, then increment the counter
5. return the counter

s = "abcd"
t = "adcb"

mapping_s_to_t = {a: a, b: d, c: c, d: b}
mapping_t_to_s = {a: a, d: b, c: c, b: d}
i = 3
s[i] = d
t[i] = b
matching_counter = 4

"""

def matching_pairs(s,t):
  if len(s) != len(t) or not s or not t:
    return 0
  matching_counter = 0
  mapping_s_to_t = {}
  mapping_t_to_s = {}
  for i in range(len(s)):
    if s[i] not in mapping_s_to_t:
      mapping_s_to_t[s[i]] = t[i]
    if t[i] not in mapping_t_to_s:
      mapping_t_to_s[t[i]] = s[i]
  for i in range(len(s)):
    if s[i] == mapping_t_to_s[t[i]]:
      matching_counter += 1
    elif t[i] == mapping_s_to_t[s[i]]:
      matching_counter += 1
  return matching_counter
