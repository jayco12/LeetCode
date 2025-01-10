class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        stack = [] 
        for word in words1:
            stack.append(word)
        words = "".join(words2) 
        result_list = [] 

        while stack:
            word = stack.pop()  
            if all(char in word for char in words):  
                result_list.append(word) 
        return result_list