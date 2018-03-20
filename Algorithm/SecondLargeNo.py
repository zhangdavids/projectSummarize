def main(num_list):
    one = num_list[0]
    two = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]
        else:
            pass
    print(two)
    return two


if __name__ == '__main__':
    main([8, 7, 8, 9, 7])
