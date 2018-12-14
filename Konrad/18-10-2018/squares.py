def create_list(n, i = 1):
    list_of_squares = [n**2 for n in range(i, n+1)]
    return list_of_squares


some_table = create_list(50, 25)
#list comprehension
print([x % 2 for x in some_table])