def RecIntMut(x: str, y: str):
    
    # first we need to make the length of x and y be power of 2
    n_max = max(len(x), len(y))
    n = 1
    while True:
        if n >= n_max:
            break
        else:
            n *= 2
    
    x = "0"*(n - len(x)) + x
    y = "0"*(n - len(y)) + y        


    if n == 1: # base case
        return int(x) * int(y)
    else:
        # recursive case
        if n % 2 == 1 and n >= 5:
            x = "0" + x
            y = "0" + y
            
        a = x[:n//2]
        b = x[n//2:]
        
        c = y[:n//2]
        d = y[n//2:]
        
        p = str(int(a) + int(b))
        q = str(int(c) + int(d))
        
        ac = RecIntMut(a, c)
        bd = RecIntMut(b, d)
        pq = RecIntMut(p, q)

        adbc = pq - ac - bd
        return int(10**n * ac + 10 **(n//2) * adbc + bd)

x = "3141592653589793238462643383279502884197169399375105820974944592"
y = "2718281828459045235360287471352662497757247093699959574966967627"

print(RecIntMut(x, y))

print(int(x) * int(y)) # check answer