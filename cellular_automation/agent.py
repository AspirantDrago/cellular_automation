from abc import ABCMeta, abstractmethod


class Agent(metaclass=ABCMeta):
    def __init__(self,
                 automation: 'Automation',
                 row: int,
                 col: int,
                 *args, **kwargs):
        self._automation = automation
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
