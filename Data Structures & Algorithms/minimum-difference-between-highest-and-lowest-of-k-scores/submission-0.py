class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        ans = nums[-1] - nums[0]
        for r in range(len(nums)):
            if r - l + 1 == k:
                ans = min(ans, nums[r] - nums[l])
                l += 1
        return ans