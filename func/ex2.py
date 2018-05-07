def get_answer(question, answer):

    for key in answer:
        if question == key:
            return answer[key]

question = input('Введита ваш вопрос: ').lower()
answer = {'привет':'И тебе привет', 'как дела':'Лучше всех', 'пока':'Увидимся'}
print(get_answer(question, answer))