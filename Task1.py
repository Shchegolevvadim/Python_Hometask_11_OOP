# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time
"""Испортируем time для хранения данных во времени"""
class MyString(str):
    def __new__(cls, value: str, author: str):
        """Создаем функцию для хранения данных об авторе и времени на основе класса str """
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

if __name__ =='__main__':
    s = MyString("skfjskdfhjsdhf",'iryry')
    """Передаем данные """
    print(s)
    print(s.time)
    print(s.author)