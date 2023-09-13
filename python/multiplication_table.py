# n = int(input("Please enter a positive integer "))
# 
# m = 1
# while m <= 10:
#     print(n, "x", m, " = ", n*m)
#     m += 1

number = int(input("Provide a positive number whois you want to multiplication table: "))

def multiplication_table(number_multiplicat):
    one = 1
    while one <= 10:
#         multiplicat = number_multiplicat*one
#         result = str(number_multiplicat) + "x" + str(one) + " = " + str(multiplicat)
        print(number_multiplicat, "x", one, "=", number_multiplicat*one)
        one += 1
#     return result

multiplicate_result = multiplication_table(number)
# print(multiplicate_result)