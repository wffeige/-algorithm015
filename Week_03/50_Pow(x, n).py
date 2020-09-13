#!object:utf-8


class Solution:
    """
    思路:
        1. 暴力破解 循环N次 数字*N次 进行累乘

        2. 分治 log(N)
            - 转换成子问题
                - terminator
                - process(split problem )
                - dril down(sub problem)、 merge(sub result)
                - reverse states

            一分为二
                subproblem: subresult = pow(x, n/2)

                merge:
                 奇数 if n % 2 == 1 : subresult * subresult * x
                 偶数 else  subresult * subresult


    """

    def myPow(self, x, n):
        """

        :param x:
        :param n:
        :return:
        """

        def quick_pow(N):

            # 终止条件
            if N == 0:
                return 1.0

            # 细分成子任务
            half = quick_pow(N // 2)

            # 合并结果

            if N % 2 == 1:
                # 奇数次幂
                return half * half * x
            else:
                # 偶数次幂
                return half * half

        if n < 0:
            return 1/quick_pow(-n)
        else:
            return quick_pow(n)



if __name__ == "__main__":
    x = 2
    n = 10
    print(Solution().myPow(x, n))