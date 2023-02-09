# Given a valid (IPv4) IP address, return a defanged version of that IP address.
#
# A defanged IP address replaces every period "." with "[.]".

# --------------- Runtime 20 ms, beats 99.9%. Memory 13.8MB, beats 41.10% ---------------


class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = ["[.]" if char == "." else char for char in address]
        return ''.join(new_address)
