## 说明 按照一些提交标准 需要构建Solution 的类 python2 当中不显示继承 是旧式类
### 新式类 显示继承需要加上(object)  python3 类有共同祖先object 可以隐式继承


1.二叉树的镜像（第二版第27题，递归）

```
class Solution(object):
    # 返回镜像树的根节点
    def Mirror(self, root):
        """
        交换根节点的左右子树
        交换节点值
        """
        if root == None:
            return 
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left,root.right = root.right,root.left
```

2.链表中环的入口结点（23）

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
        
class Solu(object):
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

4.从尾到头打印链表（6）

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

5.斐波那契数列（10）

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

6.跳台阶（10）

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

7.变态跳台阶（2**(n-1)）

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

8.矩形覆盖(10)

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

9.把字符串转换成整数(67)

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
        """
        二叉树的深度
        """
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        lh = self.Treeheight(pRoot.left)
        rh = self.Treeheight(pRoot.right)
        return max(rh,lh)+1

    def IsBalanced_Solution(self, pRoot):
        # write code here  之差的绝对值小于等于1
        if pRoot == None:
            return True
        return abs(self.Treeheight(pRoot.left)-self.Treeheight(pRoot.right))<=1
```

=======

11.和为S的连续正数序列

```
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        k = 2
        ret = []
        for k in range(2,tsum):
            if k%2==1 and tsum%k==0:
                tmp = []
                mid = tsum/k
                if mid-k/2>0:
                    for i in range(mid-k/2,mid+k/2+1):
                        tmp.append(i)
                    ret.append(tmp[:])
            elif k%2==0 and (tsum%k)*2==k:
                mid = tsum/k
                tmp = []
                if mid-k/2+1>0:
                    for i in range(mid-k/2+1,mid+k/2+1):
                        tmp.append(i)
                    ret.append(tmp[:])
        ret.sort()
        return ret
```

12.左旋转字符串

```
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s == '':
            return s
        n = n%len(s)
        return s[n:]+s[0:n]
```

13.数字在排序数组中出现的次数

```
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        start = 0
        end = len(data)-1
        while(start<=end):
            mid = (start+end)/2
            if data[mid]==k:
                cnt = 0
                tmp = mid
                while(tmp>=0 and data[tmp]==k):
                    cnt+=1
                    tmp-=1
                tmp = mid+1
                while(tmp<len(data) and data[tmp]==k):
                    cnt+=1
                    tmp+=1
                return cnt
            elif data[mid]>k:
                end = mid-1
            else:
                start = mid+1
        return 0
```

14.数组中只出现一次的数字

```
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans,a1,a2,flag= 0,0,0,1
        for num in array:
            ans = ans ^ num
        while(ans):
            if ans%2 == 0:
                ans = ans >>1 
                flag = flag <<1
            else:
                break
        for num in array:
            if num & flag:
                a1 = a1 ^ num
            else:
                a2 = a2 ^ num
        return a1,a2
```

15.翻转单词顺序列

```
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        ret = s.split(" ")
        ret.reverse()
        return ' '.join(ret)
```

16.二叉树的深度

```
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right==None:
            return 1
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1
```

17.和为S的两个数字

```
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        memorys= {}
        ret = []
        for num in array:
            if tsum-num in memorys:
                if ret == []:
                    ret = [tsum-num,num]
                elif ret and ret[0]*ret[1]>(tsum-num)*num:
                    ret = [tsum-num,num]
            else:
                memorys[num] = 1
        return ret
```

18.顺时针打印矩阵

```
pass
```

19.二叉树的下一个结点

```
class Solution:
    def GetNext(self, pNode):
        # write code here
        # left root right
        if pNode == None:
            return None
        if pNode.right:
            tmp = pNode.right
            while(tmp.left):
                tmp = tmp.left
            return tmp
        p = pNode.next
        while(p and p.right==pNode):
            pNode = p
            p = p.next
        return p
