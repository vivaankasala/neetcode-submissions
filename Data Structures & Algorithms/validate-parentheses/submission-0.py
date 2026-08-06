class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        count=0
        dic = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in dic.values():
                stack.append(c)
            else:
                if not stack or stack[-1]!=dic[c]:
                    return False
                stack.pop()

        return len(stack)==0

            

