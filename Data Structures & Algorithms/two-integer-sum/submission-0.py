class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapAntigo = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapAntigo:
                return [mapAntigo[diff], i]
                
            mapAntigo[n] = i
        return