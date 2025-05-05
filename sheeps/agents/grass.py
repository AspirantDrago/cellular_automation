import random
from typing import override

from cellular_automation import Agent, Automation


class GrassAgent(Agent):
    MIN_POWER = 3
    MAX_POWER = 5

    STATUS = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._power = random.randint(self.MIN_POWER, self.MAX_POWER)

    @property
    def power(self) -> int:
        return self._power

    @override
    def update(self, *args, **kwargs):
        ...

    @override
    @property
    def status(self) -> int:
        return self.STATUS
