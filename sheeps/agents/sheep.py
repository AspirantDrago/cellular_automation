import random
from typing import override
from math import dist

from cellular_automation import Agent
from .empty import EmptyAgent
from .grass import GrassAgent


class SheepAgent(Agent):
    MIN_POWER = 250
    MAX_POWER = 300

    MIN_AGE = 2000
    MAX_AGE = 3000

    STATUS = 2

    RADIUS = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._power = random.randint(self.MIN_POWER, self.MAX_POWER)
        self._age = random.randint(self.MIN_AGE, self.MAX_AGE)

    @property
    def power(self) -> int:
        return self._power

    @override
    def update(self, *args, **kwargs):
        self._age -= 1
        self._power -= 1
        if self._age <= 0 or self._power <= 0:
            self.death()
            return
        self.find_grass()

    def find_grass(self) -> None:
        min_distance = float('inf')
        diff: list[tuple[int, int]] = []
        for row in range(self.row - self.RADIUS, self.row + self.RADIUS + 1):
            for col in range(self.col - self.RADIUS, self.col + self.RADIUS + 1):
                if isinstance(self._automation(row, col), GrassAgent):
                    distance = dist((self.row, self.col), (row, col))
                    if distance < min_distance and distance <= self.RADIUS:
                        diff.clear()
                    if distance <= min_distance and distance <= self.RADIUS:
                        min_distance = distance
                        diff_row = diff_col = 0
                        if row < self.row:
                            diff_row = -1
                        elif row > self.row:
                            diff_row = 1
                        if col < self.col:
                            diff_col = -1
                        elif col > self.col:
                            diff_col = 1
                        diff.append((diff_row, diff_col))
        if diff:
            diff_row, diff_col = random.choice(diff)
            self.move(self.row + diff_row, self.col + diff_col)

    def move(self, new_row: int, new_col: int) -> None:
        old_agent = self._automation(new_row, new_col)
        if isinstance(old_agent, GrassAgent):
            self._power += old_agent.power
        if isinstance(old_agent, GrassAgent) or isinstance(old_agent, EmptyAgent):
            self._automation.create_agent(self.row, self.col, EmptyAgent)
            self._automation._grid[new_row][new_col] = self
            self._row = new_row
            self._col = new_col

    def death(self):
        self._automation.create_agent(self.row, self.col, EmptyAgent)

    @override
    @property
    def status(self) -> int:
        return self.STATUS
