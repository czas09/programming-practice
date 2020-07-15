#   Algorithms and Data Structures Outline

- - - - -

##  1 基础概念与基础工具

基础编程模型
数据抽象、抽象数据类型

### 1.1 基础编程模型

基础编程模型：描述和实现算法所用到的语言特性、软件库和操作系统特性

### 1.2 数据抽象

数据抽象、抽象数据类型（ADT）

数据类型
使用抽象数据类型：集中关注 API 描述的操作上而不会关心数据的表示
实现抽象数据类型：集中关注数据本身并将实现对该数据的各种操作

### 1.3 背包、队列和栈

基础的抽象数据类型：背包、队列、栈；及其 API 的实现：数组、变长数组、链表

背包
先进先出（FIFO）队列
下压（后进先出，LIFO）栈

API：

背包：

```Java
public class Bag<Item> implements Iterable<Item>
Bag()                  // 创建一个空背包
void add(Item item)    // 添加一个元素
boolean isEmpty()      // 判断背包是否为空
int size()             // 返回背包中的元素数量
```

背包的典型用例：

```Java
public class Stats {
    public static void main(String[] args) {
        Bag<Double> numbers = new Bag<Double>();

        while (!StdIn.isEmpty())
            numbers.add(StdIn.readDouble());
        int N = numbers.size();

        double sum = 0.0;
        for (double x : numbers)
            sum += x;
        double mean = sum / N;

        sum = 0.0;
        for (double x : numbers)
            sum += (x - mean) * (x - mean);
        double std = Math.sqrt(sum/(N-1));

        StdOut.printf("Mean: %.2f\n", mean);
        StdOut.printf("Std dev: %.2f\n", std);
    }
}
```

队列：

```Java
public class Queue<Item> implements Iterable<Item>
Queue()                    // 创建一个空队列
void enqueue(Item item)    // 添加一个元素
Item dequeue()             // 删除最早添加的元素
boolean isEmpty()          // 判断队列是否为空
int size()                 // 返回队列中的元素数量
```

队列的典型用例：

```Java
public static int[] readInts (String name) {
    In in = new In(name);
    Queue<Integer> q = new Queue<Integer>();
    while (!in.isEmpty())
        q.dequeue(in.readInt());
    
    int N = q.size();
    int[] a = new int[N];
    for (int i = 0; i < N; i++)
        a[i] = q.dequeue();
    return a;
}
```

栈：

```Java
public class Stack<Item> implements Iterable<Item>
Stack()                 // 创建一个空栈
void push(Item item)    // 添加一个元素
Item pop()              // 删除最近添加的元素
boolean isEmpty()       // 判断栈是否为空
int size()              // 返回栈中的元素数量
```

栈的典型用例：

```Java
public class Reverse {
    public static void main(String[] args) {
        Stack<Integer> stack;
        stack = new Stack<Integer>();
        while (!StdIn.isEmpty())
            stack.push(StdIn.readInt());
        
        for (int i : stack)
            StdOut.println(i);
    }
}
```

算数表达式求值：Dijkstra 双栈算法

```Java
public class Evaluate {
    public static void main(String[] args) {
        Stack<String> ops = new Stack<String>();
        Stack<Double> vals = new Stack<Double>();

        while (!StdIn.isEmpty()) {
            // 读取字符，如果是运算符则压入栈
            String s = StdIn.readString();
            if (s.equals("(")) ;
            else if (s.equals("+")) ops.push(s);
            else if (s.equals("-")) ops.push(s);
            else if (s.equals("*")) ops.push(s);
            else if (s.equals("/")) ops.push(s);
            else if (s.equals("sqrt")) ops.push(s);
            else if (s.equals(")")) {
                // 如果字符为“)”，弹出运算符和操作数，计算结果并压入栈
                String op = ops.pop();
                double v = vals.pop();
                if (op.equals("+"))      v = vals.pop() + v;
                else if (op.equals("-")) v = vals.pop() - v;
                else if (op.equals("*")) v = vals.pop() * v;
                else if (op.equals("/")) v = vals.pop() / v;
                else if (op.equals("sqrt")) v = Math.sqrt(v);
                vals.push(v);
            }   // 如果字符既非运算符也不是括号，将它作为 `double` 值压入栈
            else vals.push(Double.parseDouble(s));
        }
        StdOut.println(vals.pop());
    }
}
```

### 1.3.2 集合类数据类型的实现

定容字符串栈（fixed capacity stack of strings）
只能处理 `String` 值；
要求用例指定一个容量；
不支持迭代；

选择数据的表示方式：`FixedCapacityStackOfStrings` 选择 `String` 数组

一种表示定容字符串栈的抽象数据类型的 API：

```Java
public class FixedCapacityStackOfStrings

FixedCapacityStackOfStrings(int cap)    // 创建一个容量为 `cap` 空定容字符串栈
void push(String item)                  // 添加一个新元素
String pop()                            // 删除最近添加的元素
boolean isEmpty()                       // 判断定容字符串栈是否为空
int size()                              // 返回定容字符串栈中的元素数量
```

