class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        

        if x[0]=="-":
            s="-"
            for i in range(len(x)-1, 0, -1):
                s+=x[i]
            return int(s)
            
        return int(x[::-1])

        