def convert_binary_to_decimal_v1(binary: str):
    based = [128,64,32,16,8,4,2,1]
    count = 0
    result = 0

    for index in binary:
        result += (based[count] * int(index))
        count += 1
    
    return result


def convert_binary_to_decimal_v2(binary: str):
    result = 0
    binary = binary[::-1]

    for index in range(len(binary)):
        result += (2**index) * int(binary[index])

    return result


convert_binary_to_decimal_v3 = lambda binary:sum([((2**index)*int("".join(binary[::-1])[index]))for index in range(len(binary))])

binary_value = input("Binary: ")

my_decimal1 = convert_binary_to_decimal_v1(binary=binary_value)
print(f"result_of_function 1: {my_decimal1}")

my_decimal2 = convert_binary_to_decimal_v2(binary=binary_value)
print(f"result_of_function 2: {my_decimal2}")

my_decimal3 = convert_binary_to_decimal_v3(binary=binary_value)
print(f"result_of_function 3: {my_decimal3}")


