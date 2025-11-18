# General Programming Logic Assignment
# Author: Sivaram K

# (Full code below)

def add_two_numbers(a, b):
    return a + b

def get_biggest_between_two_numbers(a, b):
    return a if a > b else b

def is_even(number):
    return number % 2 == 0

def get_grade_for_three_subjects(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    if avg > 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "A-"
    elif avg >= 60:
        return "B+"
    elif avg >= 50:
        return "B"
    else:
        return "FAIL"

def get_first_10_natural_numbers():
    return list(range(1, 11))

def get_first_10_natural_numbers_reverse():
    return list(range(10, 0, -1))

def get_first_10_even_numbers():
    return [num for num in range(1, 21) if num % 2 == 0]

def get_numbers_in_range(start, end):
    return list(range(start, end + 1))

def get_multiplication_table(number):
    return [number * i for i in range(1, 11)]

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_prime_numbers_between_2_to_100():
    return [n for n in range(2, 101) if is_prime(n)]

def sum_of_digits(number):
    return sum(int(d) for d in str(abs(number)))

def get_lucky_number(number):
    while number > 9:
        number = sum_of_digits(number)
    return number

def get_reverse_number(number):
    rev = int(str(abs(number))[::-1])
    return -rev if number < 0 else rev

def is_palindrome(number):
    return number == get_reverse_number(number)

def get_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def ncr(n, r):
    return get_factorial(n) // (get_factorial(n-r) * get_factorial(r))

def digit_to_word(d):
    mapping = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    return mapping.get(d, "Invalid Digit")

def number_to_words(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

    num = int(num)

    if num == 0:
        return "Zero"

    words = ""

    if num >= 100:
        words += ones[num // 100] + " Hundred "
        num %= 100

    if 10 <= num <= 19:
        words += teens[num - 10]
    else:
        words += tens[num // 10]
        if num % 10 != 0:
            words += " " + ones[num % 10]

    return words.strip()
