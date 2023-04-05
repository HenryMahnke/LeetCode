class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second =1 
        for i in range(n):
            last = first + second
            first = second
            second = last
        return(second)
solution = Solution()
stairs = solution.climbStairs(10)
print(stairs)