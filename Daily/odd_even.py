def odd_even(l):
    return [i for i in l if (~i&1)] + [j for j in l if (j&1)]
    
    
# 整数list 偶数放在前面 奇数放后面
