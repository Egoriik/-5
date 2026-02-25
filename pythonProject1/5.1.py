N = int(input("Введите количество слов: "))
for i in range(N):
    word = input("Введите слово: ")
    if i == 0:
        res = word
    else:
        res = res + " " + word
    i += 1
print(res)
