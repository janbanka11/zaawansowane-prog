
def zad1(name: str, surname: str):
    output : str = name + ' ' + surname
    return output

def zad2(num1: int, num2: int):
    return num1 * num2

def zad3(number) -> bool:
    return number % 2 == 0

def zad4(num1: int, num2: int, num3: int) -> bool:
    return num1 + num2 > num3

def zad5(lista: list, num: int) -> bool:
    for i in lista:
        if i == num:
            return True
    return False

def zad6(lista1: list, lista2: list) -> list:
    merged_list: set = set(lista1 + lista2)
    output_list = [x**3 for x in merged_list]
    return output_list


print(zad1("Jan", "Kowalski"))
print(zad2(3, 2))

#zad3
isEven = zad3(5)
if isEven:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
#koniec zad3

print(zad4(4,2,3))
print(zad5([3,2,1,4,5], 4))
print(zad6([3,2,1,4,5], [5,12,32]))
