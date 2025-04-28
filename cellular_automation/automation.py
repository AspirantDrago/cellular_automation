from .agent import Agent


class Automation:
    def __init__(self,
                 rows: int,
                 cols: int,
                 agent_class: type[Agent],
                 ) -> None:
        self._rows = rows
        self._cols = cols
        self._status = False
        self._agent_class = agent_class

    @property
    def status(self) -> bool:
        return self._status

    def start(self) -> None:
        self._status = True

    def stop(self) -> None:
        self._status = False
