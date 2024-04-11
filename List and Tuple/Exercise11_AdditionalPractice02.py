NUMS = [[1], [1, 2, 3], [1, 2], [1, 2, 3, 4, 5], [1, 2, 3, 4]]


def nums_sum(list_of_nums):
    def get_sum(list):
        return sum(list)
    sorted_list = sorted(list_of_nums, key=get_sum)

    return sorted_list

print(nums_sum(NUMS))
