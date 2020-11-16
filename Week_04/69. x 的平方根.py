#!coding:utf-8


class Solution:

    def mySqrt(self, x):
        """
        实现思路  二分查找
        :param x:
        :return:
        """

        if x == 1 or x == 0:
            return x

        # 定义左边界和右边界
        left = 1
        right = x
        mid = 1

        while left <= right:

            # 中间点 在left的中间
            mid = left + (right - left) / 2
            if (mid * mid) > x:
                right = mid - 1
            else:
                left = mid + 1

        return right


    def mySqrt2(self, x):
        """
        实现思路 牛顿迭代法
        :param x:
        :return:
        """

        if x == 1 or x == 0:
            return x

        # 定义左边界和右边界
        left = 1
        right = x
        mid = 1

        while left <= right:

            # 中间点 在left的中间
            mid = left + (right - left) / 2
            if (mid * mid) > x:
                right = mid - 1
            else:
                left = mid + 1

        return right

