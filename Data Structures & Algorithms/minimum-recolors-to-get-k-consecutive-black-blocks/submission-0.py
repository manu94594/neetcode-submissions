class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        whites = 0
        ans = k
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                whites += 1
            if i - l + 1 > k:          # shrink to keep window size == k
                if blocks[l] == 'W':
                    whites -= 1
                l += 1
            if i - l + 1 == k:         # only score full windows
                ans = min(ans, whites)
        return ans        

        # l = 0
        # op = 0
        # max_op = k
        # for i in range(len(blocks)):
        #     while i - l > 7:
        #         if blocks[l] == 'W':
        #             op -= 1
        #         l += 1

        #     if blocks[i] == 'W':
        #         op += 1
        #     if i - l + 1 == k:
        #         max_op = min(max_op, op)
        # return max_op        