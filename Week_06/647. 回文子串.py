#!coding:utf-8

class Solution(object):

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 定义一个指针 遍历所有的字符串  将每个位置的字符当做回文中心扩散
        # - 以当前的节点为中心 向外扩散
        # - 以相邻的两个相同的字符串为中心 向外扩散
        length = len(s)
        # 一个字符也算是回文，所以开局count就是s中字符的数量
        count = length

        for i in range(length):

            # 如果有两个相同的字符，那么将这两个相同字符作为回文中心扩散
            if i+1 < length and s[i] == s[i+1]:
                count += 1
                # 定义两个指针 向外扩散
                left_pointer = i-1
                right_pointer = i+2
                while left_pointer >= 0 and right_pointer < length and s[left_pointer] == s[right_pointer]:
                    count += 1
                    left_pointer -= 1
                    right_pointer += 1

            # 以当前字符作为回文中心开始扩散
            left_pointer = i-1
            right_pointer = i+1
            while left_pointer >= 0 and right_pointer < length and s[left_pointer] == s[right_pointer]:
                count += 1
                left_pointer -= 1
                right_pointer += 1

        return count



def main():
    data = "abc"
    Solution().countSubstrings(data)


if __name__ == '__main__':
    main()