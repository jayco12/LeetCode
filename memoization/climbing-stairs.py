class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
    
        def climb_helper(i: int) -> int:
            if i <= 1:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = climb_helper(i - 1) + climb_helper(i - 2)
            return memo[i]
        
        return climb_helper(n)