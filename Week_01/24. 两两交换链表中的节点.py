# -*- coding: utf-8 -*-

# @File    : 24. 两两交换链表中的节点.py
# @Date    : 2020-09-21
# @Author  : wb-wf505100


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路:
        递归实现
            两两交换 新的右节点的next 指向下两个交换后的左节点
        """
        # 终止条件
        if not head.next:
            return head

        # 处理逻辑
        new_left = head.next
        new_left.next = head
        new_right = head

        # 下探到下一层
        new_right.next = self.swapPairs(new_left.next)

        # 清理操作
        return new_right


if __name__ == '__main__':
    Solution().swapPairs()
