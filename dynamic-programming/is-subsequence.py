class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen=set(t)

        for i in range(len(s)):
            if s[i] not in seen:
                return False
        return True
