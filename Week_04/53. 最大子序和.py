# -*- coding: utf-8 -*-

# @File    : 53. 最大子序和.py
# @Date    : 2020-09-24
# @Author  : wb-wf505100

import math

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        dp[i] = nums[i] + Math.max(dp[i -1 ], 0)

        """
        # 定义最大值
        max_value = None
        # 定义sum 维护当前窗口中的总和
        sum = 0
        for i in range(len(nums)):
            if sum > 0:
                # 如果窗口总和大于0 继续添加
                sum += nums[i]
            else:
                # 如果窗口总数小于0 放弃该窗口 开启新窗口
                sum = nums[i]
            # 计算当前的最大值
            max_value = max(max_value, sum)

        return max_value