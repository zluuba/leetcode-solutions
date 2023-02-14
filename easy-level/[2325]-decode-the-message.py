# You are given the strings key and message, which represent a cipher key and a secret message, respectively.
# The steps to decode message are as follows:
#
# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
# we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
# Return the decoded message.

# --------------- Runtime 35 ms, beats 73.44%. Memory 13.9MB, beats 73.69% ---------------


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        decoder = {' ': ' '}

        for char in key:
            if char not in decoder:
                decoder[char] = abc[0]
                abc = abc[1:]

        encode_msg = [decoder[char] for char in message]
        return ''.join(encode_msg)
