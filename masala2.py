def new_massiv(func):
    def wrapper(a):
        b = []
#b[k] = (a[0] + a[1] + ... + a[k])/k
        for i in range(len(a)):
            if i == 0:
                b.append(a[0])
            else:
                bi = sum(x for x in a[:i+1]) / i
                b.append(bi)
        return func(b)
    return wrapper

@new_massiv
def printer(lst):
    print(lst)

a = [5, 3, 6, 7, 3, 2]
printer(a)


