def check_card(number):
    try:
        assert number + "a"
        number.replace(" ", "")
    except AssertionError:
        return False
    number_as_list = []
    for i in range(len(number)):
        number_as_list.append(number[i - 1])
    for i in range(len(number)-1, 1, -2):
        number_as_list[i - 1]

print(" coupe coupe ".replace(" ", ""))
http://phys.p.lodz.pl/verification.html - zrobić to w pythonie enter enter enter