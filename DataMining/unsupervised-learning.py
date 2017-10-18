#! usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'john cheung, zhangjohn202@gmail.com'
__mtime__ = '2017/10/16'


# 生成数据集 均值 [10, 0] [0, 10] 方差为
# $$
#  \left[
#  \begin{matrix}
#    3 & 1 \\
#    1 & 4
#   \end{matrix}
#   \right] \tag{2}
# $$

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


np.random.seed(4711)
c1 = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
l1 = np.zeros(100)
l2 = np.ones(100)
c2 = np.random.multivariate_normal([0, 10], [[3, 1], [1, 4]], size=[100,])


# add noise
np.random.seed(1)
noise1x = np.random.normal(0, 2, 100)
noise1y = np.random.normal(0, 8, 100)
noise2 = np.random.normal(0, 8, 100)
c1[:,0] += noise1x
c1[:,1] += noise1y
c2[:,1] += noise2


fig = plt.figure(figsize=(20, 15))
ax = fig.add_subplot(111)
ax.set_xlabel('x', fontsize=30)
ax.set_ylabel('y', fontsize=30)
fig.suptitle('classes', fontsize=30)
labels = np.concatenate((l1, l2), )
X = np.concatenate((c1, c2), )
pp1 = ax.scatter(c1[:,0], c1[:,1], cmap='prism', s=50, color='r')
pp2 = ax.scatter(c2[:,0], c2[:,1], cmap='prism', s=50, color='g')

ax.legend((pp1, pp2), ('class 1', 'class 2'), fontsize=35)
fig.savefig('classes.png')

