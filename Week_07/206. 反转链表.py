# -*- coding: utf-8 -*-

# @File    : 206. 反转链表.py
# @Date    : 2020-10-13
# @Author  : wb-wf505100


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def reverseList(self, head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#
#     lst_stack = list()
#     tail_node = None
#     if not head.next:
#         return
#     while head.next:
#         # 记录尾节点
#         lst_stack.append(head.val)
#         if head.next:
#             head = head.next
#         else:
#             break
#
#     tail_node.next = lst_stack[-1]
#     # 将数据重新组织到新的链表
#     for index in range(len(lst_stack) - 1, -2, -1):
#         curr_node = lst_stack[index]
#         curr_node.next = lst_stack[index + 1]
#
#     return tail_node

class Solution(object):

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归
        """
        # 判断空

        # 处理逻辑

        # 下探到下一层

        # 本层数据测清理


    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # current指针指向当前节点
        current = head
        # pre指针指向上一个节点
        pre = None

        while current:
            # 临时保存当前节点的next
            tmp = current.next
            # 当前节点的next 指向上一个节点
            current.next = pre
            # current指针和pre指针 向右顺移一位
            pre = current
            current = tmp

        return pre