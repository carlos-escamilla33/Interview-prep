
def isPalindrome(s):
    s_new = s.lower()

    l = 0
    r = len(s_new) - 1

    while l <= r:
        if s_new[l].isalum() and s_new[r].isalnum():
            if s_new[l] == s_new[r]:
                l += 1
                r -= 1
            else:
                return False
        elif not s_new[l].isalnum():
            l += 1
        else:
            r -= 1
    
    return True