# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.

# --------------- Runtime 32 ms, beats 72.19%. Memory 13.8MB, beats 97.94% ---------------


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        backspace = '#'

        def get_text(seq):
            dels, new_seq = 0, []

            for char in seq[::-1]:
                if char == backspace:
                    dels += 1
                    continue
                if dels:
                    dels -= 1
                    continue
                new_seq.append(char)

            return new_seq

        return get_text(s) == get_text(t)
