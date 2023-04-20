# https://leetcode.com/problems/defanging-an-ip-address/

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

# --------------- Runtime 20 ms, beats 99.9%. Memory 13.8MB, beats 41.10% ---------------


class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ["[.]" if char == "." else char for char in address]
        return ''.join(new_address)
