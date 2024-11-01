class Solution:
    def makeFancyString(self, s: str) -> str:
        count=1
        st=[]
        stri=""
        for i in range(len(s)):
            st.append(s[i])
            if s[i]==s[i-1]:
                count+=1
                if count>2:
                    st.remove(s[i-1])
            i+=1
        for element in st:
            stri+=element
        
        return stri

        