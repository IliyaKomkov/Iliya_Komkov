# s = "Daniil Nikolaev"
# s1 = s.lower()
# s2 = s.upper()
# print(s1)
# print(s2)
# print(s)
# строка. метод()

# print(s.count("i",0, 6))
# print(s.count("i"))

# print(s.rfind("i", 6))
# print(s.index("y"))
# print(s.replace("i", "e", 2))
# print(s.replace(" ", ""))
# print(s.replace(" ", "").isalpha())
#
# print(s.isalpha())
# print("DaniilNikolaev".isalpha())
# a = "21545"
# print(a.isdigit())
# a = "22"
# b = "2242247"
# c = "3322"
# print(a.rjust(8, "-"))
# print(b.rjust(8, "*"))
# print(c.rjust(8, "+"))
# print(a.ljust(8, "-"))
# print(b.ljust(8, "-"))
# print(c.ljust(8, "-"))

# s = "Николаев-Даниил-Александрович"
# name, surname, second_name = s.split("-")
# print(name)
# print(surname)
# print(second_name)

# nums = "1, 2,43, 32,33    ,3 3 32"
# print(nums.replace(" ", "").split(","))

# words = [" str", "float", "bool"]
# print(", ".join(words))

a = "  Аааа ааа  "
print(a.strip())
print(a.rstrip())
print(a.lstrip())
