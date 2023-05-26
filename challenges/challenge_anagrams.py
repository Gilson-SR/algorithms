def merge_sort(array):
    if len(array) <= 1:
        return "".join(array)

    middle = len(array) // 2
    left, right = merge_sort(array[:middle]), merge_sort(array[middle:])
    return "".join(merge(left, right, array.copy()))


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_string_sorted = merge_sort(list(first_string.lower()))
    second_string_sorted = merge_sort(list(second_string.lower()))
    boolean = first_string_sorted == second_string_sorted
    return (first_string_sorted, second_string_sorted, boolean)
