class Solution:
    def partition(self, s: str) -> List[List[str]]:
        arr=[]
        arr_edit=[]

        def is_palindrome(a,b):
            for i in range((b-a)//2+1):
                if s[a+i]!=s[b-i]:
                    return False
            return True
        
        def backtrack(a,b):
            '''
            a부터 b까지 닫힌구간으로 팔린드롬 인지 체크하고 b+1 부터 끝까지 backtrack호출
            '''
            if a==len(s):
                arr.append(arr_edit.copy())
                return

            if is_palindrome(a,b):
                arr_edit.append(s[a:b+1])
                for j in range(b+1,len(s)):
                    backtrack(b+1,j)
                if b+1==len(s):
                    backtrack(b+1,b+1)
                arr_edit.pop()
        for i in range(len(s)):
            backtrack(0,i)
        return arr
            