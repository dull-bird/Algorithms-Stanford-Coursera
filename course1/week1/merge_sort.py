def merge(list1, list2):
    i = 0
    j = 0
    out = []
    for k in range(len(list1 + list2)):
        if list1[i] < list2[j]:
            out.append(list1[i])
            i += 1
            if i == len(list1):
                out.extend(list2[j:])
                return out
        else:
            out.append(list2[j])
            j += 1
            if j == len(list2):
                out.extend(list1[i:])
                return out
    return out


def divide(list):
    n = len(list)
    return list[0:n//2], list[n//2:]

def merge_sort(l):
    if len(l) == 1: # base case
        return list
    else: # recursive case
        list1, list2 = divide(l) # divide
        #print(list1, list2)
        return merge(merge_sort(list1), merge_sort(list2)) # sort sub-arrays recursively and then merge



if __name__ == "__main__":
    out1 = merge([1], [6])
    #divid = divide([1,2,3,4,5])
    out = merge_sort([22,200, -1, 2, 1, 1,4,5,3])
    print(out)