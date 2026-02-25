print("В случае если вы захотите прекратить ввод слов пропишите Stop")
word = input("Введите слово: ")
res = ""
while word != "stop":
    if res == "":
        res = word
    else:
        res = res + " " + word
    word = input("Введите слово: ")
print(res)
