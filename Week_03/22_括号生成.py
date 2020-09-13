#!coding:utf-8

from functools import lru_cache


class Solution:
    """
    思路与算法

    任何一个括号序列都一定是由 ( 开头，并且第一个 ( 一定有一个唯一与之对应的 )。这样一来，每一个括号序列可以用 (a)b 来表示，其中 a 与 b 分别是一个合法的括号序列（可以为空）。

    那么，要生成所有长度为 2 * n 的括号序列，我们定义一个函数 generate(n) 来返回所有可能的括号序列。那么在函数 generate(n) 的过程中：

    我们需要枚举与第一个 ( 对应的 ) 的位置 2 * i + 1；
    递归调用 generate(i) 即可计算 a 的所有可能性；
    递归调用 generate(n - i - 1) 即可计算 b 的所有可能性；
    遍历 a 与 b 的所有可能性并拼接，即可得到所有长度为 2 * n 的括号序列。
    为了节省计算时间，我们在每次 generate(i) 函数返回之前，把返回值存储起来，下次再调用 generate(i) 时可以直接返回，不需要再递归计算。

    """

    def generate(self, left, right, n, res):
        """

        :param left:
        :param right:
        :param n:  配额总数
        :param res:
        :return:
        """
        # 终止条件 左括号n 右括号n
        if left == right == n:
            # print(res)
            self.res_lst.append(res)
            return res

        # 处理逻辑
        if left < n:
            # 下探下一层
            self.generate(left+1, right, n, res + "(")

        # 右括号必须在左括号后面  左括号的个数 > 当前右括号的个数
        # left 上限最多到n
        if left > right:
            # 下探下一层
            self.generate(left, right+1, n, res + ")")

        # 清理操作

    def generateParenthesis(self, n):
        """

        :param n:
        :return:
        """
        self.res_lst = list()
        self.generate(left=0, right=0, n=n, res="")
        return self.res_lst


if __name__ == "__main__":
    n=3
    print(Solution().generateParenthesis(n))

