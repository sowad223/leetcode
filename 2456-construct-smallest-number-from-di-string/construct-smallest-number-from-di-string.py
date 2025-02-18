class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = list("123456789")
        stack = []
        d_count = 0
        
        for i in range(len(pattern) - 1, -1, -1):
            if pattern[i] == 'D':
                d_count += 1
            else:
                if d_count:
                    stack.append(d_count)
                d_count = 0
                stack.append(0)  # for 'I'
        
        if d_count:
            stack.append(d_count)
        
        i = 1
        while stack:
            top = stack.pop()
            if top == 0:
                i += 1
            else:
                res[i - 1 : i + top] = reversed(res[i - 1 : i + top])
                i += top
        
        return "".join(res[: len(pattern) + 1])
        