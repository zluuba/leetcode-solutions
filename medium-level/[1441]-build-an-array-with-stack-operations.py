# https://leetcode.com/problems/build-an-array-with-stack-operations/

# You are given an integer array target and an integer n.
# You have an empty stack with the two following operations:
#  - "Push": pushes an integer to the top of the stack.
#  - "Pop": removes the integer on the top of the stack.
# You also have a stream of the integers in the range [1, n].
# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target.
# You should follow the following rules:
#  - If the stream of the integers is not empty, pick the next integer from the stream and push it to the
#    top of the stack.
#  - If the stack is not empty, pop the integer at the top of the stack.
#  - If, at any moment, the elements in the stack (from the bottom to the top) are equal to target,
#  do not read new integers from the stream and do not do more operations on the stack.
# Return the stack operations needed to build target following the mentioned rules.
# If there are multiple valid answers, return any of them.

# Example 1:
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Pop the integer on the top of the stack. s = [1].
# Read 3 from the stream and push it to the stack. s = [1,3].

# Example 3:
# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
# The answers that read integer 3 from the stream are not accepted.

# --------------- Runtime 39 ms, beats 65.86%. Memory 16.3MB, beats 44.85% ---------------
from typing import List, Union


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        last_target_elem = target[-1]
        result = []

        for num in range(1, n + 1):
            if num > last_target_elem:
                break

            if num in target:
                result.append('Push')
            else:
                result.extend(['Push', 'Pop'])

        return result


# Alternative solution - same, but without (num > last_target_elem) condition
# --------------- Runtime 46 ms, beats 15.15%. Memory 16.2MB, beats 76.57% ---------------

class Solution2:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        length = min(target[-1] + 1, n + 1)
        result = []

        for num in range(1, length):
            if num in target:
                result.append('Push')
            else:
                result.extend(['Push', 'Pop'])

        return result


# Alternative solution - overthinking
# --------------- Runtime 40 ms, beats 54.14%. Memory 16.3MB, beats 44.85% ---------------

class Solution3:
    @staticmethod
    def flat(array: List[Union[str, list[str]]]) -> List[str]:
        flat_array = []

        for item in array:
            if isinstance(item, list):
                flat_array.extend(item)
            else:
                flat_array.append(item)

        return flat_array

    def buildArray(self, target: List[int], n: int) -> List[str]:
        length = min(n + 1, target[-1] + 1)
        result = ['Push' if num in target else ['Push', 'Pop'] for num in range(1, length)]

        return self.flat(result)
