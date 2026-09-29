class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, len(nums) - 1
        pivot = 0

        while lo < hi:
            mid = (lo + hi) // 2

            # if nums[mid] < nums[hi]:
            #     hi = mid
            # elif nums[lo] < nums[mid]:
            #     lo = mid + 1
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        pivot = lo

        if nums[pivot] <= target <= nums[-1]:
            lo, high = pivot, n-1
        else:
            lo, high = 0, pivot

        while lo <= high:
            mid = (lo + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                high = mid - 1
        return -1 