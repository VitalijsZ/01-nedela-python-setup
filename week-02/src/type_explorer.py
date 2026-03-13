print(bool("False")) #jebkura netukša virkne ir true 
print(bool(" ")) #jebkura netukša virkne ir true 
print(int("42")) #int ir vesels skaitļis
print(float("3.14")) #float ir peldošā komata skaitlis
#print(int("abc")) nestrāda jo abc nav skaitlis
#print(float("x.y")) nestrāda, jo float ir skaitlis 
print(bool(""))    # False — tukša virkne
print(bool(0))     # False — skaitlis 0
print(bool([]))    # False — tukšs saraksts
print(bool([0]))   # True — saraksts nav tukšs, pat ja satur 0
print(bool(None))  # False — None ir falsy
print(True + True) # 2
print(True * 10)   # 10
print(False + 5)   # 5
print(0.1 + 0.2 == 0.3) # False, precizitātes iemeslu dēļ

x_int = 42
x_float = 3.14
x_bool = True
x_none = None
print(type(x_int))   # <class 'int'>
print(type(x_float)) # <class 'float'>
print(type(x_bool))  # <class 'bool'>
print(type(x_none))  # <class 'NoneType'>