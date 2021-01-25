from collections import deque
import json

"""
Python 3.7.4
Задача:На бесконечной координатной сетке находится муравей.
Муравей может перемещаться на 1 клетку вверх (x,y+1),
вниз (x,y-1), влево (x-1,y), вправо (x+1,y), по одной клетке за шаг.
Клетки, в которых сумма цифр в координате X
плюс сумма цифр в координате Y больше чем 25 недоступны муравью.
Например, клетка с координатами (59, 79) недоступна,
т.к. 5+9+7+9=30, что больше 25.
Сколько клеток может посетить муравей,
если его начальная позиция (1000,1000),
(включая начальную клетку).
"""


class AntScanner:
    """
    Сканер доступных муравью клеток. Ищет клетки, на которые муравей может попасть
    и клетки которое блокируют путь муравью. Результаты хранятся в двух множествах,
    доступных клеток и заблокированных клеток. Имеет метод записи результатов в JS
    объект. Имеет метод вывода числа достижимых для муравья клеток.
    """
    __slots__ = ('x_start', 'y_start', 'available_cells', 'unscanned_cells', 'block_sells')

    def __init__(self, x_start=1000, y_start=1000):
        self.x_start = x_start
        self.y_start = y_start
        self.available_cells = set()  # множество координат доступных для муравья клеток
        self.unscanned_cells = deque()  # очередь непросканированных клеток (подлежащих проверке)
        self.block_sells = set()  # множество клеток ограничивающих путь муравья

    def _scan(self, coordinates: tuple):
        """Проверяет все соседние клетки, и добавляет текущую клетку в пул доступных"""
        self.available_cells.add(coordinates)
        self._check((coordinates[0], coordinates[1] + 1))
        self._check((coordinates[0], coordinates[1] - 1))
        self._check((coordinates[0] + 1, coordinates[1]))
        self._check((coordinates[0] - 1, coordinates[1]))

    def _check(self, coordinates: tuple):
        """
        Если клетка не отмечена как заблокированная, доступная или подлежащая проверке, то
        если клетка доступна, она помечается как подлежащая проверке, а если нет как заблокированная
        """
        if (coordinates not in self.block_sells) and (
                coordinates not in self.available_cells) and (
                coordinates not in self.unscanned_cells):
            if self._cell_is_available(coordinates):
                self.unscanned_cells.append(coordinates)
            else:
                self.block_sells.add(coordinates)

    def _cell_is_available(self, coord: tuple) -> bool:
        """Если сумма цифр x координаты + сумма цифр y координаты больше 25 клетка не будет доступна"""
        if (self._sum_of_digits(coord[0]) + self._sum_of_digits(coord[1])) > 25:
            return False
        else:
            return True

    def _sum_of_digits(self, number: int) -> int:
        """Считает сумму цифр переданного числа"""
        return sum([int(i) for i in str(abs(number))])

    def save_results(self):
        """
        Сохраняет координаты начала поиска доступного пути,
        множество координат доступных клеток и
        множество координат клеток, блокирующих путь в JS файле,
        в объект "data".
        """
        with open("data.js", "w") as write_file:
            write_file.write('data = ')
            result = {
                "start": (self.x_start, self.y_start),
                "available_cells": tuple(self.available_cells),
                "block_cells": tuple(self.block_sells)
            }
            json.dump(result, write_file)

    def find_all(self):
        """
        Метод запускающий поиск достижимых клеток
        и клеток, блокирующих путь муравью
        """
        self._scan((self.x_start, self.y_start))
        while len(self.unscanned_cells) != 0:
            self._scan(self.unscanned_cells[0])
            self.unscanned_cells.popleft()

    def count_of_available_cells(self):
        """Количество доступных клеток"""
        return len(self.available_cells)


if __name__ == '__main__':
    ant = AntScanner(1000, 1000)
    ant.find_all()
    print(f'Количество клеток доступных для муравья: {ant.count_of_available_cells()}')
    ant.save_results()
