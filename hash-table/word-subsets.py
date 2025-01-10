class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        stack = [] 
        for word in words1:
            stack.append(word)

        result_list = [] 

        while stack:
            word = stack.pop()  
            if all(element in word for element in words2):  
                result_list.append(word) 
        return result_list