# високосный год: 
def is_year_leap(year):
    if (year % 4 == 0 and (not year % 100 == 0)) or year % 400 == 0:
        return True
    else:
        return False

year = int(input('Введите год: '))
answer = is_year_leap(year)
print(f'год {year}: {answer}')
