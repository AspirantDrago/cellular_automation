import itertools
from copy import deepcopy
from typing import Iterator

from .agent import Agent
from .plot import Plot


class Automation:
    def __init__(self,
                 rows: int,
                 cols: int,
                 agent_class: type[Agent],
                 fake_agent: Agent | None = None,
                 ) -> None:
        self._rows = rows
        self._cols = cols
        self._status = False
        self._agent_class = agent_class
        self._fake_agent = fake_agent
        self._grid: list[list[Agent]] = [
            [agent_class(self, row, col) for col in range(self._cols)]
            for row in range(self._rows)
        ]
        self._plot : Plot | None = None

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def create_agent(self,
                     row: int,
                     col: int,
                     agent_class: type[Agent] | None = None,
                     *args, **kwargs) -> Agent | None:
        if 0 <= row < self._rows and 0 <= col < self._cols:
            if agent_class is None:
                agent_class = self._agent_class
            agent = agent_class(self, row, col, *args, **kwargs)
            self._grid[row][col] = agent
            return agent
        return self._fake_agent

    def get(self, row: int, col: int) -> Agent | None:
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._grid[row][col]
        return self._fake_agent

    def __call__(self, row: int, col: int) -> Agent | None:
        return self.get(row, col)

    @property
    def status(self) -> bool:
        return self._status

    def start(self) -> None:
        self._status = True

    def stop(self) -> None:
        self._status = False

    def update(self, *args, **kwargs) -> None:
        copy_grid = deepcopy(self._grid)
        for row in range(self._rows):
            for col in range(self._cols):
                copy_grid[row][col].update(*args, **kwargs)
        self._grid = copy_grid
        if self._plot is not None:
            self._plot.update()

    def get_all_agents(self) -> list[Agent | None]:
        return list(itertools.chain.from_iterable(self._grid))

    def __iter__(self) -> Iterator[Agent]:
        for row in self._grid:
            for agent in row:
                if agent is not None:
                    yield agent

    def create_plot(self) -> Plot:
        if self._plot is None:
            self._plot = Plot(self)
        return self._plot


class ThoreMixin:
    def create_agent(self, row: int, col: int, *args, **kwargs) -> Agent | None:
        row %= self._rows
        col %= self._cols
        agent = self._agent_class(self, row, col, *args, **kwargs)
        self._grid[row][col] = agent
        return agent

    def get(self, row: int, col: int) -> Agent | None:
        return self._grid[row % self._rows][col % self._cols]


class MooreNeighborhoodMixin:
    MOORE_RADIUS = 1

    def get_neighbors(self, row: int, col: int) -> list[Agent]:
        result = []
        for row2 in range(row - self.MOORE_RADIUS, row + self.MOORE_RADIUS + 1):
            for col2 in range(col - self.MOORE_RADIUS, col + self.MOORE_RADIUS + 1):
                if row == row2 and col == col2:
                    continue
                result.append(self.get(row2, col2))
        return result
