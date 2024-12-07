class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen={}
        
        for num in arr:
            seen[num] = seen.get(num, 0) + 1 

        frequencies = list(seen.values())

        if len(frequencies) != len(set(frequencies)):
            return False  

        return True

