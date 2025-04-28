from cellular_automation import Automation, MooreNeighborhoodMixin, ThoreMixin
from .life_agent import LifeAgent, AgentStatus


class LifeModel(Automation, MooreNeighborhoodMixin, ThoreMixin):
    def __init__(self,
                 rows: int,
                 cols: int,
                 ) -> None:
        fake_agent = LifeAgent(self, -1, -1)
        fake_agent._status = AgentStatus.ALIVE
        super().__init__(rows, cols, LifeAgent, fake_agent)
