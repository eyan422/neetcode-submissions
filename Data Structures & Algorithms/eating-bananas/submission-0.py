import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = 0

        def check(speed, h):
            hours = 0
            for p in piles:
                hours += math.ceil(p/speed)
            
            return hours <= h

        while lo <= hi:
            mid = (lo+hi) // 2

            if check(mid,h):
                result = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return result
