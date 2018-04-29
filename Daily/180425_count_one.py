def my_count_one(n):
    count = 0
    # for i in range(32):
    #     if n&1:
    #         count = count + 1
    #     n = n>>1
    if n < 0:
        n = n & 0xffffffff

    while n:
        # 消去n最后一位的1
        n = n & (n-1)
        count += 1


    return count


def f(n):
    return bin(n).count('1')

if __name__ == "__main__":
    print(my_count_one(9))

