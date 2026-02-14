def removeStars(s):
    stack = []

    for char in s:
        if char == "*" and stack:
            stack.pop()
        else:
            stack.append(char)
    
    return "".join(stack)