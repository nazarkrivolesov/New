import random
def task_1(list):
    list_new = ''
    for i in list:
        list_new += i.capitalize() + ', '
        list_new.join(i.capitalize())
    print(list_new)

def task_2():
    CamelCase = ["FirstItem", "FriendsList", "MyTuple"]
    snace_case = CamelCase.copy()
    for i in range(len(snace_case)):
        snace_case[i] = snace_case[i][0].lower() + snace_case[i][1:]

    for idx, word in enumerate(snace_case):
        for l_index, letter in enumerate(word):
            if letter.isupper():
                snace_case[idx] = word[:l_index] + "_" + letter.lower() + word[l_index + 1:]
    print(snace_case)

def task_3():
    My_favorites = {
        'Ruby': 'Yukihiro Matsumoto',
        'C#': 'Anders Hejlsberg',
        'Python': 'Guido van Rossum',
        'C++': 'Bjarne Stroustrup'
    }
    for key,value in My_favorites.items():
        print('My favorite programming language is ' + key + '. It was created by ' + value +'.')
    element = random.choice(list(My_favorites.keys()))
    My_favorites.pop(element)
    print(My_favorites.items())

def task_4(list):
    for i in list:
        if type(i) == str:
            print(i)
        else:
            continue

def task_5():
    types = [1, 1000, 2, 12, {'key': 'value'}]
    for i in types:
        if type(i) == int:
            print(i)
        else:
            t = type(i)
            print('Цикл не працює з', t)
            break

def task_6():
    string = 'abcdefgabc'
    string_dict = {}
    for i in string:
        q = string_dict.get(i,0)
        string_dict[i] = q + 1

    for i,q in string_dict.items():
        print(i + '-' + str(q))

def task_7():

    count = 0

    while count < 2:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        op = input('Enter operator: ')
        if op == '+':
            print(a+b)
            i = input("If you want to calculate enter 'start': ")
            if i == 'start':
                continue
            else:
                print('Bye')
                break

        if op == '-':
            print(a-b)
            i = input("If you want to calculate enter 'start': ")
            if i == 'start':
                continue
            else:
                print('Bye')
                break

        if op == '/':
            if b == 0:
                count +=1
                print("Division by zero is not possible, enter another value")
                continue
            else:
                print(a/b)
                i = input("If you want to calculate enter 'start': ")
                if i == 'start':
                    continue
                else:
                    print('Bye')
                    break

        if op == '*':
            print(a*b)
            i = input("If you want to calculate enter 'start': ")
            if i == 'start':
                continue
            else:
                print('Bye')
                break

    else:
        print('The attempts are over')




# task_1(["john", "marta", "james", "amanda", "marianna"])
# task_2()
# task_3()
# task_4(['Jack', 'Leon', 'Alice', None, 32, 'Bob'])
# task_5()
# task_6()
task_7()