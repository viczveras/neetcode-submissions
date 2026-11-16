class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        first_time = set()
        for n in nums:
            if n in first_time:
                return True
            first_time.add(n)
        
        return False
