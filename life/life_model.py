from cellular_automation import Automation, MooreNeighborhoodMixin, ThoreMixin
from .life_agent import LifeAgent, AgentStatus


class LifeModel(ThoreMixin, Automation, MooreNeighborhoodMixin):

    def __init__(self,
                 rows: int,
                 cols: int,
                 ) -> None:
        super().__init__(rows, cols, LifeAgent)
