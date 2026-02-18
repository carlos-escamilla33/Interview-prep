def decodeString(s):
    stack = []
    
    for char in s:
        if char != "]":
            stack.append(char)
        else:
            substr = ""
            while stack[-1] != "[":
                substr = stack.pop() + substr
            stack.pop()

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            stack.append(int(k) * substr)
    
    return "".join(stack)

s = "3[a]2[bc]"

print(decodeString(s))