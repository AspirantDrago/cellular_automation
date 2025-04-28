from .agent import Agent


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

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def create_agent(self, row: int, col: int, *args, **kwargs) -> Agent | None:
        if 0 <= row < self._rows and 0 <= col < self._cols:
            agent = self._agent_class(self, row, col, *args, **kwargs)
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


class ThoreMixin:
    def create_agent(self, row: int, col: int, *args, **kwargs) -> Agent | None:
        row %= self._rows
        col %= self._cols
        agent = self._agent_class(self, row, col, *args, **kwargs)
        self._grid[row][col] = agent
        return agent

    def get(self, row: int, col: int) -> Agent | None:
        return self._grid[row % self._rows][col % self._cols]
