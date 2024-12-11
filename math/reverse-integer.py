class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        

        if x[0]=="-":
            s="-"
            for i in range(len(x)-1, 0, -1):
                s+=x[i]
            return int(s)
        min_int = -2**31
        max_int = 2**31 - 1

        # Check if the result is within the 32-bit range
        if int(x[::-1])< min_int or int(x[::-1]) > max_int:
        
            return 0
        return int(x[::-1])
            

        