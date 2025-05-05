from collections import Counter

import pygame as pg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

from .plot_line import PlotLine
from .agent import Agent


class Plot:
    def __init__(self,
                 model: 'Automation',
                 count_last: int = 100,
                 title: str | None = None,
                 xlabel: str = 'time',
                 ylabel: str = 'count',
                 ):
        self._model = model
        self._lines: dict[int, PlotLine] = {}
        self._t: list = []
        self.count_last = count_last
        self.title = title
        self.x_label = xlabel
        self.y_label = ylabel

    def get_line(self, status: int) -> PlotLine:
        if status not in self._lines:
            self._lines[status] = PlotLine(status)
        return self._lines[status]

    def update(self) -> None:
        cntr = Counter(agent.status for agent in self._model)
        statuses = set(cntr) | set(self._lines)
        for status in statuses:
            self.get_line(status).append(cntr.get(status, 0))
        self._t.append(len(self._t))

    def render(self, size: tuple[int, int] | None = None) -> pg.Surface:
        figsize = (4, 4)
        if size is not None:
            figsize = (size[0] // 100 + 1, size[1] // 100 + 1)
        fig = Figure(figsize=figsize, dpi=100)
        ax = fig.subplots()

        count_last = min(self.count_last, len(self._t))
        for line in self._lines.values():
            if line.visible:
                ax.plot(self._t[-count_last:], line.get_last(count_last), color=line.color, label=str(line))
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        if self.title is not None:
            ax.set_title(self.title)
        fig.legend(loc='lower right')
        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        img = pg.image.frombytes(canvas.tostring_argb(), canvas.get_width_height(), "ARGB")
        if size is not None:
            img = pg.transform.smoothscale(img, size)
        return img
