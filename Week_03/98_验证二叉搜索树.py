#!coding:utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    """
    二叉搜索树具有如下特征
        节点的左子树只包含小于当前节点的数。
        节点的右子树只包含大于当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树

    思路:
        -  1.递归
        -  2.中序遍历BST 判断元素是否递增
    """

    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            """
            判断是否是BST
            :param node:
            :param lower:
            :param upper:
            :return:
            """
            # 终止条件
            if not node:
                return True

            # 当前层判断逻辑
            val = node.val
            #  必须满足  下界限 < 当前值 < 上界限
            if val <= lower or val >= upper:
                return False

            # 下探到下一层
            # 判断右子树是否BST
            if not helper(node.right, val, upper):
                return False

            # 下探到下一层
            # 判断右子树是否BST
            if not helper(node.left, lower, val):
                return False

            # 清理条件 无
            return True

        return helper(root)


    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True



if __name__ == "__main__":


    Solution().isValidBST()

    