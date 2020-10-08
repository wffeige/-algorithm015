#!coding:utf-8


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """

        :param l1:
        :param l2:
        :return:

        思路:
            -   递归方法
            - 两两比较  修改最小的结点的next 指向 下一个结点
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2



