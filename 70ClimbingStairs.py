# 70. Climbing Stairs
# Hint
# You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
class Solution:
    def climbStairs(self, steps: int) -> int:
        memo = {}
        return self.memoization(steps, memo)
    
    def memoization(self, steps, memo):
        if steps < 4:
            return steps
        if steps not in memo:
            memo[steps] = self.memoization(steps-1, memo) + self.memoization(steps-2, memo)
        return memo[steps]

sol = Solution()
steps = int(input("Enter The Number Of Steps To Be Climb: "))
print(f"Number Of Ways To Climb {steps} Steps are:\t", sol.climbStairs(steps)) 