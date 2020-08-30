
class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height)-1
        max_value = 0

        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j-i)
                i += 1
            else:
                area = height[j] * (j-i)
                j -= 1

            max_value = max(max_value, area)

        return max_value