```

20.对称的二叉树

```
class Solution:
    def Symmetrical(self,Lnode,Rnode):
        if Lnode == None and Rnode == None:
            return True
        if Lnode and Rnode:
            return Lnode.val == Rnode.val and self.Symmetrical(Lnode.right,Rnode.left) and self.Symmetrical(Lnode.left,Rnode.right)
        else:
            return False
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.Symmetrical(pRoot.left,pRoot.right)
```

=======

21.把二叉树打印成多行

```
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack = [pRoot]
        ret = []

        while(stack):
            tmpstack = []
            tmp = []
            for node in stack:
                tmp.append(node.val)
                if node.left:
                    tmpstack.append(node.left)
                if node.right:
                    tmpstack.append(node.right)
            ret.append(tmp[:])
            stack = tmpstack[:]
        return ret
```

22.按之字形顺序打印二叉树

```
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack = [pRoot]
        step = 1
        ret = []
        while(stack):
            tmpstack = []
            tmp = []
            for node in stack:
                tmp+=[node.val]
                if node.left:
                    tmpstack.append(node.left)
                if node.right:
                    tmpstack.append(node.right)
            if step%2==0:
                tmp.reverse()
            ret.append(tmp)
            step += 1
            stack = tmpstack[:]
        return ret 
```

23.序列化二叉树

```
class Solution:
    def Serialize(self, root):
        # write code here
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def Deserialize(self, s):
        # write code here
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(s.split())
        return doit()
```

24.二叉搜索树的第k个结点

```
pass
```

25.数据流中的中位数

```
from heapq import *
class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
```

26.重建二叉树

```
class Solution(object):
    def buildTree(self, pre, tin):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if pre==[]:
            return None
        val = pre[0]
        idx = tin.index(val)
        ltin = tin[0:idx]
        rtin = tin[idx+1:]
        lpre = pre[1:1+len(ltin)]
        rpre = pre[1+len(ltin):]
        root = TreeNode(val)
        root.left = self.buildTree(lpre,ltin)
        root.right = self.buildTree(rpre,rtin)
        return root
```

27.滑动窗口的最大值

```
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0:
            return []
        ret = []
        stack = []
        for pos in range(len(num)):
            while (stack and stack[-1][0] < num[pos]):
                stack.pop()
            stack.append((num[pos], pos))
            if pos>=size-1:
                while(stack and stack[0][1]<=pos-size):
                    stack.pop(0)
                ret.append(stack[0][0])
        return ret
```

28.用两个栈实现队列

```
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if len(self.stack2):
            return self.stack2.pop()
        while(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
```

29.旋转数组的最小数字

```
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        _len = len(rotateArray)
        left = 0
        right = _len - 1
        while left <= right:
            mid = int((left + right) >> 1)
            if rotateArray[mid]<rotateArray[mid-1]:
                return rotateArray[mid]
            if rotateArray[mid] >= rotateArray[right]:
                # 说明在【mid，right】之间
                left = mid + 1
            else:
                # 说明在【left，mid】之间
                right = mid - 1
        return rotateArray[mid]
```

30.丑数(49)

只包含因子2、3和5的数称作丑数（Ugly Number），求按从小到大的顺序的第N个丑数

```
# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<1:
            return 0
        heaps = []
        heapq.heappush(heaps,1)
        lastnum = None
        idx = 1
        while(idx<=index):
            curnum = heapq.heappop(heaps)
            while(curnum==lastnum):
                curnum = heapq.heappop(heaps)
            lastnum = curnum
            idx+=1
            heapq.heappush(heaps,curnum*2)
            heapq.heappush(heaps,curnum*3)
            heapq.heappush(heaps,curnum*5)
        return lastnum
```

**********************

31.两个链表的第一个公共结点

```
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1== None or pHead2 == None:
            return None
        pa = pHead1
        pb = pHead2 
        while(pa!=pb):
            pa = pHead2 if pa is None else pa.next
            pb = pHead1 if pb is None else pb.next
        return pa
```

32.第一个只出现一次的字符位置

```
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        queue = []
        memories = dict()
        for idx,char in enumerate(s):
            if char not in memories:
                queue.append(idx)
                memories[char]=0
            memories[char]+=1
            while(queue and memories[s[queue[0]]]>1):
                queue.pop(0)
        return queue[0] if queue else -1
```

33.数组中的逆序对

```
import bisect
class Solution:
    def InversePairs(self, data):
        data.reverse()
        L = []
        ret = 0
        for d in data:
            pos = bisect.bisect_left(L,d)
            L.insert(pos,d)
            ret+= pos
            ret = ret % 1000000007
        return ret % 1000000007
```

34.连续子数组的最大和

```
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array)==1:
            return array[0]
        cur = pos = array[0]
        for i in range(1,len(array)):
            pos = max(pos+array[i],array[i])
            cur = max(cur,pos)
        return cur
