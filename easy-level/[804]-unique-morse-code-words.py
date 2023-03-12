# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
# as follows:
#
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
#
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...".
# We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
#
# Example:
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

# --------------- Runtime 32 ms, beats 88.62%. Memory 13.8MB, beats 61.8% ---------------
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        to_morse = []
        for word in words:
            morse_word = ''
            for char in word:
                morse_word += morse[ord(char) - 97]
            to_morse.append(morse_word)

        return len(set(to_morse))
