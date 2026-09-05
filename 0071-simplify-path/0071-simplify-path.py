class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        t = path.split('/')
        for dir in t:
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/"+"/".join(stack)
        