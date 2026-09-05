class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        j = 0
        for i in range(1,n+1):
            if j>=len(target):
                break
            elif i == target[j]:
                stack.append("Push")
                j+=1
            else:
                stack.append("Push")
                stack.append("Pop")
        return stack
            

                
        