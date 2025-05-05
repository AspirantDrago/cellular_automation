import enum
import random
from typing import override

from cellular_automation import Agent, Automation


class AgentStatus(enum.IntEnum):
    LIVE = 1
    ALIVE = 0


class LifeAgent(Agent):
    LIVE_PROBABILITY = 0.1

    @override
    def __init__(self, automation: Automation,
                 row: int,
                 col: int):
        super().__init__(automation, row, col)
        self._status = AgentStatus.LIVE if random.random() < self.LIVE_PROBABILITY else AgentStatus.ALIVE

    def get_live_neighbours(self) -> int:
        return sum(
            bool(agent) for agent in self._automation.get_neighbors(self.row, self.col)
        )

    @override
    def update(self, *args, **kwargs):
        n = self.get_live_neighbours()
        if self._status == AgentStatus.ALIVE:
            if n == 3:
                self._status = AgentStatus.LIVE
        else:
            if n < 2 or n > 3:
                self._status = AgentStatus.ALIVE

    @override
    @property
    def status(self) -> AgentStatus:
        return self._status

    def __bool__(self) -> bool:
        return self.status is AgentStatus.LIVE
