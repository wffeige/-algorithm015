#!coding:utf-8
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :param nums:
        :param k:
        :return:
        思路
            - 定义两个指针 左指针i  右j
                -   间隔K个距离
                -   每次向右平移一个距离

            - 定义一个双端队列
                - 双端队列 仅存放[i, i+k]范围内的存最大的1个元素
                - j指针每次右移一个位置 将对应的元素放入双端队列
                - i指针每次右移一个位置 将i的前一个元素删除
        """
        result_lst = list()
        # 定义一个双端队列
        deque = collections.deque()
        res, n = [], len(nums)

        for j in range(n):
            i = j - k + 1

            # i指针每次右移一个位置 将i的前一个元素删除
            if i > 0 and deque[0] == nums[i-1]:
                deque.popleft()

            # 队列不为空时, 判断队列中最后面的元素 是否小于 j指针对应的元素;小于的话就删除
            while deque and deque[-1] < nums[j]:
                deque.pop()