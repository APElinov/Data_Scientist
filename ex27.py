question, words = ' ', []

while question != '':
    question = input('Введите слово: ')
    if question != '':
        if words.count(question) == 0:
            words.append(question)

print(words)