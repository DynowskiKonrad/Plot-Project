def interest(A, p, n):
    return A *(1 + (p/100)) ** n


print(interest(1000, 5, 3))