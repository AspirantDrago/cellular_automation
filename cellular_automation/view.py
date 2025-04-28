from abc import ABCMeta, abstractmethod

import pygame as pg

from cellular_automation import Automation, Agent


class View(metaclass=ABCMeta):
    def __init__(self,
                 model: Automation,
                 cell_size: int):
        self._model = model
        self._cell_size = cell_size
        self._border_color = pg.Color(0, 0, 0)
        self._border_width = 1

    @property
    def border_color(self) -> pg.Color:
        return self._border_color

    @property
    def border_width(self) -> int:
        return self._border_width

    @border_width.setter
    def border_width(self, value: int) -> None:
        self._border_width = value

    @border_color.setter
    def border_color(self, value: pg.Color) -> None:
        self._border_color = value

    def render(self) -> pg.Surface:
        screen = pg.surface.Surface(
            (self._model.cols * self._cell_size, self._model.rows * self._cell_size),
            pg.SRCALPHA
        )
        for row in range(self._model.rows):
            for col in range(self._model.cols):
                rect = pg.Rect(row * self._cell_size, col * self._cell_size, self._cell_size, self._cell_size)
                self.render_agent(self._model(row, col), screen, rect)
                pg.draw.rect(screen, self._border_color, rect, 1)
        return screen

    @abstractmethod
    def render_agent(self, agent: type[Agent] | None, screen: pg.Surface, rect: pg.Rect) -> None:
        ...
