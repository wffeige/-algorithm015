# -*- coding: utf-8 -*-

# @File    : 11. 盛最多水的容器.py
# @Date    : 2020-09-21
# @Author  : wb-wf505100


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int


        思路:
            - 定义2个指针 left right
            - 两边分别向内收缩  left 和right比较 谁小谁向内收缩 移动到大于当前指针的点
            - 直到 left 和 right相遇

        """
        left_point = 0
        right_point = len(height)-1
        max_value = min(height[left_point], height[right_point]) * (right_point - left_point)
        while left_point < right_point:
            if height[left_point] > height[right_point]:
                current_values = min(height[left_point], height[right_point]) * (right_point - left_point)
                max_value = max(max_value, current_values)
                right_point -= 1
            else:
                current_values = min(height[right_point], height[left_point]) * (right_point - left_point)
                max_value = max(max_value, current_values)
                left_point += 1

        return max_value


if __name__ == '__main__':
    data = [1,8,6,2,5,4,8,3,7]
    print Solution().maxArea(data)