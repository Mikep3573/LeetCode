def two_sum(nums: list[int], target: int) -> list[int]:
    return_inds = []
    length_nums = len(nums)

    if length_nums % 2 == 0:
        nums[length_nums // 2] + two_sum(nums[length_nums // 2:], target)
    else:
        pass


    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if nums[i] + nums[j] == target and j != i:
    #             return_inds = [i, j]

    return return_inds

# print(two_sum([3, 3], 6))