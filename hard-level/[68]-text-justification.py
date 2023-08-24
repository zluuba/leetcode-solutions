# https://leetcode.com/problems/text-justification/

# Given an array of strings words and a width maxWidth, format the text such that each line has
# exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line does not divide evenly between words,
# the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
#  - A word is defined as a character sequence consisting of non-space characters only.
#  - Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#  - The input array words contains at least one word.

# Example 1:
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
# because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.",
#                 "Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

# --------------- Runtime 44 ms, beats 50.81%. Memory 16.5MB, beats 31.4% ---------------
from typing import List


class Solution:
    def split_words_by_lines(self, words, max_width):
        length = len(words)
        lines = []
        pointer = 0

        while pointer < length:
            chunk = []
            chunk_width = 0

            for i in range(pointer, length):
                word = words[i]
                word_length = len(word)

                if word_length + chunk_width <= max_width:
                    chunk.append(word)
                    chunk_width += word_length + 1
                    pointer += 1
                else: break

            lines.append(chunk)

        return lines

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = self.split_words_by_lines(words, maxWidth)
        lines_len = len(lines)
        result = []

        for ind in range(lines_len):
            line = lines[ind]
            line_len = len(line)
            length_between = (line_len - 1) if line_len > 1 else line_len
            words_width = sum([len(word) for word in line])

            spaces_count = maxWidth - words_width
            space_len = spaces_count // length_between
            remainder = spaces_count % length_between

            new_line = []

            if ind == lines_len - 1:
                text_len = sum([len(w) for w in line]) + (line_len - 1)
                for i in range(line_len - 1):
                    line[i] += ' '
                line.extend([' ' * (maxWidth - text_len)])
                new_line.extend(line)
            else:
                for i in range(line_len):
                    new_word = line[i] + (' ' * space_len)
                    new_line.append(new_word if (i < line_len - 1 or line_len == 1) else line[i])

            j = 0
            while remainder and ind != lines_len - 1:
                new_line[j] += ' '
                remainder -= 1
                j += 1

            result.append(''.join(new_line))

        return result
