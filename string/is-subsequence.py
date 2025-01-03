class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen = set(t)  
       
        s_index = 0 
        if len(s)==0:
            return True
        for char in t:  # Traverse through `t`
            if s_index < len(s) and char == s[s_index]:  # Check order and match
                s_index += 1
            if s_index == len(s):  # All characters in `s` matched
                return True

        # If not all characters of `s` were matched
        return False