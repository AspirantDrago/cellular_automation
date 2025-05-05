import random

from cellular_automation import Automation, MooreNeighborhoodMixin, ThoreMixin
from .agents import EmptyAgent, SheepAgent


class SheepModel(Automation, MooreNeighborhoodMixin):
    def __init__(self,
                 rows: int,
                 cols: int,
                 count_sheep: int
                 ) -> None:
        super().__init__(rows, cols, EmptyAgent)
        while count_sheep > 0:
            row = random.randrange(rows)
            col = random.randrange(rows)
            if isinstance(self(row, col), EmptyAgent):
                count_sheep -= 1
                self.create_agent(row, col, SheepAgent)
