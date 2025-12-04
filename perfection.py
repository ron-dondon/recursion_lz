def perf(n, i=1, summ=0): #создаем функцию, сумма делителей с 0
    if i == n: # если i равно n, проверяем сумму делителей
        return summ == n
    if n % i == 0: #если i делитель n,то  добавляем его к сумме
        summ += i
    return perf(n, i + 1, summ)

def main():#создаём функцию, которая помогает импортировать функцию в другом файле
    a = int(input("Введите число: "))
    d= perf(a)
    if d:
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()