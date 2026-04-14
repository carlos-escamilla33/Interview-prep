def isAnagram(s, t):
        if len(s) != len(t):
            return False
        
        s_ht = {}

        for l in s:
            if l not in s_ht:
                s_ht[l] = 0
            s_ht[l] += 1
        
        for l in t:
            if l not in s_ht:
                return False
            
            if l in s_ht:
                s_ht[l] -= 1
                if s_ht[l] == 0:
                    del s_ht[l]
        
        return len(s_ht) == 0

# Time Complexity - O(2N), simplifies to O(N)
# Space Complexity - O(N), because it can hold N characters in the hashtable