```

35.最小的K个数

```
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        heaps = []
        ret = []
        for num in tinput:
            heapq.heappush(heaps,num)
        if k>len(heaps):
            return []
        for i in range(k):
            ret.append(heapq.heappop(heaps))
        return ret

```

36.数组中出现次数超过一半的数字

```
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0
        val,cnt = None,0
        for num in numbers:
            if cnt==0:
                val,cnt = num,1
            elif val == num:
                cnt+=1
            else:
                cnt-=1
        return val if numbers.count(val)*2>len(numbers) else 0
```

37.整数中1出现的次数（从1到n整数中1出现的次数）

```
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n<1:  return 0
        if n==1: return 1
        last,ans,pos = 0,0,1
        while(n):
            num = n%10
            n = n/10
            ans += pos*n
            if num>1:
                ans+=pos
            elif num==1:
                ans+=(last+1)
            last = last+num*pos
            pos*=10
        return ans
```

38.把数组排成最小的数

```
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:return ""
        numbers = list(map(str,numbers))
        numbers.sort(cmp=lambda x,y:cmp(x+y,y+x))
        return '0' if numbers[0]=='0' else ''.join(numbers)
```

39.数组中重复的数字

```
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        dup = dict()
        for num in numbers:
            if num not in dup:
                dup[num] = True
            else:
                duplication[0]=num
                return True
```

40.构建乘积数组

```
class Solution:
    def multiply(self, A):
        # write code here
        size = len(A)
        B = [1]*size
        for i in range(1,size):
            B[i] = B[i-1]*A[i-1]
        tmp = 1
        for i in range(size-2,-1,-1):
            tmp = tmp*A[i+1]
            B[i] = B[i]*tmp
        return B
```

=======

41.二维数组中的查找

```
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array)==0 or len(array[0])==0:
            return False
        i = 0
        j = len(array[0])-1
        while(i<len(array) and j>=0):
            if array[i][j]==target:
                return True
            elif array[i][j]>target:
                j-=1
            else:
                i+=1
        return False
```

42.扑克牌顺子

```
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return 0
        numbers.sort()
        zeros = numbers.count(0)
        for i, v in enumerate(numbers[:-1]):
            if v!=0:
                if numbers[i+1]==v:
                    return False
                zeros -= (numbers[i+1]-numbers[i]-1)
                if zeros<0:
                    return False
        return True
```

43.孩子们的游戏(圆圈中最后剩下的数)

```
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1: return -1
        final,start = -1,0
        cnt = [i for i in range(n)]
        while cnt:
            k = (start+m-1)%n
            final = cnt.pop(k)
            n-=1
            start = k
        return final 
```

44.正则表达式匹配

```
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def __init__(self):
        self.dic = {}
    def match(self, s, p):
        # write code here
        if (s,p) in self.dic:
            return self.dic[(s,p)]
        if p == '':
            return s==''
        if len(p)==1 or p[1]!='*':
            self.dic[(s[1:],p[1:])] = self.match(s[1:],p[1:])
            return len(s)>0 and (p[0]=='.' or p[0]==s[0]) and self.dic[(s[1:],p[1:])]
        while(len(s) and (p[0]=='.' or p[0]==s[0])):
            self.dic[(s,p[2:])] = self.match(s,p[2:])
            if self.match(s[:],p[2:]):
                return True
            s = s[1:]
        self.dic[(s,p[2:])] = self.match(s,p[2:])
        return self.dic[(s,p[2:])]
```

45.表示数值的字符串

```
pass
```

46.字符流中第一个不重复的字符

```
# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.memory = dict()
        self.queue = []

    def FirstAppearingOnce(self):
        # write code here
        while len(self.queue) and self.memory[self.queue[0]]>1:
            self.queue.pop(0)

        return self.queue[0] if len(self.queue) else '#'
    def Insert(self, char):
        # write code here
        if char not in self.memory:
            self.memory[char]=0
        self.memory[char]+=1
        if self.memory[char]==1:
            self.queue.append(char)
