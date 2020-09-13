#!coding:utf-8

class Solution(object):
    """
    要求:
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。

    - 问题解决 终止条件
    - 处理当前逻辑 如何分成子问题(比较重要)
    - 下探到下一层 解决细分的子问题
    - 合并子问题的结果 组装到一起
    """

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def helper(index, tmp):

            # 终止条件
            if index >= len(nums):
                return tmp

            helper(index + 1, tmp + [nums[index]])

            res.append(tmp)
            helper(index + 1, tmp + [nums[index]])

        helper(0, res)
        return res



if __name__ == "__main__":
    nums = [1, 2, 3]
    res = Solution().subsets(nums)
    print(res)