# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串
#  👍 455 👎 0



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        思路:
            先排序 再hashtable

        """
        res_dict = dict()

        for line in strs:
            new_line = sorted(line)
            new_line = "".join(new_line)
            if new_line not in res_dict.keys():
                res_dict[new_line] = list()
            res_dict[new_line].append(line)

        res_lst = list()
        for value in res_dict.values():
            res_lst.append(value)

        return res_lst


def main():

    data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(data))


main()

