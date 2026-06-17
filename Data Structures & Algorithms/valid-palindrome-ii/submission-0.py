class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        omit = 0

        def helper(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        while l < r:
            if s[l] != s[r] and omit == 1:
                return False
            if s[l] != s[r] and omit == 0:
                omit = 1
                left_skip = helper(l+1, r)
                right_skip = helper(l, r-1)
                if left_skip or right_skip :
                    return True
            else:
                l += 1
                r -= 1
        return True