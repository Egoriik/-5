cnt = 0
print("Математика для детей")
task1 = int(input("3 + 5 = "))
if task1 == 8:
    cnt += 1
    print("Правильно! \n")
else:
    print("Ответ неверный \n")
task2 = int(input("5 + 2 = "))
if task2 == 7:
    cnt+=1
    print("Правильно! \n")
else:
    print("Ответ неверный \n")
task3 = int(input("2 + 1 = "))
if task3 == 3:
    cnt+=1
    print("Правильно! \n")
else:
    print("Ответ неверный \n")

print(f"Игра окончена. \nПравильных ответов: {cnt}")