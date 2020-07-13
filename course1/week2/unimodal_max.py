def find_max(l):
    if len(l) == 1: # base case
        return l[0]
    else:
        n = len(l)
        left = l[:n//2]
        right = l[n//2:]
        
        l_start = left[0]
        l_end = left[-1]
        
        r_start = right[0]
        r_end = right[-1]
        
        if l_end == r_start:
            return l_end
        elif l_end < r_start:
            return find_max(right)
        else:
            return find_max(left)
            
l = [1,2]

print(find_max(l))