fahrenheit = input("Please type in a temperature (F): ")

F = float(fahrenheit)
C = (F - 32) * (5 / 9)

print(f"{F} degrees Fahrenheit equals {C:.6f} degrees Celsius")

if C < 0:
    print("Brr! It's cold in here!")