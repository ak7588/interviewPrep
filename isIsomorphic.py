class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for c1, c2 in zip(s,t):
            if c1 not in dict_s and c2 not in dict_t:
                dict_s[c1] = c2
                dict_t[c2] = c1
            elif dict_s.get(c1) != c2 or dict_t.get(c2) != c1:
                return False
        return True
                    
