# -*- coding: utf-8 -*-

# @File    : 191. 位1的个数.py
# @Date    : 2020-10-29
# @Author  : wb-wf505100


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        n = str(n)
        for i in range(0, len(n)):
            if n[i] == "1":
                count += 1

        return count

data = "00000000000000000000000000001011"
print Solution().hammingWeight(data)