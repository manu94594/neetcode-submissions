class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        ans = 0
        sliding_sum = 0
        for r in range(len(arr)):
            sliding_sum += arr[r]
            if r - l + 1 == k:
                if sliding_sum / k >= threshold:
                    ans += 1
                sliding_sum -= arr[l]
                l += 1
        return ans