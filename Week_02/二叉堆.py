#! encoding: utf-8
import sys


class BinaryHeap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # 占位
        self.Heap = [0] * (self.capacity + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, pos):
        return pos // 2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        """

        :param pos:
        :return:
        """
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        """
        交换两个下标的值
        :param fpos:
        :param spos:
        :return:
        """
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def heapifyDown(self, pos):
        """
        小顶堆的删除操作

        思路:
            - 将堆顶元素(min values)删除
            - 将堆尾元素 替换到堆顶
            - 依次和自己的儿子节点进行比较
                - 如果父节点 > 最小的儿子 则将最差的儿子节点和自己交换
                - 直到父节点 <= 最小的儿子
        :param pos:
        :return:
        """

        if not self.isLeaf(pos):

            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                # 左节点最小 则左节点和父节点进行交换
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapifyDown(self.leftChild(pos))

                # 右节点最小 则右节点和父节点进行交换
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.heapifyDown(self.rightChild(pos))


    def heapifyDown_maxheap(self, pos):
        """
        大顶堆的操作

        - 依次和自己的儿子节点进行比较
            - 如果父节点 < 最大的儿子 则将最差的儿子节点和自己交换
            - 直到父节点 >= 最大的儿子
        :param pos:
        :return:
        """

        if not self.isLeaf(pos):

            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # 左节点最大 则左节点和父节点进行交换
                if self.Heap[self.leftChild(pos)] > self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapifyDown(self.leftChild(pos))

                # 右节点最大 则右节点和父节点进行交换
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.heapifyDown(self.rightChild(pos))

    def insert(self, element):
        """
        小顶堆的插入操作
        思路
            - 新元素插入堆的尾部
            - 依次和父节点进行比较
                -   如果新元素 < 父节点 则进行交换;否则结束比较 完成插入操作
        :param element:
        :return:
        """
        # 判断是否存在溢出
        if self.size >= self.capacity:
            return

        # 堆的尾部插入新元素
        self.size += 1
        self.Heap[self.size] = element

        # 新元素的下标
        current = self.size

        # 新元素 < 父节点 则进行交换
        # 父节点下标 i -1 //2
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            # 插入元素 获取新的下标(即父节点的下标)  取整
            current = self.parent(current)

    def insert_maxheap(self, element):
        """
        大顶堆的插入操作
        思路
            - 新元素插入堆的尾部
            - 依次和父节点进行比较
                -   如果新元素 > 父节点 则进行交换;否则结束比较 完成插入操作
        :param element:
        :return:
        """
        # 判断是否存在溢出
        if self.size >= self.capacity:
            return

        # 堆的尾部插入新元素
        self.size += 1
        self.Heap[self.size] = element

        # 新元素的下标
        current = self.size

        # 新元素 > 父节点 则进行交换
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            # 插入元素 获取新的下标(即父节点的下标)
            current = self.parent(current)


    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def minHeap(self):

        for pos in range(self.size // 2, 0, -1):
            self.heapifyDown(pos)

    def delete(self):
        # 删除第一个下标(即删除最小的元素)
        popped = self.Heap[self.FRONT]

        # 将堆尾的元素 放入堆顶
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1

        # 从下标1 也就是堆顶依次进行对比操作
        self.heapifyDown(self.FRONT)
        return popped

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity


if __name__ == "__main__":
    print('The minHeap is ')
    minHeap = BinaryHeap(5)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()

    minHeap.Print()
    print("The Min val is " + str(minHeap.delete()))