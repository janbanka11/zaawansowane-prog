# Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
# metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
# ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
# stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
# zwracała true , a dla drugiego false .


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks > 50


student1 = Student("Jan", 60)
student2 = Student("Juan", 30)

print(f"Student {student1.name} is_passed {student1.is_passed()}")
print(f"Student {student2.name} is_passed {student2.is_passed()}")
