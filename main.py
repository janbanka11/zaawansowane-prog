def zad2a(names):
    for name in names:
        print(name)


def zad2b1(numbers):
    for number in numbers:
        number *= 2
    return numbers


def zad2b2(numbers):
    new_numbers = [number * 2 for number in numbers]
    return new_numbers


def zad2c(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


def zad2d(numbers):
    i = 0
    for number in numbers:
        if i % 2 == 0:
            i = i + 1
            print(number)


print(f"zadanie 1: {zad2a(['ala', 'janek', 'robert', 'marek', 'kot'])}")
print(f"zadanie 2a: {zad2b1([10,32,55,33,3,5])}")
print(f"zadanie 2b: {zad2b2([10,32,55,33,3,5])}")
print(f"zadanie 2c: {zad2c([10,32,55,33,3,5, 4,14,543,123,66])}")
print(f"zadanie 2d: {zad2d([423,45,123,55,2,3,4,5,6,7,8])}")
