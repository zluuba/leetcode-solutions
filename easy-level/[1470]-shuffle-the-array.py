# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# --------------- Runtime 56 ms, beats 94.54%. Memory 14.1MB, beats 86.30% ---------------


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        left = nums[:n]
        right = nums[n:]
        result = []

        for i in range(n):
            result.append(left[i])
            result.append(right[i])

        return result
