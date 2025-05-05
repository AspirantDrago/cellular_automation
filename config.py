import dataclasses

import pygame as pg


@dataclasses.dataclass
class Padding:
    top: int
    right: int
    bottom: int
    left: int


class Config:
    # размеры
    COLUMNS = 60
    ROWS = 60

    CELL_SIZE = 10
    TITLE = 'Game of Life'

    PADDING = Padding(10, 10, 10, 10)

    WIDTH = COLUMNS * CELL_SIZE + PADDING.left + PADDING.right + 400
    HEIGHT = COLUMNS * CELL_SIZE + PADDING.top + PADDING.bottom
    SIZE = (WIDTH, HEIGHT)

    BACKGROUND_COLOR = pg.color.Color(255, 255, 255)

    FPS = 15
