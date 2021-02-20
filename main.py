if __name__ == '__main__':
    while (True):
        print("""Создаем массив содержащий 10 первых нечетных чисел.
                Выведете элементы массива на консоль в одну строку, разделяя запятой""")
        print("0. Exit")
        answer = input("enter choise")
        if answer == "0":
            break
        if answer == "1":
            mylist = []
            for x in range(1, 20, 2):
                mylist.append(x)
                print(mylist)
