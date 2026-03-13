print(bool("False")) # True — jebkura netukša virkne ir True, pat "False"
print(bool(" ")) # True — atstarpe ir simbols
print(bool("")) # False — tukša virkne
print(int("42")) # int ir vesels skaitļis
print(float("3.14")) # float ir peldošā komata skaitlis
# print(int("abc"))  # ValueError — "abc" nav skaitlis
# print(float("x.y"))# ValueError — "x.y" nav skaitlis
print(bool(0))     # False — skaitlis 0
print(bool([]))    # False — tukšs saraksts
print(bool([0]))   # True — saraksts nav tukšs, pat ja satur 0
print(bool(None))  # False — None ir falsy
print(True + True) # 2 — True ir 1
print(True * 10)   # 10
print(False + 5)   # 5 — False ir 0

# Mainīgo tipi
x_int = 42       # int — vesels skaitlis
x_float = 3.14   # float — peldošā komata skaitlis
x_bool = True    # bool — True/False vērtība
x_none = None    # NoneType — nekas
print(type(x_int))   # <class 'int'>
print(type(x_float)) # <class 'float'>
print(type(x_bool))  # <class 'bool'>
print(type(x_none))  # <class 'NoneType'>

# Interesanti gadījumi
print(round(2.5)) # 2 — noapaļo uz tuvāko pāru skaitli
print(round(3.5)) # 4 — noapaļo uz tuvāko pāru skaitli
print(0.1 + 0.2 == 0.3) # False, precizitātes (noapaļojuma) iemeslu dēļ 