数据类型的实现：

```Java
public class FixedCapacityStackOfStrings {
    private String[] a;    // stack entries
    private int N;         // stack size

    public FixedCapacityStackOfStrings(int cap) {
        // 创建一个容量为 `cap` 空定容字符串栈
        a = new String[cap];
    }

    public boolean isEmpty() {
        // 判断定容字符串栈是否为空
        return N == 0;
    }

    public int size() {
        // 返回定容字符串栈中的元素数量
        return N;
    }

    public void push(String item) {
        // 添加一个新元素
        a[N++] = item;
    }

    public String pop() {
        // 删除最近添加的元素
        return a[--N];
    }
}
```

这种实现的主要性能特点是 `push` 和 `pop` 操作所需的时间独立于栈的长度
定容字符串栈的测试用例：

```Java
public static void main(String[] args) {
    FixedCapacityStackOfStrings s;
    s = new FixedCapacityStackOfStrings(100);
    while (!StdIn.isEmpty()) {
        String item = StdIn.readString();
        if (!item.equals("-")) {
            s.push(item);
        } else if (!s.isEmpty()) {
            StdOut.print(s.pop() + " ");
        }
        StdOut.println("(" + s.size() + " left on stack!");
    }
}
```

栈的性质【

泛型定容栈（fixed capacity stack）
下压（LIFO）栈（能够动态调整数组大小）（resizing array stack）

### 1.3.3 链表

结点记录
构造链表
在表头插入结点
在表尾删除结点
在表尾插入结点
其他位置的插入和删除操作
遍历
栈的实现
队列的实现
背包的实现

- - - - -

### 1.4 算法分析

算法性能、算法分析

计时器（`Stopwatch`）
表示计时器的抽象数据类型 API：

```Java
public class Stopwatch
Stopwatch()            // 创建一个计时器
double elapseTime()    // 返回对象创建以来经过的时间
```

### 1.4.3 数学模型

成本模型
得到某个程序运行时间的数学模型所需的步骤

算法分析中的常见函数
算法分析中常用的近似函数

### 1.4.4 增长数量及的分类

常数级别
对数级别
线性级别
线性对数级别
平方级别
立方级别
指数级别

### 1.4.7 对实际情况的注意事项
### 1.4.8 对于输入的依赖
### 1.4.9 内存

对象
链表
数组
字符串对象
字符串的值和子字符串

- - - - -

##  2 排序

有序地重新排列数组中的元素
插入排序、选择排序、希尔排序、快速排序、归并排序、堆排序
优先队列、选举、归并

### 2.1 初级排序算法

2.1.1 排序算法类的模板
【】
运行时间、成本模型、额外的内存使用、数据类型

2.1.2 选择排序
【】

2.1.3 插入排序
【】

2.1.4 排序算法的可视化

2.1.5 比较两种排序算法
【】

2.1.6 希尔排序
【】

### 2.2 归并排序

基于归并操作
先（递归地）将它分成两半分别排序，然后将结果归并起来
能够保证将任意长度为 $N$ 的数组排序所需时间和 $N\log N$ 成正比
所需的额外空间和 $N$ 成正比

2.2.1 原地归并的抽象方法
【】

2.2.2 自顶向下的归并排序
【】
2.2.2.1 对小规模子数组使用插入排序
2.2.2.2 测试数组是否已经有序
2.2.2.3 不将元素复制到辅助数组

2.2.3 自底向上的归并排序
【】

2.2.4 排序算法的复杂度

### 2.3 快速排序

2.3.1 基本算法
【】
【】快速排序的切分
2.3.1.1 原地切分
2.3.1.2 别越界
2.3.1.3 保持随机性
2.3.1.4 终止循环
2.3.1.5 处理切分元素值有充足的情况
2.3.1.6 终止递归

2.3.2 性能特点

2.3.3 算法改进
切换到插入排序
三取样切分
熵最优的排序
【】三项切分的快速排序

### 2.4 优先队列

2.4.1 API
【】

2.4.2 初级实现
数组实现（无序）
数组实现（有序）
链表表示法

2.4.3 堆的定义
二叉堆

2.4.4 堆的算法
由下至上的堆有序化（上浮）
由上至下的堆有序化（下沉）
【】基于堆的优先队列
多叉堆
调整数组大小
元素的不可变性
索引优先队列

2.4.5 堆排序
堆的构造
【】
下沉排序
先下沉后上浮

### 2.5 应用

指针排序
不可变的键
低成本交换
多种排序方法
多键数组
使用比较器实现优先队列
稳定性

- - - - -

##  3 查找

经典查找算法
从庞大的数据集中找到指定的条目
符号表的实现：链表（顺序查找）、有序数组（二分查找）、二叉查找树;平衡二叉查找树、散列表

