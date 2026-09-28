class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        half = (m+n+1) // 2

        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            a_left = nums1[i-1] if i > 0 else float('-inf')
            a_right = nums1[i] if i < m else float('inf')
            b_left = nums2[j-1] if j > 0 else float('-inf')
            b_right = nums2[j] if j < n else float('inf')

            if a_left > b_right:
                hi = i - 1
            elif b_left > a_right:
                lo = i + 1
            else:
                left_max = max(a_left, b_left)
                if (m+n) % 2 == 1:
                    return left_max
                
                right_min = min(b_right, a_right)

                return float(left_max + right_min) / 2
        