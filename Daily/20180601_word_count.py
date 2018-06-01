# 对单词的统计

def word_count(data):
    result = dict()
    for i in data:
        result[i] = result.get(i, 0) + 1
    return result
