from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        seen=set(word1)
        seen2=set(word2)
        
        if len(word1)!=len(word2):
            return False
        print(seen)
        return sorted(freq1.values()) == sorted(freq2.values())