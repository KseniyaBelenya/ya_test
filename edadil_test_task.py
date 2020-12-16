"""
1) Посчитать общее число конфет N
2) Найти все делители n числа N, отсортировать их от большего к меньшему
3) Для каждого n и для каждого типа конфет проверить, можем ли мы разделить этот
   тип конфет между n людей поровну
   Если нет - следующая итерация n, если можем разделить все типы - вернуть n
"""

test1 = ['a', 'b', 'c']
test2 = ['a', 'b', 'c', 'a', 'b', 'c', 'd']
test3 = ['a', 'b', 'c', 'a', 'b', 'c']
test4 = ['a', 'b', 'b', 'a', 'a', 'a', 'a', 'a']
test5 = ['a' for i in range(1000000)] + ['b' for i in range(1000000)] + \
        ['c' for i in range(1000000)]


def divide_candies(candies):
    candies_num = len(candies)
    friends_num = [i for i in range(candies_num, 0, -1) if candies_num % i == 0]

    candies_types = {}
    for candy in candies:
        if candy in candies_types:
            candies_types[candy] += 1
        else:
            candies_types[candy] = 1

    for n in friends_num:
        for candy_type in candies_types:
            if candies_types[candy_type] % n != 0:
                break
            return n


if __name__ == '__main__':
    print(divide_candies(test1))
    print(divide_candies(test2))
    print(divide_candies(test3))
    print(divide_candies(test4))
    print(divide_candies(test5))
