class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        seen=set(word2)
        
        if len(word1)!=len(word2):
            return False

        for i in range(len(word1)):
            if word1[i] not in seen:
                return False
            return True