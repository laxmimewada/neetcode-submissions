from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        max_freq = 0
        low = 0

        for high in range(len(s)):
            freq[s[high]] += 1
            max_freq = max(max_freq, freq[s[high]])
            length = high - low + 1

            if length - max_freq > k:
                freq[s[low]] -= 1
                low += 1

        res = max(res, high-low+1)
        return res

        