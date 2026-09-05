class Solution:
    def clearDigits(self, s: str) -> str:
        t = []
        for i in s:
            if i.islower():
                t.append(i)
            else:
                t.pop()
        return ''.join(t)


            
        