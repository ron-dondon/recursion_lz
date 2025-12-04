def part(a, min=1): #создаем функцию 
    if a == 0:
        return [[]]  #если осталось 0, возвращаем пустое разбиение
    d = []
    for i in range(min, a + 1):  # Пробегаем от min до n
        for j in part(a - i, i):  # Рекурсивный вызов для остатка
            d.append([i] + j)  # Добавляем  число к каждому разбиению
    return d

def b(n): #создаем функцию
    parts = part(n) #список всех разложений
    for t in parts:
        print(t)
        
def main():
    n = int(input("Введите число, которое хотите разложить на сумму целых чисел: "))
    b(n) #вызываем функцию
if __name__ == "__main__":
    main()
