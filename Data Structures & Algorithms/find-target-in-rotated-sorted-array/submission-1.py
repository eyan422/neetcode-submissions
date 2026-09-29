class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, len(nums) - 1
        pivot = 0

        while lo < hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        pivot = lo

        if nums[pivot] <= target <= nums[-1]:
            lo, hi = pivot, n-1
        else:
            lo, hi = 0, pivot

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1 