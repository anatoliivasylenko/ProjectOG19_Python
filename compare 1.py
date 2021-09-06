def compare():
    a = int(input("Введите значение 'A' "))
    b = int(input("Введите значение 'Б' "))
    c = int(input("Введите значение 'В' "))
    while a <= b:
        a = a + c
        if a<b:
            print("Число " + str(a) + " меньше " + str(b))

        elif a == b:
            print("Число " + str(a) + " равно " + str(b))

    else:
        print("Ураа, цикл завершен. Число " + str(a) + " больше " + str(b))

compare()