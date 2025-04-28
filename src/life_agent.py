import enum
import random
from typing import override

from cellular_automation import Agent, Automation


class AgentStatus(enum.IntEnum):
    LIVE = 1
    ALIVE = 0


class LifeAgent(Agent):
    @override
    def __init__(self, automation: Automation,
                 row: int,
                 col: int):
        super().__init__(automation, row, col)
        self._status = random.choice([AgentStatus.ALIVE, AgentStatus.LIVE])

    @override
    def update(self, *args, **kwargs):
        raise NotImplementedError()

    @override
    @property
    def status(self) -> AgentStatus:
        return self._status
