class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        

        if x[0]=="-":
            s="-"
            for i in range(len(x)-1, 0, -1):
                s+=x[i]
            return int(s)
        if ((-2^31) > int(x[::-1]) > (2^31) - 1) :
            return 0
        else:
            return int(x[::-1])
            

        