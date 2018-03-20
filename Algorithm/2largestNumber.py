def find_second_large_number(array):
    tmp_list = sorted(array)
    result = tmp_list[-2]
    print(result)
    return result


if __name__ == '__main__':
    find_second_large_number([8, 7, 8, 9, 7])
