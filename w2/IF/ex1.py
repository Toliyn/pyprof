user_age = input('Введите возраст: ')
user_age = int(user_age)
print(type(user_age))
if user_age > 30:
    print('Иди работай')
elif user_age > 18:
    print('Иди на пары')
elif user_age > 7:
    print('Пора в школу')
else:
    print('Пора в садик')