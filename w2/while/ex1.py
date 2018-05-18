list1 = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
#while True:
#    if list1[0] == 'Валера':
#        print('Валера нашелся')
#        break
#    else:
#        list1.pop(0)

def find_person():
    pname = input('Введите имя человека, которого надо найти: ')
    while True:
        if list1[0] == pname:
            print('{} нашелся!'.format(pname))
            break
        else:
            list1.pop(0)
find_person()