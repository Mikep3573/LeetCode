def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    
    return []

if __name__ == '__main__':
    print(two_sum([3, 4, 2], 6))