# -*- coding: utf-8 -*-

# @File    : 18.py
# @Date    : 2020-09-27
# @Author  :


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 排序
        nums.sort()
        result = list()
        #  先固定两个数 下标i和j  然后浮动两个指针 夹逼出结果
        # i 的右边必须要有3个数以上
        # j 在i的基础上 向右边界靠拢 右边至少2个数以上
        for i in range(len(nums)-3):

            for j in range(i+1, len(nums)-2):
                # 左指针从 j的右边开始
                left_point = j+1
                # 右指针 从数组的末尾开始
                right_point = len(nums)-1

                # 不停的调整两个指针 撞击结果
                while left_point < right_point:
                    # 计算当前的结果总和
                    curent_count =  nums[i] + nums[j] +nums[left_point] + nums[right_point]

                    if curent_count == target:
                        # 如果撞击成功 记录到列表
                        curent_count_lst = [ nums[i], nums[j], nums[left_point], nums[right_point] ]

                        if curent_count_lst not in result:
                            result.append(curent_count_lst)
                        # 缩小两个指针 继续撞击
                        right_point -= 1
                        left_point += 1
                    else:
                        # 如果撞击失败 调整指针 继续尝试
                        if curent_count > target:
                            # 如果当前计算结果 大于 期望值 右指针向左转移 指向更小的数
                            right_point -= 1
                        else:
                            left_point += 1

        return result





