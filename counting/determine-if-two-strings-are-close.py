class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        seen=set(word1)
        seen2=set(word2)
        
        if len(word1)!=len(word2):
            return False

        if seen==seen2:
            return True
        return False