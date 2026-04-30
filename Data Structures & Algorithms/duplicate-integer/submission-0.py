class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for num in nums:
            if result.get(str(num), None):
                result[str(num)] += 1
                if result[str(num)] > 1:
                    return True
            else:
                result[str(num)] = 1
        
        return False

        