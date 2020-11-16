# -*- coding: utf-8 -*-

# @File    : kaoshi2.py
# @Date    : 2020-09-27
# @Author  : wb-wf505100


class Solution:

    # def find_max_index(self, index, step):
    #     """
    #     Find the best
    #     找到当前范围内的最大下标
    #     """
    #     # 次数+1
    #     self.use_time += 1
    #
    #     # 终止条件 当前下标 + 步数可以到达终点
    #     if index + step >= len(self.nums):
    #         return
    #
    #     # 处理逻辑
    #     # 从当前可跳跃的范围内的找到最大值 并且定位下标
    #     max_value = max(nums[index: index+step])
    #     maxindex = nums.index(max_value, index, index+step)
    #     if index + max_value < len(self.nums):
    #         return self.find_max_index(maxindex, max_value)
    #
    #
    #     # 指针指向最大值的下标
    #     # 下一次探测

    def jump(self, nums):
        """
        思路:
            use_time 记录条约的次数
            pointer记录下标
        """
        step = 0
        cur_end, max_end = 0, 0

        for i, n in enumerate(nums):
            if i == cur_end + 1:
                cur_end = max_end
                step += 1

            max_end = max(max_end, i + n)

        return step

nums = []
print Solution().jump(nums)