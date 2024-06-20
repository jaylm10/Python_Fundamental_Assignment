class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        a = len(nums)
        v = [-1] * (a + 1)
        for num in nums:
            v[num] = num
        for i in range(len(v)):
            if v[i] == -1:
                return i
        return 0
