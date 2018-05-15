str1 = input('введите строку: ')
str2 = input('введите еще одну: ')

def compare(string1, string2):
    if string1 == string2:
        print(1)
        return 1
    elif (string1 != string2) and (len(string1) > len(string2)):
        print(2)
        return 2
    elif (string1 != string2) and string2 == 'learn':
        print(3)
        return 3


compare(str1, str2)


