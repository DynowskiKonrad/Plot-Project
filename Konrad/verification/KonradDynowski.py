def check_card(credit_number):
    credit_number = credit_number.replace(" ", "")
    digits_as_list = []
    sum_of_digits = 0
    for digit in credit_number:
        digits_as_list = list(digit) + digits_as_list
    i = 0
    for digit in digits_as_list:
        temp_difference = int(digit) * (i % 2 + 1)
        if temp_difference > 9:
            sum_of_digits += (temp_difference - 9)
        else:
            sum_of_digits += temp_difference
        i += 1
    if sum_of_digits % 10 == 0:
        return True
    else:
        return False


months = [" January ", " February ", " March ", " April ", " May ", " June ", " July ", " August ", " September ",
          " October ", " November ", " December "]
years = ["19", "20", "21", "22", "18"]


def PESEL(number_pesel):
    assert(len(number_pesel) == 11)
    checksum = 0
    i = -1
    for digit in number_pesel[:10]:
        i += 2
        if i % 5 == 0:
            i += 2
        checksum += (int(digit) * (i % 10))
    if 10 - (checksum % 10) == int(number_pesel[-1]):
        to_print = number_pesel[4:6]
        to_print += months[int(number_pesel[2:4]) % 20 - 1]
        to_print += years[int(number_pesel[2:4]) // 20] + number_pesel[:2]
        print(to_print)
        return True
    else:
        return False


def IBAN(acc_number):
        acc_number = acc_number.replace(" ", "")
        if not acc_number[:2].isalpha():
            acc_number = "PL" + acc_number
        acc_number = acc_number[4:] + acc_number[:4]
        acc_number_temp = ""
        for sign in acc_number:
            if sign.isalpha():
                acc_number_temp += str(ord(sign) - 55)
            else:
                acc_number_temp += sign
        acc_number = acc_number_temp
        remainder = int(acc_number) % 97
        if remainder == 1:
            return True
        return False
