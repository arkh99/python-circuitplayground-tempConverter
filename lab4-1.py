
def CelToFahr(F):
    C = (F - 32) * 5/9
    return C


fahr = float(input("enter the number in Fahrenheit: "))
print(CelToFahr(fahr))

def min(a, b):
    if a > b:
        return b
    else:
        return a
num1 = int(input("enter a number "))
num2 = int(input("enter another number "))
print("The min of inputs is", min(num1, num2))

def VolumeOfSphere(rad):
    volum = 3.14 * rad * rad * rad * 4/3
    return volum


volum = int(input("enter the radius of the sphere: "))
print("The volume of sphere is ", VolumeOfSphere(volum))


