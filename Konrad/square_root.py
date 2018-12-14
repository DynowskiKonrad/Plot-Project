def square_root(a, b, c):
    """
    Compute roots of square function
    Arg are real number
    a, b, c which are equation coeficcients
    Returns :
        Tuple with results
    """
    if a != 0:
        delta = b**2 - 4 * a * c
        if delta < 0:
            return ()
        elif delta == 0:
            return -b / (2 * a),
        else:
            sqrt_delta = delta**0.5
            return (-b - sqrt_delta) / (2 * a), (-b + sqrt_delta) / (2 * a),
    elif b != 0:
        return - c / b,
    else:
        return ()


def input_of_float():

    coefficient = float(input("Please give me a coefficient for square function: "))
    print('\n')
    return coefficient


a_coefficient = input_of_float()
b_coefficient = input_of_float()
c_coefficient = input_of_float()
solutions = square_root(a_coefficient,b_coefficient,c_coefficient)
print("the number of real solutions is: ")
print(len(solutions))
