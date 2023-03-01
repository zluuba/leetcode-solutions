# You are playing the Bulls and Cows game with your friend.
#
# You write down a secret number and ask your friend to guess what the number is.
# When your friend makes a guess, you provide a hint with the following info:
#
# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number
# but are located in the wrong position.
# Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number (secret) and your friend's guess (guess), return the hint for your friend's guess.
#
# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.
# Note that both secret and guess may contain duplicate digits.

# --------------- Runtime 67 ms, beats 18.48%. Memory 13.9MB, beats 68.44% ---------------


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sec, gue = [], []

        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                sec.append(secret[i])
                gue.append(guess[i])

        cows = 0
        for i in sec:
            if i in gue:
                cows += 1
                gue.remove(i)

        return f'{str(bulls)}A{str(cows)}B'
