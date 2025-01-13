class Solution:
    def minimumLength(self, s: str) -> int:
        ch_freq = {}
        for ch in s: 
            ch_freq[ch] = ch_freq.get(ch, 0) + 1 
        total = 0 
        for ch in ch_freq.keys(): 
            if ch_freq[ch] % 2 == 0: 
                total += 2 
            else: 
                total += 1 
        return total