class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        x=str(n)
        if x[0]=="-":
            return False
        if n%4==0:
            return True
        return False