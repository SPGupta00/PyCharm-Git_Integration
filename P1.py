def celcius_to_ferhenite(Temp1):
    F = ((9/5)*Temp1 + 32)
    return F

def ferhenite_to_celsius(Temp2):
    C = ((5/9)*(Temp2 - 32))
    return C

Temp1 = int(input("Enter a temperature in celsius: "))
Temp2 = int(input("Enter a temperature in fahrenheit: "))

print(f"{Temp1}C = {celcius_to_ferhenite(Temp1)}F")
print(f"{Temp2}F = {ferhenite_to_celsius(Temp2)}C")
