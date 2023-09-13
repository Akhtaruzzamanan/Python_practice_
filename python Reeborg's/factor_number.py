number = int(input("Insert a number to see the factor number: "))
factor_number = []
for factor in range(1, number + 1):
    if number % factor == 0:
        factor_number.append(factor)
#     factor_num = number / factor
#     print(factor_num)
print(f"{number} has total {len(factor_number)} factor number")
print(f"factor number are: {factor_number}")