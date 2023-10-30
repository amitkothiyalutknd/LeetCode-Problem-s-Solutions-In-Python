# Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, pillars):
        maxWater = 0
        left = 0
        right = len(pillars) - 1
        while left < right:
            h = min(pillars[left], pillars[right])
            # print(h)
            w = right - left
            # print(w)
            maxWater = max(maxWater, h * w)
            # print(maxWater)
            if pillars[left] < pillars[right]:
                left += 1
            else:
                right -= 1
        return maxWater

sol = Solution()
numberOfPillar = int(input("Enter The Number Of Pillars: "))
heights = list(map(int, input(f"Enter Total {numberOfPillar} Height For {numberOfPillar} Pillars. Seperate Each Input From Single Space: ").strip().split()))[:numberOfPillar]
print(f"The Maximum Quantity Of Water With This Group Of Containers {heights} Is: ", sol.maxArea(heights))