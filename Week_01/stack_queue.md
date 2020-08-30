## 堆栈和队列
基本概念
- FILO 先进后出
- 可以是数组、链表
- 元素是无序的

复杂度
- 添加、删除、插入O(1)
- 查询O(n)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2faa32e440a4454a0657ecb56553958~tplv-k3u1fbpfcp-zoom-1.image)


## 队列(queue)
基本概念
- FIFO 先入先出

复杂度![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64af40389c834f9d804fd3c7f0fb5f70~tplv-k3u1fbpfcp-zoom-1.image)
- 添加、删除、插入O(1)
- 查询O(n)

## 双端队列(dqueue)
- 两边都可以 出入

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9020e7fb7f2f4e69ad1a39cdf5fce3ba~tplv-k3u1fbpfcp-zoom-1.image)

## 优先队列
- 时间复杂度
	- 添加、删除、插入O(1)
	- 查询O(log n) 按照元素的优先级取出
- 底层实现机制 
	- 堆(heap)
	- 二叉搜索树 bst(binary search tree)

### 小顶堆 (Mix Heap):

- 最小的元素在堆顶 元素越小优先级越高
- 父节点要比左右孩子小

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2f6b327b5d246c98975f10f99804969~tplv-k3u1fbpfcp-zoom-1.image)

### 大顶堆(Max Heap)
- 最大的元素在堆顶 元素越大优先级越高
- 父节点要比左右孩子大

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fb2fd54cb2046f89b2590fd94af6f8f~tplv-k3u1fbpfcp-zoom-1.image)

### 二叉搜索树
- 如果任意节点的左子树不能为空, 左子树所有的节点的值 小于 根节点的值
- 如果任意节点的右子树不能为空, 右子树所有的节点的值 大于 根节点的值

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e44e0c40c2442bca94d84ead11301bb~tplv-k3u1fbpfcp-zoom-1.image)


各种数据结构和算法的时间复杂度
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c479d411d8480c97d7af63c9a8bd91~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f568a3b65b0343a2975275e06714f7d5~tplv-k3u1fbpfcp-zoom-1.image)

## 练习题
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/159263cc896643588d1188b674201f9c~tplv-k3u1fbpfcp-zoom-1.image)



## 分析Queue和PriorityQueue的源码
- 理解
- 实现原理


https://docs.python.org/zh-cn/2.7/library/collections.html

https://docs.python.org/zh-cn/2.7/library/heapq.html