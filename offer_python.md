

1.二叉树的镜像

```
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return 
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left,root.right = root.right,root.left
```

2.链表中环的入口结点

```
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
class Solu:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead== None or pHead.next == None:
            return None
        fast = slow = pHead
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = pHead
                while(fast!=slow):
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
```

3.删除链表中重复的结点

```
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pos = pHead
        ret = ListNode(-1)
        tmp = ret
        flag = False
        while(pos and pos.next):
            if pos.val == pos.next.val:
                flag = True
                pos.next = pos.next.next
            else:
                if flag:
                    flag = False
                else:
                    tmp.next = ListNode(pos.val)
                    tmp = tmp.next
                pos = pos.next
        if pos and flag==False:
            tmp.next = ListNode(pos.val)
        return ret.next
```

4.从尾到头打印链表

```
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ret = []
        head = listNode
        while(head):
            ret.append(head.val)
            head = head.next
        ret.reverse()
        return ret
```

5.斐波那契数列

```
def fibonacci(n):
    if n == 0:
        return 0
    if n==1 or n==2:
        return 1
    memories = [1,1]
    for i in range(n-2):
        memories.append(memories[-1]+memories[-2])
    return memories[-1]
```

6.跳台阶

```
def jump_floor(number):
    # write code here
    '''
    n = 1 : 1 
    n = 2 : 1+1 = 2
    n = 3 : dp[n-2]+dp[n-1]
    '''
    if number == 1 or number == 2:
        return number
    dp = [1,2]
    for i in range(number-2):
        dp.append(dp[-1]+dp[-2])
    return dp[-1]
```

7.变态跳台阶

```
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        ret = sum_ = 3
        for i in range(number-2):
            ret = sum_+1
            sum_+=ret
        return ret 
```

8.矩形覆盖

```
class Solution:
    def rectCover(self, number):
        # write code here

        if number<=2:
            return number
        dp = [1,2]
        for i in range(number-2):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]
```

9.把字符串转换成整数

```
class Solution:
    def StrToInt(self, s):
        # write code here
        flag = True
        pos = 1
        ret = None
        if s=='':
            return 0
        for i in s:
            if i=='+' or i=='-':
                if flag:
                    pos = -1 if i=='-' else 1
                    flag = False
                else:
                    return 0
            elif i>='0' and i<='9':
                flag = False
                if ret == None:
                    ret = int(i)
                else:
                    ret = ret*10+int(i)
            else:
                return 0
        return pos*ret if ret else 0
```

10.平衡二叉树的判断

```
class Solution:
    def Treeheight(self,pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        lh = self.Treeheight(pRoot.left)
        rh = self.Treeheight(pRoot.right)
        return max(rh,lh)+1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return abs(self.Treeheight(pRoot.left)-self.Treeheight(pRoot.right))<=1
```

=======

11.和为S的连续正数序列

12.左旋转字符串

13.数字在排序数组中出现的次数

14.数组中只出现一次的数字

15.翻转单词顺序列

16.二叉树的深度

17.和为S的两个数字

18.顺时针打印矩阵

19.二叉树的下一个结点

20.对称的二叉树

=======

把二叉树打印成多行

按之字形顺序打印二叉树

序列化二叉树

二叉搜索树的第k个结点

数据流中的中位数

重建二叉树

滑动窗口的最大值

用两个栈实现队列

旋转数组的最小数字

丑数

=======

两个链表的第一个公共结点

第一个只出现一次的字符位置

数组中的逆序对

连续子数组的最大和

最小的K个数

数组中出现次数超过一半的数字

整数中1出现的次数（从1到n整数中1出现的次数）

把数组排成最小的数

数组中重复的数字

构建乘积数组

=======

二维数组中的查找

扑克牌顺子

孩子们的游戏(圆圈中最后剩下的数)

正则表达式匹配

表示数值的字符串

字符流中第一个不重复的字符

替换空格

矩阵中的路径

机器人的运动范围

求1+2+3+…+n

=======

不用加减乘除做加法

二叉搜索树与双向链表

复杂链表的复制

字符串的排列

二进制中1的个数

链表中倒数第k个结点

合并两个排序的链表

反转链表

树的子结构

数值的整数次方

=======

调整数组顺序使奇数位于偶数前面

包含min函数的栈

二叉树中和为某一值的路径

从上往下打印二叉树

二叉搜索树的后序遍历序列

栈的压入、弹出序列

