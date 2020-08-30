## 数组、链表、跳表
概念
- 是一种线性表 数据结构 
- 内存中连续的存储区域 内存管理器直接访问 所以复杂度O(1)
- 存储相同类型的数据

复杂度
- 查找时间复杂度平均O(1)
- 插入时间复杂度平均O(n)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2916381d409244759d1aa4df6dcf02f8~tplv-k3u1fbpfcp-zoom-1.image)

## 链表
概念
- 内存地址非连续的数据结构 结点的逻辑顺序是通过指针链接实现的
- 单向链表
- 双向链表
- 循环链表
- 静态链表

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33f41355c56748d2a96d45eb5550a270~tplv-k3u1fbpfcp-zoom-1.image)


### 单向链表
仅支持单方向,每个结点包括两部分:
- next指针(指向下一个结点)
- 存储的数据

复杂度
- 插入/删除O(1)
- 查询O(n)


### 双向链表
支持双方向,每个结点包括3部分
- next指针 指向下一个结点
- prev指针 指向上一个结点
- 存储数据

复杂度
- 插入/删除O(1)
- 查询O(n)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ffa03573cee4ec8995bac62bacae40b~tplv-k3u1fbpfcp-zoom-1.image)

### 循环链表
定义:尾结点 指向 头结点;可以是单向或双向

优点: 链尾到链头方便;约瑟夫问题


### 静态链表

基本概念: 
- 用数组描述的链表
- data区域 存放数据
- cur区域(游标) 存放后继在数组中的下标


### 跳表
- 必须是有序的链表 元素必须是有序的
- 跳表对标得是平衡树和二分查找
- 时间复杂度:插入、删除、搜索都是O(log n)
- 优点: 原理简单、容易实现、方便扩展 常见的项目有 Redis、LevelDB
- 缺点: 索引的维护成本高 每次增加/删除的时候 都要更新索引数据

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b25cea37d7674454b9cd61bca04f4ee2~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e58ef8283f734dc6903110fab9cfde7d~tplv-k3u1fbpfcp-zoom-1.image)


### 相关学习文档
 https://www.jianshu.com/p/b1ab4a170c3c  <LRU缓存算法>

 https://leetcode-cn.com/problems/Iru-cache/ 

 https://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html  <跳跃表>

 https://www.geeksforgeeks.org/implementing-a-linked-list-in-java-using-class/ <Linked List 的标准实现代码>

 https://www.zhihu.com/question/20202931  <为啥 redis 使用跳表(skiplist)而不是使用 red-black？>

## 练习题

1.从尾到头打印单链表
2.单链表实现约瑟夫环(JosephCircle)
3.逆置/反转单链表
4.K个节点为一组进行翻转
5.返回链表中间(1/2)节点(扩展返回链表1/K节点)
6.单链表排序(冒泡排序&快速排序)
7.查找单链表的中间节点，要求只能遍历一次链表
8.查找单链表的倒数第K个节点，要求只能遍历一次链表
9.删除链表的倒数第K个结点
10.判断单链表是否带环?若带环，求环的长度?求环的入口点?并计算每个算法的时间复杂度&空间复杂度
11.判断两个链表是否相交，若相交，求交点(假设链表不带环)
12.判断两个链表是否相交，若相交，求交点(假设链表可能带环)
13.求两个已排序单链表中相同的数据
14.合并两个有序链表，合并后依然有序


 1. https://leetcode.com/problems/reverse-linked-list/ 
 2. https://leetcode.com/problems/swap-nodes-in-pairs 
 3. https://leetcode.com/problems/linked-list-cycle 
 4. https://leetcode.com/problems/linked-list-cycle-ii 
 5. https://leetcode.com/problems/reverse-nodes-in-k-group/
    

## python实现单向链表

参考连接https://juejin.im/post/6844903810825977869

```
# -*- coding: utf-8 -*-

# @File    : link_list.py
# @Date    : 2020-08-17
# @Author  : 


class Element(object):
    """
    元素类(叶子结点)
    """

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    """
    链表类
    """

    def __init__(self, head):
        self.head = head
        self.length = 0


    def append(self, new_node):
        """
        在链表的后面增加一个元素
        """

        # 指针从头开始 当前的头节点
        pointer = self.head

        if self.head:
            # 遍历 拿到最后一个节点
            while pointer.next:
                # 指针指向最后的尾节点
                pointer = pointer.next
            pointer.next = new_node
        else:
            self.head = new_node

        self.length += 1

    def get_position(self, index):
        """
        根据下标取数值
        第一个数值的下标为0
        :param index:
        :return:
        """
        # 异常判断: 如果下标小于0 或者大于链表长度 直接返回
        if index > self.length or index < 0:
            return None

        # 定义一个指针
        pointer = self.head
        # 定义起始查找的下标
        start_index = 0

        # 循环遍历链表 直到 start_index == index
        while pointer and start_index < index:
            pointer = pointer.next
            start_index += 1

        return pointer

    def insert(self, index, new_node):
        """
        向指定下标插入节点
        :param index:
        :param new_node:
        :return:
        """
        start_index = 0
        pointer = self.head

        if index < 0 or index > self.length:
            print "Index Error"
            return None

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        while pointer and start_index < index:

            if start_index == index -1 :
                new_node.next = pointer.next
                pointer.next = new_node
                return

            start_index += 1
            pointer = pointer.next


def main():
    innodb = LinkedList(head=Element(1))
    innodb.append(Element(3))
    innodb.append(Element(5))

    innodb.insert(6, Element("xx"))


if __name__ == '__main__':
    main()
```