# 在需要低延迟和高资源效率的情况下 线程是比进程更好的解决方案

from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count


def main(use_threads=False):
    if use_threads:
        pool_cls = ThreadPool
    else:
        pool_cls = ProcessPool
        
    with pool_cls(cpu_count) as pool:
        results = pool.map(func(), args)
        
    
