from typing import override

import pygame as pg

from cellular_automation import View, Agent


class LifeView(View):
    COLOR_LIVE = pg.Color("#0CFF00")
    COLOR_ALIVE = pg.Color("#000000")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._border_width = 0

    @override
    def render_agent(self, agent: type[Agent] | None, screen: pg.Surface, rect: pg.Rect) -> None:
        from .life_agent import AgentStatus

        if agent is None:
            return
        match agent.status:
            case AgentStatus.LIVE:
                pg.draw.rect(screen, self.COLOR_LIVE, rect)
            case AgentStatus.ALIVE:
                pg.draw.rect(screen, self.COLOR_ALIVE, rect)
