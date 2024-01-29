def fizz_buzz(n): # определяем функцию fizz_buzz
    for x in range(1, n+1): # создаем цикл от 1 до n включительно
        if x % 15 == 0: # если число делится на 15, то оно делится и на 3, и на 5
            print("FizzBuzz") # выводим FizzBuzz с переносом строки
        elif x % 3 == 0: # иначе, если число делится на 3
            print("Fizz") # выводим Fizz с переносом строки
        elif x % 5 == 0: # иначе, если число делится на 5
            print("Buzz") # выводим Buzz с переносом строки
        else: # иначе, если число не делится ни на 3, ни на 5
            print(x) # выводим само число с переносом строки

# тестируем функцию на разных значениях
fizz_buzz(17) # выводит
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
fizz_buzz(25) # выводит
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
