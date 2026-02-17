def decodeString(s):
    stack = []
    current_str = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)  # handles multi-digit numbers
        elif char == "[":
            stack.append((current_str, current_num))  # save state
            current_str = ""
            current_num = 0
        elif char == "]":
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str  # restore and expand
        else:
            current_str += char

    return current_str