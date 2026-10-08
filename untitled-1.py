for x in range(10000):
    a = 0
    b = 0
    y = x
    while x > 0:
        a = a + 2
        b = b +  (x % 10)
        x = x // 10
    print(a, end=" ")
    print(b)
    if a==6 and b ==9:
        print(y)
        break