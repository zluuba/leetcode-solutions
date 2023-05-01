# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.
# Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

# Example 2:
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

# --------------- Runtime 35 ms, beats 44.3%. Memory 16.2MB, beats 8.21% ---------------
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)[1:-1]
        return sum(salary) / len(salary)


# Alternative solution - without any built-in function
# --------------- Runtime 47 ms, beats 5.49%. Memory 16.4MB, beats 8.21% ---------------

class Solution2:
    def average(self, salary: List[int]) -> float:
        minimum, maximum = (salary[0], salary[1]) if salary[0] < salary[1] else (salary[1], salary[0])

        length = 0
        s = salary[0] + salary[1]
        for i in salary[2:]:
            if i < minimum:
                minimum = i
            elif i > maximum:
                maximum = i
            length += 1
            s += i

        return (s - minimum - maximum) / length