```

47.替换空格

```
pass
```

48.矩阵中的路径

```
pass
```

49.机器人的运动范围

```
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        memories = set()
        def dfs(i,j):
            def judge(i,j):
                return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold
            if not judge(i,j) or (i,j) in memories:
                return
            memories.add((i,j))
            if i != rows - 1:
                dfs(i + 1, j)
            if j != cols - 1:
                dfs(i, j + 1)
        dfs(0,0)
        return len(memories)
```

50.求1+2+3+…+n(不用if for while等，不循环 不递归)

```
pass
```

=======

51.不用加减乘除做加法

不计进位的和为 a^b，进位就是 a&b 
a+b = a^b + (a&b)<<1; 

```java
public class Solution {
    public int Add(int a,int b) {
        int unit = a ^ b;  
        int carry_bit = a & b;  
        while(carry_bit != 0) {  
            int temp_a = unit;  
            int temp_b = carry_bit << 1;  
            unit = temp_a ^ temp_b;  
            carry_bit = temp_a & temp_b;  
        }  
        return unit;  
    }
}
```

52.二叉搜索树与双向链表

```
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return pRootOfTree
        if pRootOfTree.left == None and pRootOfTree.right == None:
            return pRootOfTree
        left = self.Convert(pRootOfTree.left)
        p = left
        if left:
            while(p.right):
                p = p.right
            p.right = pRootOfTree
            pRootOfTree.left = p
        right = self.Convert(pRootOfTree.right)
        if right:
            pRootOfTree.right = right
            right.left = pRootOfTree
        return left if left else pRootOfTree
```

53.复杂链表的复制

```
pass
```

54.字符串的排列

```
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        def dfs(s):
            if len(s) == '':
                return []
            if len(s)==1:
                return [s]
            if len(s)==2:
                return list(set([s[0]+s[1],s[1]+s[0]]))
            ans = set([])
            left = s[0]
            right = dfs(s[1:])
            for word in right:
                for i in range(len(word)+1):
                    ans.add(word[:i]+left+word[i:])
            return list(ans)
        if ss == '':
            return []
        return sorted(dfs(ss))
```

55.二进制中1的个数

[内部链接](https://github.com/zhangdavids/workspace/blob/master/Daily/180425_count_one.py)

56.链表中倒数第k个结点

```
pass
```

57.合并两个排序的链表

```
pass
```

58.反转链表

```
pass
```

59.树的子结构

```
pass
```

60.数值的整数次方

```
"""
指数要考虑正数 负数 0
再就是正整数考虑基数和偶数 
"""
def power_common(base, exponent):
    exp = abs(exponent)
    ans = 1.0
    for i in range(0, exp):
        ans = ans * base
    return ans
        
def power_fast(base, exponent):
    result = power_common(base, exponent >> 1)
    if exponent & 1:
        return result * result * base
    else:
        return result * result
        
def power(base, exponent):
    if exponent == 0:
        return 1
    ans = power_fast(base, exponent)
    if exponent > 0:
        return ans
    else:
        return 1 / ans
    
        
def main():
    print(power(2, 9))


if __name__ == '__main__':
    main()
```

=======

61.调整数组顺序使奇数位于偶数前面

```
pass
```

62.包含min函数的栈

```
pass
```

63.二叉树中和为某一值的路径

```
pass
```

64.从上往下打印二叉树

```
pass
```

65.二叉搜索树的后序遍历序列

```
pass
```

66.栈的压入、弹出序列

```
pass
```


++++++++

:blush:

67.电梯算法

[内部连接]()

68.天平称出N个球中一个异常重量的球

[内部连接]()

69.装饰器实现记忆化

```python3.6
from functools import wraps


def memoize(function):
    @wraps(function)
    call_cache = {}
    
    def memoized(argument):
        tyr:
            return call_cache[argument]
        except KeyError:
            return calll_cache.setdefault(argument, function(argument)
            
    return memoized
    
```

实现这个记忆化的装饰器可以对比如斐波那契数列 杨辉三角等递归的 确定性缓存


