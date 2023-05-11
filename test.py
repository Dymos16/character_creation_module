from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Вычисляет квадратный корень введенного числа."""
    if your_number <= 0:
        return
    calc_number = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. Это будет'
          f': {calc_number}')


print(message)
calc(25.5)
