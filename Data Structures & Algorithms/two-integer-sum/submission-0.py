class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        result = []

        for index, num in enumerate(nums):
            diff = target - num

            if hashmap.get(diff, None) is not None:
                result.append(hashmap[diff])
                result.append(index)

                break
            else:
                hashmap[num] = index

        return  result         
        