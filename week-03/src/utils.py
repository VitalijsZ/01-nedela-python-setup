def capitalize(text):
    """Pārvērš pirmo burtu lielajā.

    Args:
        text (str): ievades teksts

    Returns:
        str: teksts ar lielo pirmo burtu

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    return text.capitalize()


def truncate(text, max_len=20):
    """Apgriež tekstu un pievieno '...' ja tas pārsniedz max_len.

    Args:
        text (str): ievades teksts
        max_len (int): maksimālais garums (noklusējums 20)

    Returns:
        str: saīsināts vai oriģināls teksts

    Example:
        >>> truncate("Hello world", 5)
        'Hello...'
    """
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text


def count_words(text):
    """Saskaita vārdus tekstā.

    Args:
        text (str): ievades teksts

    Returns:
        int: vārdu skaits

    Example:
        >>> count_words("Hello world")
        2
    """
    return len(text.split())

def clamp(num, low, high):
    """Ierobežo skaitli norādītajā diapazonā.

    Args:
        num (int or float): skaitlis, ko ierobežot
        low (int or float): minimālā robeža
        high (int or float): maksimālā robeža

    Returns:
        int or float: ierobežotā vērtība

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    if num < low:
        return low
    elif num > high:
        return high
    else:
        return num

def is_prime(num):
    """Pārbauda, vai skaitlis ir pirmskaitlis.

    Args:
        num (int): skaitlis

    Returns:
        bool: True ja pirmskaitlis, False ja nav

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
    """
    if num <= 1: 
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factorial(n):
    """Aprēķina skaitļa faktoriālu (n!).

    Faktoriāls tiek definēts kā:
        n! = n * (n-1) * (n-2) * ... * 1
    Īpašs gadījums: 0! = 1

    Args:
        n (int): Vesels skaitlis (n >= 0)

    Returns:
        int: n faktoriāls

    Raises:
        ValueError: Ja n < 0

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

def total(numbers):
    """Aprēķina saraksta elementu summu.

    Args:
        numbers (list of int/float): Skaitļu saraksts

    Returns:
        int or float: Elementu summa

    Example:
        >>> total([1, 2, 3])
        6
    """
    result = 0
    for i in numbers:
        result += i
    return result

def average(numbers):
    """Aprēķina vidējo aritmētisko sarakstā.

    Args:
        numbers (list of int/float): Skaitļu saraksts

    Returns:
        float: Vidējā vērtība vai 0, ja saraksts tukšs

    Example:
        >>> average([1, 2, 3])
        2.0
    """
    if len(numbers) == 0:
        return 0

    total = 0
    for i in numbers:
        total += i

    return total / len(numbers)

if __name__ == "__main__":
    print(capitalize("hello"))
    print(truncate("I like Python programming."))
    print(truncate("I like Python."))
    print(count_words("Today is good and sunny wheather."))
    print(clamp(22, 10, 20))
    print(is_prime(7))
    print(factorial(3))
    print(total([1, 2, 3, 4, 5]))
    print(average([1, 2, 3, 4, 5]))
    

