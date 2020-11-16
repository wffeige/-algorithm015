# -*- coding: utf-8 -*-

# @File    : 206. 反转链表.py
# @Date    : 2020-09-24
# @Author  : wb-wf505100

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    """

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路
            将元素放入stack
            然后依次读取到新
        """
        lst_stack = list()
        tail_node = None
        while head.next:
            # 记录尾节点
            tail_node = head.next
            lst_stack.append(head.val)

        tail_node.next = lst_stack[-1]
        # 将数据重新组织到新的链表
        for index in range(len(lst_stack)-1, -2, -1):
            curr_node = lst_stack[index]
            curr_node.next = lst_stack[index+1]


        return tail_node



# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

