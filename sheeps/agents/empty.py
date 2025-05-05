import random
from typing import override

from cellular_automation import Agent

from .grass import GrassAgent


class EmptyAgent(Agent):
    PROBABILITY_GRASS = 0.005

    STATUS = 0

    @override
    def update(self, *args, **kwargs):
        if random.random() < self.PROBABILITY_GRASS:
            self._automation.create_agent(self.row, self.col, GrassAgent)

    @override
    @property
    def status(self) -> int:
        return self.STATUS
