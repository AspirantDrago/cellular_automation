from typing import override

import pygame as pg

from cellular_automation import View, Agent
from .agents import *


class SheepView(View):
    COLOR_EMPTY = pg.Color("#FFFFFF")
    COLOR_GRASS = pg.Color("#05FF47")
    COLOR_SHEEP = pg.Color("#FF9BAD")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._border_width = 0

    @override
    def render_agent(self, agent: type[Agent] | None, screen: pg.Surface, rect: pg.Rect) -> None:
        if agent is None:
            return
        match agent:
            case EmptyAgent():
                pg.draw.rect(screen, self.COLOR_EMPTY, rect)
            case GrassAgent():
                pg.draw.rect(screen, self.COLOR_GRASS, rect)
            case SheepAgent():
                pg.draw.rect(screen, self.COLOR_SHEEP, rect)
