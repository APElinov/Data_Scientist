question, words, all_words = ' ', [], []

while question != '':
    question = input('Введите слово: ')
    if question != '':
        all_words.append(question)
        if words.count(question) == 0:
            words.append(question)

count = 0
for word in words:
    count += all_words.count(word) // 2

print('Количество пар одинаковых элементов: ', count)
