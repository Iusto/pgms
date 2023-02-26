def solution(s):
    count = 0
    i = 0
    for i in range(len(s)): 
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == '[' and j == ']':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            else:
                stack.append(j)
        s = s[1:] + s[0] # 괄호 회전
        if not stack:
            count += 1
    return count