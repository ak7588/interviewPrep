class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        1. create a stack of opening parenthesis
        2. if seeing a closed parenthesis,
        3. pop and element from the stack to check if it's equal to the closed parenthesis
        4. if not equal, return false
        5. else keep checking
        6. if all checked, return true
        """
        
        if s == "" or len(s) == 1:
            return False
        opened = []
        for char in s:
            if char in "({[":
                opened.append(char)
            else:
                if char == ')':
                    if len(opened) != 0 and opened[len(opened) - 1] == '(':
                        opened.pop()
                    else:
                        return False
                elif char == '}':
                    if len(opened) != 0 and opened[len(opened) - 1] == '{':
                        opened.pop()
                    else:
                        return False
                elif char == ']':
                    if len(opened) != 0 and opened[len(opened) - 1] == '[':
                        opened.pop()
                    else:
                        return False
        if len(opened) == 0:
            return True
        else:
            return False
            
