from typing import List
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:    
    sorted_arr = sorted(nums1 + nums2)
    length = len(sorted_arr)
    # print(f"length: {length}")
    if length % 2 == 0:
        lhs = sorted_arr[(length // 2) - 1]
        rhs = sorted_arr[length // 2]
        # print(f"LHS: {lhs} & RHS: {rhs}")
        return (lhs + rhs) / 2
    else:
        # TODO: Fix this
        return sorted_arr[round(length / 2) - 1]
    

nums1 = []
nums2 = [1, 2, 3, 4, 5]
print(findMedianSortedArrays(nums1, nums2))