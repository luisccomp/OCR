import re


def is_valid_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[^\d]', '', cpf)

    if len(cpf) != 11 or re.match(r'(\d)\1{10}'):
        return False

    for index in range(-2, 0):
        checksum = 0
        weight = 2

        for digit in map(int, reversed(cpf[:index])):
            checksum += digit * weight
            weight += 1

        remainder = checksum % 11

        check_digit = str(11 - remainder if remainder >= 2 else 0)

        if check_digit != cpf[index]:
            return False
    
    return True
