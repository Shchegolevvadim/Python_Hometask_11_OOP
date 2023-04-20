# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

class Archive():
    """Класс содержит номера и значения."""
    _one = None
    def __init__(self, num: int, val: str) ->None:
        """"Добавляет числа и значения."""
        self.num = num
        self.val = val
    def __new__(cls, *args, **kwargs):
        """ Создает новые списки для чисел и значений."""
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one)
            cls._one.values.append(cls._one.val)
        return cls._one

    def __str__(self):
        """Метод представления для пользователя"""
        return f'Класс записывает число {self.num} в строку {self.val} в словарь'
    def __repr__(self):

        return f'Archive({self.num}, "{self.val}")'
    """Метод представления для программиста"""
s = Archive(123, 'Formula')
print(s.numbers, s.values)

s = Archive(789, 'yacht-tour')
print(s.numbers, s.values)

s = Archive(312, 'tournament')
print(s.numbers, s.values)