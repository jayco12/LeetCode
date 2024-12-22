class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x[0]=="-":
            if int(x[1:])==int(x):
                return True
            return False
        else:
            if int(x[::-1])==int(x):
                return True
            return False