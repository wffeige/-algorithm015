# -*- coding: utf-8 -*-

# @File    : 105.py
# @Date    : 2020-09-27
# @Author  :

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)

        return root

preorder=["E","F","H","I","G","J","K"]

inorder=["H","F","I","E","J","K","G"]
# 前序遍历 根左右	EFHIGJK
# 中序遍历 左根右	HFIEJKG
print Solution().buildTree(preorder, inorder).val

