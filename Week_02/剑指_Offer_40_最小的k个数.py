#!coding:utf-8

import sys


class BinaryHeap(object):

    def __init__(self, capacity, array):

        self.capacity = capacity
        self.size = len(array)
        self.Heap = array

    def rightChild(self, pos):
        """
        获取右孩子节点的下标
        return 2i + 2
        """
        return 2 * pos + 1
        pass

    def leftChild(self, pos):
        """
        获取左孩子节点的下标
        return 2i + 1
        """
        return 2 * pos

    def parent(self, pos):
        """
        获取父节点的下标
        return i -1 // 2 取整
        """
        return (pos-1) // 2

    def swap(self, pos1, pos2):
        """

        :param pos1:
        :param pos2:
        :return:
        """
        self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1]

    def heapifyDown(self, pos):
        """
        - 删除堆顶的最小元素
        - 将堆尾的元素 插入堆顶
        - 依次向下遍历
            - 如果最小的儿子节点 < 父节点 则互相交换
            - 直到 虽小的儿子节点 >= 父节点
        :return:
        """
        print(pos)

        if self.size < pos:
            return

        while self.Heap[pos] < self.Heap[self.rightChild(pos)] or \
            self.Heap[pos] < self.Heap[self.leftChild(pos)]:
            # 如果左孩子最小
            if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                # 交换父节点 和左孩子节点的下标
                self.swap(pos, self.leftChild(pos))
                # 父节点 继续下探
                self.heapifyDown(self.leftChild(pos))
            else:
                # 交换父节点 和右孩子节点的下标
                self.swap(pos, self.rightChild(pos))
                # 父节点 继续下探
                self.heapifyDown(self.rightChild(pos))

    def delete(self):
        """
        - 删除堆顶的最小元素
        - 将堆尾的元素 插入堆顶
        - 依次向下遍历
            - 如果最小的儿子节点 < 父节点 则互相交换
            - 直到 虽小的儿子节点 >= 父节点
        :return:
        """
        # 删除堆顶的最小元素
        min_value = self.Heap[0]

        # 将堆尾的元素 插入堆顶
        self.Heap[0] = self.Heap[self.size-1]
        self.size -= 1

        # 依次向下遍历
        self.heapifyDown(0)

        return min_value


class Solution(object):

    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]

        思路1 排序 NlogN
        思路2 堆 NlogK
        思路3 快排

        """
        if len(arr) < k:
            return

        min_heap = BinaryHeap(array=arr, capacity=len(arr))

        res_lst = list()
        for i in range(k):
            min_value = min_heap.delete()
            print(min_value)
            res_lst.append(min_value)

        return res_lst


if __name__ == "__main__":
    arr = [3, 2, 1]
    k = 2
    print(Solution().getLeastNumbers(arr, k))




