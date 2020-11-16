# -*- coding: utf-8 -*-

# @File    : 283. 移动零.py
# @Date    : 2020-09-24
# @Author  : wb-wf505100


class Solution(object):
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        思路:
            第一次遍历
                非零的元素全部左移置 非零序列的末端(也就是指针指向的位置)
                - 每次移动一个非零元素 指针的下标+1 向右挪1位

            第二次遍历
                指针右侧的位置 全部标记成0

        """
        data_pointer = 0

        # 第一次遍历
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[data_pointer] = nums[i]
                data_pointer += 1

        # 第二次遍历
        for i in range(data_pointer, len(nums)):
            nums[i] = 0

        return nums


    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        思路：
            复杂度 O(n)
            定义
        """