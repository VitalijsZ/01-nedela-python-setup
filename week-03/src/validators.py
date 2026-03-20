def is_email(text):
    """Pārbauda vai teksts ir vienkāršs e-pasts.

    Args:
        text (str): ievades teksts

    Returns:
        bool: True ja atbilst, False ja neatbilst
    """

    # nav atstarpju
    if " " in text:
        return False

    # tieši viens @
    if text.count("@") != 1:
        return False

    email_name, domain = text.split("@")

    # daļas nedrīkst būt tukšas
    if not email_name or not domain:
        return False

    # domain jābūt .
    if "." not in domain:
        return False

    # nedrīkst sākties vai beigties ar .
    if domain[0] == "." or domain[-1] == ".":
        return False

    return True

def is_phone_number(text):
    """Pārbauda vai teksts atbilst Latvijas telefona numura formātam.

    Formāts: +371 XXXXXXXX (kur X ir cipari)

    Args:
        text (str): ievades teksts

    Returns:
        bool: True ja atbilst formātam, False ja neatbilst
    """

    if not text.startswith("+371"):
        return False

    if text[4] != " ":
        return False

    if text.count(" ") != 1:
        return False

    number_part = text.split(" ")[1]

    if len(number_part) != 8:
        return False

    if not number_part.isdigit():
        return False

    return True

def is_valid_age(age):
    """Pārbauda vai vecums ir derīgs.

    Vecumam jābūt veselam skaitlim diapazonā no 0 līdz 150.

    Args:
        age (int): vecums

    Returns:
        bool: True ja vecums ir derīgs, False ja nav

    Example:
        >>> is_valid_age(25)
        True
        >>> is_valid_age(-5)
        False
        >>> is_valid_age(200)
        False
    """

    if not isinstance(age, int):
        return False

    if age < 0 or age > 150:
        return False

    return True

def is_strong_password(text):
    """Pārbauda vai parole ir pietiekami droša.

    Parole ir droša, ja:
    - tā ir vismaz 8 simbolus gara
    - satur vismaz vienu burtu
    - satur vismaz vienu ciparu

    Args:
        text (str): parole

    Returns:
        bool: True ja parole ir droša, False ja nav

    Example:
        >>> is_strong_password("abc12345")
        True
        >>> is_strong_password("abcdefg")
        False
    """

    if len(text) < 8:
        return False

    is_alpha = False
    is_digit = False

    for i in text:
        if i.isalpha():
            is_alpha = True
        if i.isdigit():
            is_digit = True

    if is_alpha and is_digit:
        return True

    return False

def is_valid_date(text):
    """Pārbauda vai teksts atbilst datumam YYYY-MM-DD formātā.

    Args:
        text (str): ievades teksts

    Returns:
        bool: True ja formāts ir pareizs, False ja nav

    Example:
        >>> is_valid_date("2024-05-10")
        True
        >>> is_valid_date("2024-5-10")
        False
    """

    # jābūt 2 domuzīmēm
    if text.count("-") != 2:
        return False

    parts = text.split("-")

    # jābūt 3 daļām
    if len(parts) != 3:
        return False

    year, month, day = parts

    # pārbaude uz cipariem
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    # garuma pārbaude
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    return True

if __name__ == "__main__":
    print("E-pasta parbaude:")
    print(is_email("anna@inbox.lv"))
    print(is_email("john.doe@gmail.com"))
    print(is_email("user123@mail.com"))
    print(is_email("test@test.org"))
    print(is_email("anna"))
    print(is_email("anna@"))
    print(is_email("@inbox.lv"))
    print(is_email("anna@inbox"))
    print(is_email("anna@.lv"))
    print(is_email("anna@lv."))
    print(is_email("anna@@inbox.lv"))
    print(is_email("anna inbox@lv.com"))
    print("Telefona numura parbaude:")
    print(is_phone_number("26123456"))       
    print(is_phone_number("+37126123456"))      
    print(is_phone_number("+372 26123456"))    
    print(is_phone_number("+371 2612345"))      
    print(is_phone_number("+371 261234567"))   
    print(is_phone_number("+371 26a23456"))     
    print(is_phone_number("+371 26123 456"))    
    print(is_phone_number("+371 26123456"))
    print(is_phone_number("+371 12345678"))
    print(is_phone_number("+371 87654321"))
    print("Vēcuma parbaude:")
    print(is_valid_age(25))
    print(is_valid_age(0))      
    print(is_valid_age(150))   
    print(is_valid_age(-1)) 
    print(is_valid_age(200))  
    print(is_valid_age(25.5)) 
    print(is_valid_age("25"))  
    print("Paroles parbaude:")
    print(is_strong_password("abc12345"))   
    print(is_strong_password("password1")) 
    print(is_strong_password("abcdefg"))
    print(is_strong_password("12345678"))
    print(is_strong_password("abcd123"))
    print(is_strong_password("abcdefgh"))
    print("Datuma parbaude:")
    print(is_valid_date("2024-05-10"))
    print(is_valid_date("1999-12-31"))
    print(is_valid_date("2024-5-10"))
    print(is_valid_date("2024-05-1"))
    print(is_valid_date("2024/05/10"))
    print(is_valid_date("abcd-ef-gh"))