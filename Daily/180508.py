#!/usr/bin/env python
# coding=utf-8

# 博弈的各方达到纳什均衡点 贪心算法
#####################################
# 刘备 孙策 孔明 周瑜 吕布
# 想泡五个美女
# 貂蝉 大乔 小乔 阿丑 尚香
# 五位帅哥在美女心中的位置是这样的：

# 貂蝉:  吕布 刘备 孙策 周瑜 孔明
# 大乔:  周瑜 孙策 孔明 刘备 吕布
# 小乔:  周瑜 孔明 孙策 吕布 刘备
# 尚香:  刘备 孙策 周瑜 孔明 吕布
# 阿丑:  孔明 周瑜 吕布 孙策 刘备

# 问如何匹配？
#####################################
# 将喜好转换为pandas 的 dataframe 结构
# ...
#####################################

import pandas as pd
import numpy as np


man = np.array([['貂蝉', '大乔', '小乔', '阿丑', '尚香'],
                ['貂蝉', '小乔', '大乔', '尚香', '阿丑'],
                ['阿丑', '貂蝉', '小乔', '大乔', '尚香'],
                ['小乔', '大乔', '尚香', '貂蝉', '阿丑'],
                ['小乔', '貂蝉', '大乔', '尚香', '阿丑']])

a = ['刘备', '孙策', '孔明', '周瑜', '吕布']
pdman = pd.DataFrame(man, index=a)
# print(pdman)


woman = np.array([['吕布', '刘备', '孙策', '周瑜', '孔明'],
                  ['周瑜', '孙策', '孔明', '刘备', '吕布'],
                  ['周瑜', '孔明', '孙策', '吕布', '刘备'],
                  ['刘备', '孙策', '周瑜', '孔明', '吕布'],
                  ['孔明', '周瑜', '吕布', '孙策', '刘备']])

b =  ['貂蝉', '大乔', '小乔', '尚香', '阿丑']
pdwoman = pd.DataFrame(woman, index=b)
# print(pdwoman)


def stable_marriage_match(a, pdman, pdwoman):
    sd = pd.Series()
    # print(sd)
    while len(a) > 0:
        sset = sd.index
        pp = pdman.loc[a[0]]
        for i in list(pp):
            if i in sset:
                mmm = sd[i]
                po = pdwoman.loc[i]
                kl =list(po)
                p = kl.index(mmm)
                q = kl.index(a[0])
                if p < q:
                    continue
                else:
                    sd[i] = a[0]
                    a.remove(a[0])
                    a.append(mmm)
                    break

            else:
                sd[i] = a[0]
                a.remove(a[0])
                break

    return sd


if __name__ == '__main__':
    pass
    match = stable_marriage_match(a, pdman, pdwoman)
    print(match)
