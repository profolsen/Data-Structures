# Note: this code is not documented because the meaning of the computation contained in this file
# does not correspond to any real or even toy application.
# Although I guess that this comment counts as documentation, so I guess I lied.
def loop1():
    n = 10
    x = 0
    for i in range(10):
        x += 1
    print(x)
    
def loop2(n):
    x = 0
    for i in range(10):
        x += 1
    print(x)
    
def loop3(a_list):
    z = 0
    for i, x in enumerate(a_list):
        z += (i + x)
    print(z)
    
def loop4(n):
    m = 2 * n
    z = 0
    for i in range(n):
        for j in range(m):
            z += i+j
    print(z)
    
def loop5(n):
    x = 0
    for i in range(n):
        for j in range(i):
            x += j
    print(x)
    
def loop6(n):
    t = 0
    while(n > 0):
        n = n // 10
        t += 1
    print(t)
    
def loop7(n):
    i = 0
    j = 0
    x = 0
    while j < n:
        if i == n :
            j += 1
            i = 0
        i += 1
        x += 1
        print(">>",i,j)
    print(x)
    
def loop(a_list, b_list):
    for i, x_a in enumerate(a_list):
        for j, x_b in enumerate(b_list):
            if x_a == x_b:
                print(f"a_list[{i}] == b_list[{j}]")
                
def loop9(a_list):
    while len(a_list) > 0:
        if a_list[0] > 0:
            a_list[0] -= 1
            a_list.append(a_list[0])
        x = a_list.pop(0)
        print(a_list)
        
def loop10(a_list):
    index = 1
    while a_list[0] > 0:
        if index >= len(a_list):
            index = 1
        a_list[index] += 1
        a_list[0] -= 1
        index += 1
    print(a_list)

def loop11(a_list):
    while a_list[0] > 0:
        a_list.append(1)
        a_list[0] -= 1
    a_list.pop(0)
    print(a_list)
    
def loop12(a_list):
    n = len(a_list)
    for i in range(n):
        loop11(a_list)
    print(a_list)

def loop13(n):
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            print(f"{i} divides {n} evenly")
#loop13(1480)

def loop14(a_list):
    for e in a_list:
        loop13(e)
#loop14([10, 100, 100])

def loop15(a_list, b_list):
    if len(b_list) > 0:
        a_list.append(b_list.pop(0))
    print(a_list, b_list)

def loop16(e, a_list):
    for i, t in enumerate(a_list):
        if t == e:
            return i
print(loop16(4, [3, 4, 1]))

def loop17(n):
    t = 0
    for i in range(n):
        loop5(n)
        t += 1
    return t
    
def loop18(n):
    t = 0
    for i in range(n):
        for j in range(n):
            t += 1
    for i in range(n):
        t += 1
    return t
              
