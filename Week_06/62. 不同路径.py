#!coding:utf-8


class Solution(object):

    def uniquePaths(self, m: int, n: int) -> int:
        """

        :param m:
        :param n:
        :return:
        """
        for i in range(m - 1):
            dp = [[1] * n] + [[1] + [0] * (n - 1)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


def main():
    m = 7
    n = 3
    Solution().uniquePaths(m,n)


if __name__ == '__main__':
    main()