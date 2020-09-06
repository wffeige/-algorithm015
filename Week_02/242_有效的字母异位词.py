# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表
#  👍 248 👎 0




""":cvar
# 做题4步
 1. clarification 重新确认题目信息
 2. 解决方案 选择最优
 3. 编码
 4. 解释测试用例和代码
"""


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        思路1: 排序
        思路2 hashtable 记录每个字符串中字符出现的次数
        """

        str1_dict = dict()
        for index in range(len(s)):
            if s[index] in str1_dict.keys():
                str1_dict[s[index]] += 1
            else:
                str1_dict[s[index]] = 1

        str2_dict = dict()
        for index in range(len(t)):
            if t[index] in str2_dict.keys():
                str2_dict[t[index]] += 1
            else:
                str2_dict[t[index]] = 1

        if str2_dict == str1_dict:
            return True
        else:
            return False


def main():
    s1 = "asv"
    s2 = "sva"
    print(Solution().isAnagram(s1, s2))


main()
