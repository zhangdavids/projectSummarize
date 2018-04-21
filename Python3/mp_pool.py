# coding=utf-8
from mapreduce import SimpleMapReduce
from simple import FILES, file_parser


def count_err_log(item):
    word, occurances = item
    return (word, sum(occurances))


def map_wrapper(*args, **kwargs):
    matches = file_parser(*args, **kwargs)
    return [(match, 1) for match in matches]


def main():
    mapper = SimpleMapReduce(map_wrapper, count_err_log)
    log_counts = mapper(FILES)
    print(sorted(log_counts, key=lambda x: x[1], reverse=True)[0])


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print('COST: {}'.format(time.time() - start))