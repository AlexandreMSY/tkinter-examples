def Binary(number):
    bit = 0
    rem = 0
    result = 0

    while number:
        rem = number % 10
        number = int(number // 10)
        result += rem * 2 ** bit
        bit += 1
    
    return result

def DecimalToBinary(number):
    global stringT
    stringT = ""
    teste = 0
    if number > 1:
        DecimalToBinary(number // 2)
    teste = number % 2
    stringT += str(teste)
    
    return stringT
    




