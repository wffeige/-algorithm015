#!coding:utf-8


class Solution:

    def combine(self, n, k):
        """

        :param n:
        :param k:
        :return:
        """
        # 先生成数
        nums = [i for i in range(1, n+1)]
        # 明显用回溯法
        res = []

        def backtrace(nums_b, curr_res, index):
            if len(curr_res) == k:
                # 浅拷贝，这一步很重要
                res.append(curr_res[:])
                return

            for i in range(index, n):
                curr_res.append(nums[i])
                backtrace(nums_b[index:], curr_res, i+1)
                curr_res.pop()

        # 特殊情况处理
        if n == 0 or k == 0:
            return res

        backtrace(nums, [], 0)
        return res
