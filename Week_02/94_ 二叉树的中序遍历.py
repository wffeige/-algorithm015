# 给定一个二叉树，返回它的中序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表
#  👍 660 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = list()
        stack_lst = list()
        stack_lst.append(("white", root))

        while stack_lst:
            color, node = stack_lst.pop()
            if color == "white":
                # 右 中 左 插入栈
                stack_lst.append(("white", root.right))
                stack_lst.append(("white", root))
                stack_lst.append(("white", root.left))
            else:
                res.append(root.val)

        return res



