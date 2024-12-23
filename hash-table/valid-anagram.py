class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return  False
        if len(s) or len(t)==0:
            return False
        
        return sorted(s)==sorted(t)
