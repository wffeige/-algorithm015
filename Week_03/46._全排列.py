#!coding:utf-8


class Solution:

    def permute(self, num):
        """
        使用回溯
        :param num:
        :return:
        """
        res = []

        def backtrack(nums, tmp):
            # 中止条件
            if not nums:
                res.append(tmp)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])

        backtrack(num, [])
        return res
