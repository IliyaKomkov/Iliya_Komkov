# s = "Python для автоматизации"
# print(s.upper())
# print(s.lower())# 1 задание
from os import name

# msg = "абракадабра"
# # print(msg.count("ра"))
# print(msg.count("а", 3)) # 2 задание

# msg = "абракадабра"
# print(msg.find("ка"))
# print(msg.rfind("а"))
# print(msg.find("xyz")) # 3 задание

# text = "Я изучаю Java"
# text2 = (text.replace("Java","Python"))
# print(text2.replace(" ", ""))# 4 задание

# s = "Python"
# y = "12345"
# x = "123abc"
# print(s.isalpha())
# print(y.isdigit())
# print(x.isalpha())
# print(x.isdigit())# 5 задание

# code = "42"
# print(code.rjust(7, "0"))
# t = "text"
# print(t.ljust(10, "*"))# 6 задание

# # s = "яблоко, груша, банан"
# # apple, grusha, banan = s.split(",")
# # print(apple)
# # print(grusha)
# # print(banan)
# s = "python; Java; C++"
# A, B, C = s.split(";")
# print(A, B, C) # 7 задание

# t = "Привет", "мир", "!"
# print(" ".join(t))
# t2 = "apple", "banana", "cherry"
# print(", ". join(t2))# 8 задание

# s = " Python"
# s1 = "Python "
# s2 = " Python "
# print(s.lstrip())
# print(s1.rstrip())
# print(s2.strip()) # 9 задание

# text = "програмирование"
# print(text.replace("п", "П"))
# print(text.count("р"))
# print(text.find("и"))
# print("". join(text))# не понял, что значит "разверни строку и выведи результат"
# 10 задание

#Спецсимфолы
# text = "Hello\nPython"
# print(text)# \n переносит строку

# t = "Python\tAutomation"
# print(t)# \t - это удлиненный пробел

# path = "C:\\new\\test.txt"
# print(path)# добавил слеш, ошибка ушла

# s = "Марка вина \"Ягодка\""
# print(s)# требуется немного углубиться, путаюсь где ставить слеш

# path = r"C:\new\test.txt"
# print(path)# сырая строка из-за r string, в обычной строке такой сивол не используем

# s = "Hello\b World"# пропала буква о
# s2 = "Hello\fPython"# появился сивол вместо пробела
# print(s)
# print(s2)

# name = "Меня зовут Илья"
# age =  " 27 "
# result = name + age
# print(result)
# print(name + 27) # - вылезла ошибка

# # city = "Ногинск"
# year = "2026"
# # result = "Сегодя", year, "и я живу в городе ", city
# # print(result)
# # print(f"Сегодня {year} и я живу в городе {city}")
#
# print(f"через 5 лет будет {year + 5}")# забыл как делать

# a = "Дважды мой возраст:"
# s = 27
# result = (a.upper())
# print(f"{result} {s * 2}")
# print(f"Дважды мой возраст: {27 * 2}")

# a = "Квадрат числа 7 равен 49."
# s = 7 ** 2
# print(f"{a} =  {s}")
