number = 123456789
formatted_number = f"USD {number:,}.00"
print(formatted_number)

number = 55534567.89
formatted_number = f"{number:,}"
print(formatted_number)

number = str(1234567.89) 
formatted_number = f"{int(float(number)):,}"
print(formatted_number)

number = str(1234567.89) #1234567.89
formatted_number = f"{float(number):,}"
print(formatted_number)

number = 3456123123
number = float(f"{number:.4f}")
formatted_number = f"{number:,}0"
print(formatted_number)

number = str(345612311) 
formatted_number = f"{float(number):,}0"
print(formatted_number)