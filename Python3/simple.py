# coding=utf-8
import glob
from collections import defaultdict

FILES = glob.glob('/mfs/dae/logs/applog/dae_applog_movie/nori/*')
RESULT = defaultdict(int)


def file_parser(filename):
    output = []
    with open(filename) as f:
        for line in f:
            words = line.split()
            if len(words) > 6 and 'stderr_log' in words[5]:
                output.append(words[6])
    return output


def main():
    for filename in FILES:
        for match in file_parser(filename):
            RESULT[match] += 1
    print(sorted(RESULT.items(), key=lambda x: x[1], reverse=True)[0])


if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print('COST: {}'.format(time.time() - start))
