# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Example 2:
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
import sys

class Solution:
    def minCostClimbingStair(self, stairs):
        memo = [-1 for _ in range(len(stairs))]
        return min(self.solve(0, stairs, memo), self.solve(1, stairs, memo))
    
    def solve(self, step, stairs, memo):
        if (step == len(stairs)):
            return 0
        if (step > len(stairs)):
            return sys.maxsize
        if (memo[step] != -1):
            return memo[step]
        first = self.solve(step+1, stairs, memo)
        second = self.solve(step+2, stairs, memo)
        memo[step] = min(first,second) + stairs[step]
        return memo[step] 

sol = Solution()
stairs = list(map(int, input("Enter The Cost Values Inside A list. Separate Each Inputs from Single Space.: ").split(' ')))
print(f"The Minimum Cost To Reach To The Top Of Stair: {sol.minCostClimbingStair(stairs)}")