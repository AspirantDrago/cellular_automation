from abc import ABCMeta, abstractmethod


class Agent(metaclass=ABCMeta):
    """
    Абстрактный класс агента для имитационной модели клеточного автомата
    """

    def __init__(self,
                 automation: 'Automation',
                 row: int,
                 col: int,
                 *args, **kwargs):
        """
        Инициализация агента

        :param automation: Объект клеточного автомата, к которому привязан агент
        :param row: строка, в которой создаётся агент. Индексация начинается с нуля
        :param col: столбец, в которой создаётся агент. Индексация начинается с нуля
        :param args: Дополнительные позиционные аргументы, которые могут понадобиться в конкретных реализациях агентов
        :param kwargs: Дополнительные именованные аргументы, которые могут понадобиться в конкретных реализациях агентов
        """
        from .automation import Automation

        self._automation: Automation = automation
        self._row = row
        self._col = col

    @abstractmethod
    def update(self, *args, **kwargs):
        ...

    @property
    @abstractmethod
    def status(self) -> int:
        ...

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col
