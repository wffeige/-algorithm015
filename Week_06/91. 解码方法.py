#!coding:utf-8


class Solution(object):


    def numDecodings(self,s):

        length = len(s)

        # dp[i]表示s从下标[0]到[i]的方法总数
        dp = [0] * length
        dp[0] = 1 if s[0] != "0" else 0

        if length >= 2:
            # 为了方便理解初始化dp[1],也可初始化dp长度n+1来避免此步骤
            if s[1] == "0" and 0 < int(s[0]) <= 2:
                dp[1] = 1
            elif s[1] == "0":
                dp[1] = 0
            elif 10 < int(s[0] + s[1]) <= 26:
                dp[1] = 2
            else:
                dp[1] = dp[0]

        for i in range(2, length):
            # 先针对"0"字符中是否为10和20的情况进行判断
            # 再判断11-26的情况
            # 然后是其他1-9的情况
            if s[i] == "0" and 0 < int(s[i-1]) <= 2:
                dp[i] = dp[i-2]
            elif s[i] == "0":
                dp[i] = 0
            elif 10 < int(s[i-1] + s[i]) <= 26:
                dp[i] = dp[i-2] + dp[i - 1]
            else:
                dp[i] = dp[i-1]
        # print(dp)
        return dp[-1]

def main():

    data="12"
    Solution().numDecodings(data)


if __name__ == '__main__':
    main()