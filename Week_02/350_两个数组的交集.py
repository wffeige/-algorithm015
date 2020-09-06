#!coding:utf-8

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # 存放共同元素
        lst_set = list()

        for i in nums1:
            if not nums2:
                break
            if i in nums2:
                lst_set.append(i)
                # 删除nums2中下标最小的
                index = nums2.index(i)
                nums2.pop(index)

        return lst_set