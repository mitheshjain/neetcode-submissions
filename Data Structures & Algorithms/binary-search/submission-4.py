class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # NeetCode Pro-Tip: Prevent integer overflow
            # In Python, integers are arbitrary precision, but in Java/C++, 
            # (l + r) // 2 can exceed the max 32-bit integer.
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1