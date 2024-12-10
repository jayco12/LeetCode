class Solution:
    def maximumLength(self, s: str) -> int:
        hashmap=defaultdict(int)
        for l in range(len(s)):
            for r in range(l, len(s)):
                if s[l]!=s[r]:
                    break
                substr=s[l:r+1]
                hashmap[substr]+=1
        answer=-1
        for key, val in hashmap.items():
            if val>=3 and len(key)>answer:
                answer=len(key)
        return answer