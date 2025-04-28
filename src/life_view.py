from typing import override

import pygame as pg

from cellular_automation import View, Automation, Agent
from .life_agent import AgentStatus


class LifeView(View):
    COLOR_LIVE = pg.Color("#0CFF00")
    COLOR_ALIVE = pg.Color("#000000")

    @override
    def render_agent(self, agent: type[Agent] | None, screen: pg.Surface, rect: pg.Rect) -> None:
        if agent is None:
            return
        match agent.status:
            case AgentStatus.LIVE:
                pg.draw.rect(screen, self.COLOR_LIVE, rect)
            case AgentStatus.ALIVE:
                pg.draw.rect(screen, self.COLOR_ALIVE, rect)
