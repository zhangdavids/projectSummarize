## 算法综述


十大算法提升自我

+ 快速排序 东尼 霍尔 使用分治来把一个串行分为两个子串行
+ 堆排序 利用堆这种数据结构所设计的算法
+ 归并排序
+ 二分查找算法
+ 线性查找算法 BFPRT
+ 深度优先搜索
+ 广度优先搜索
+ dijkstra算法
+ 动态规划
+ 朴素贝叶斯分类算法


二分查找

插入排序

+ 直接插入排序
+ 希尔排序
+ 二分法插入排序

选择排序

+ 直接选择排序
+ 堆排序

交换排序

+ 冒泡排序
+ 快速排序
+ 侏儒排序或者叫stupid sort（2000，Hamid）

______

+ 归并排序
+ 基数排序


list-sort.py 列表的sort排序方法

tree 树

graph 图


排序算法的时间复杂度和空间复杂度:   



|算法名称  |  时间最好 |   最坏  |    平均 | 空间|  
|:--  | :--   | :--     |   :--            |:--  |  
|直接插入  |n   |  n<sup>2</sup>  |   n<sup>2</sup>           | |  
| 希尔 |n   |  n<sup>2</sup>    |    nlog<sub>2</sub>n          | |  
| 直接选择 | n<sup>2</sup>  |  n<sup>2</sup>    |   n<sup>2</sup>            | |  
| 堆 | nlog<sub>2</sub>n   |  nlog<sub>2</sub>n    |   nlog<sub>2</sub>n            | |  
| 冒泡 | n  |  n<sup>2</sup>    |     n<sup>2</sup>          | |  
| 快排 | nlog<sub>2</sub>n   | n<sup>2</sup>     |     nlog<sub>2</sub>n          | |  
| 归并 |  nlog<sub>2</sub>n  |  nlog<sub>2</sub>n    |  nlog<sub>2</sub>n             | |  
| 基数 | d(n+r)  |  d(n+r)    |  d(n+r)             | |  
|侏儒  | n  | n<sup>2</sup>     |              | |  
|timsort  |   |     |              | |  



