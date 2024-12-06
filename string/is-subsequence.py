class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen = set(t)  
        t_index = 0  # Pointer for `t`
        s_index = 0  # Pointer for `s`

        # Traverse through `t` while checking characters in `s`
        while t_index < len(t) and s_index < len(s):
            if t[t_index] == s[s_index]:  # Match found
                s_index += 1  # Move `s` pointer to check the next character
            t_index += 1 
        return s_index == len(s)