class Solution(object):

    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        思路：
            -   第一步 将字符串化解成n个原语

                - 字符串入栈
                    - 定位每个原语的界限 每当最里面的(被消掉 就成功识别出一个原语
                        - 清空当前栈
                    - 将界限(两边的括号删除) 剩下的字符串保存到结果中

        """
        result = ""
        stack_lst = list()
        for index, node in enumerate(S):
            # 空栈的情况下 存入第一个node 即当前原语的左边界 left_point
            if not stack_lst:
                stack_lst.append(node)
                left_point = index
                continue

            if node == "(":
                stack_lst.append(node)
            else:  # node == ")" 判断能否抵消
                if len(stack_lst) != 1:
                    if stack_lst[-1] == "(":
                        stack_lst.pop(-1)  # 两两抵消
                else:  # 成功识别一个原语
                    right_point = index
                    result += S[left_point + 1:right_point]
                    stack_lst = list()  # 清空栈

        return result