符号表、字典、索引

### 3.1 符号表

简单的泛型符号表
有序的泛型符号表

3.1.4 无序链表中的顺序查找
顺序查找（基于无序链表）
【】

3.1.5 有序数组中的二分查找
二分查找（基于有序数组）
【】
基于有序数组的二分查找（迭代）

### 3.2 二叉查找树

能够将链表插入的灵活性和有序数组查找的高效性结合起来

树的术语、二叉树的术语
二叉查找树（binary search tree，BST）

利用二叉查找树实现有序符号表
【】
数据表示
查找
插入
递归
有序性相关的方法：最大键和最小键、向上取整和向下取整、选择操作、排名等；
删除最大键、删除最小键、删除操作、范围查找

### 3.3 平衡查找树

3.3.1 2-3 查找树
2-结点、3-结点

查找
向 2-结点中插入新键
向一棵只含有一个 3-结点的树中插入新键
向一个父结点为 2-结点的 3-结点中插入新键
向一个父结点为 3-结点的 3-结点中插入新键
分解根结点
局部变换
全局性质

3.3.2 红黑二叉查找树
抽象数据结构

3.3.3 实现
红黑树的插入算法
【】

3.3.4 删除操作
自顶向下的 2-3-4 树
删除最小键
删除操作

3.3.5 红黑树的性质

### 3.4 散列表

3.4.1 散列函数

3.4.2 基于拉链法的散列表
【】

3.4.3 基于线性探测法的散列表

### 3.5 应用

3.5.2 集合的 API
3.5.3 字典类用例
3.5.4 索引类用例（+反向索引、文件索引）
3.5.5 稀疏向量

- - - - -

##  4 图

对象及其之间的连接，连接可能有权重和方向
深度优先搜索、广度优先搜索、连通性问题
最小生成树：Kruskal 算法、Prim 算法
最短路径算法：Dijkstra 算法、Bellman-Ford 算法

四种最重要的图模型：
无向图（简单连接）
有向图（连接有方向性）
加权图（连接带有权值）
加权有向图（连接既有方向性又带有权值）

### 4.1 无向图

4.1.1 术语表

4.1.2 表示无向图的数据类型（API）
【】
图的几种表示方法：邻接矩阵、边的数组、邻接表数组
【】
图的处理算法

4.1.3 深度优先搜索
【】

4.1.4 寻找路径
单点路径问题
使用深度优先搜索查找图中的路径

4.1.5 广度优先搜索
单点最短路径
使用广度优先搜索查找图中的路径

4.1.6 连通分量
使用深度优先搜索找出图中的所有连通分量【】
union-find 算法

4.1.7 符号图
符号图的数据类型【】
间隔的度数【】

### 4.2 有向图

4.2.1 有向图的术语

4.2.2 有向图的数据类型 API
【】
有向图的表示：邻接表
输入格式
有向图取反
顶点的符号名：Digraph 数据类型【】 

4.2.3 有向图的可达性
单点可达性
有向图的可达性 API【】
多点可达性
有向图的可达性【】

4.2.3.1 标记-清除的垃圾清除机制

4.2.3.2 有向图的驯鹿机制
单点有向路径（depth first directed paths）
单点最短有向路径（breadth first direct paths）

4.2.4 环宇有向无环图
有向环

4.2.4.1 调度问题
优先级限制下的调度问题
拓扑排序、及其典型应用

4.2.4.2 有向图中的环
有向环检测、有向无环图（DAG）
有向环（directed cycle）的 API【】
寻找有向环【】

4.2.4.3 顶点的深度优先次序与拓扑排序
拓扑排序的 API【】
有向图中基于深度优先搜索的顶点排序【】
拓扑排序【】

4.2.5 有向图中的强连通性
强连通分量的 API【】
计算强连通分量的 Kosaraju 算法【】
顶点对的可达性 API【】

### 4.3 最小生成树

4.3.1 原理
切分原理
贪心算法

4.3.2 加权无向图的数据类型
加权边的 API【】
加权无向图（edge weighted graph）的 API【】
带权重的边的数据类型【】
加权无向图的数据类型【】

用权重来比较边
平行边、自环

4.3.3 最小生成树的 API 与测试用例
【】

4.3.4 Prim 算法

4.3.4.1 数据结构
顶点、边、横切边

4.3.4.2 维护横切边的集合
4.3.4.3 实现
4.3.4.4 运行时间
最小生成树的 Prim 算法的延时实现

4.3.5 Prim 算法的即时实现
【】

4.3.6 Kruskal 算法
最小生成树的 Kruskal 算法

4.3.7
各类最小生成树算法的性能特点【】

### 4.4 最短路径 

- - - - -

##  5 字符串

字符串处理算法
对字符串键的排序和查找的快速算法
子字符串查找、正则表达式模式匹配、数据压缩算法

- - - - -

##  6 背景

科学计算、运筹学、计算理论等