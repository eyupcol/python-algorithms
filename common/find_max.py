def find_max(number_list: list) -> int:
    """
    Find the max. number in a list
    """
    max_num = 0
    for num in number_list:
        if num > max_num:
            max_num = num
    return max_num
