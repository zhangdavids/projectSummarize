import collections
import itertools
import multiprocessing


class SimpleMapReduce(object):
    def __init__(self, map_func, reduce_func=None, processes=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(processes)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        if self.reduce_func is None:
            return
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values

    # processes：源文章叫做num_worker，现在标准库这个参数已经叫做processes了，如果是None，会赋值成CPU的数量。 启动的进程数量要考虑资源竞争，对数据库的访问压力等多方面内容，有时候多了反而变慢了。
    #
    # chunksize：是每次取任务的数量，任务小的话可以一次批量的多取点。这个是经验值。
    #
    # chain表示把可迭代的对象串连起来组成一个新的大的迭代器。
    #
    # 这个SimpleMapReduce需要传递一个map函数和一个reduce函数，事实上就是执行2次self.pool.map，
    # 使用者可以忽略队列的细节（但是严重推荐看一下源码的实现），第二次直接返回结果而已。当然这个例子中reduce函数可以不设置，也就是不关心结果。